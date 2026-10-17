# -*- coding: utf-8 -*-
"""Variantes do relógio do Rafael (espiral J): núcleo de 20 (2 por década, par vizinho) que gira 2 casas por jogo (período 5),
J1–J5 e J6–J10 com o mesmo núcleo. Varia SÓ a escolha do apoio de 30. Três bancos: construção / seleção / teste (simulados)."""
import json, os, sys
import numpy as np
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(RAIZ, "lab"))
from ferramentas import sorteios_simulados, valido

I0 = [0, 2, 4, 7, 6, 4, 7, 8, 3, 2]       # posição inicial do par em cada década (núcleo do J1: 00 01 12 13 ... 37 38 ...)

def nucleo(k, passo=2, i0=I0):
    n = set()
    for dec in range(10):
        i = (i0[dec] + passo * (k % 5)) % 10
        n |= {dec * 10 + i, dec * 10 + (i + 1) % 10}
    return n

def evolui(DT, nuc, regra, seed, tent):
    """Hill-climbing só no apoio de 30; regra: apoio nunca contém dezenas do núcleo do jogo anterior."""
    rng = np.random.default_rng(seed)
    proib = [(nuc[k - 1] if (regra and k > 0) else set()) for k in range(10)]
    livres = [sorted(set(range(100)) - nuc[k] - proib[k]) for k in range(10)]
    apoio = [set(rng.choice(livres[k], 30, replace=False).tolist()) for k in range(10)]
    if tent == 0: return [sorted(nuc[k] | apoio[k]) for k in range(10)]
    H = np.stack([DT[sorted(nuc[k] | apoio[k])].sum(0, dtype=np.int16) for k in range(10)]).astype(np.int8)
    f = lambda H: (lambda m: m.mean() + 4 * (m >= 15).mean())(H.max(0)); cur = f(H)
    for _ in range(tent):
        k = int(rng.integers(10)); sai = int(rng.choice(sorted(apoio[k]))); ent = int(rng.choice(sorted(set(livres[k]) - apoio[k])))
        old = H[k].copy(); H[k] = old - DT[sai] + DT[ent]; v = f(H)
        if v > cur: cur = v; apoio[k] = (apoio[k] - {sai}) | {ent}
        else: H[k] = old
    return [sorted(nuc[k] | apoio[k]) for k in range(10)]

def av(D, J):
    V = np.zeros((100, 10), np.float32)
    for j, g in enumerate(J): V[g, j] = 1
    mx = (D @ V).max(1); return mx.mean(), (mx >= 15).mean(), (mx >= 17).mean()

if __name__ == "__main__":
    Dc = sorteios_simulados(150_000, 1); DT = np.ascontiguousarray(Dc.T.astype(np.int8))
    Dsel = sorteios_simulados(400_000, 555); Dte = sorteios_simulados(800_000, 777)
    nuc = [nucleo(k) for k in range(10)]
    J = [g["dezenas"] for gr in json.load(open(os.path.join(RAIZ, "data", "jogos_C2988.json")))["grupos"] if gr["id"] == "J" for g in gr["jogos"]]
    K = list(json.load(open(os.path.join(RAIZ, "data", "jogos_C2989_K10.json")))["jogos"].values())
    rng = np.random.default_rng(2026); ctrl = []
    while len(ctrl) < 40:
        g = [sorted(rng.choice(100, 50, replace=False).tolist()) for _ in range(10)]
        if all(valido(x) for x in g): ctrl.append(av(Dte, g))
    C = np.array(ctrl)
    linhas = [("40 aleatórios (média)", tuple(C.mean(0))), ("J espiral real (suporte do Rafael)", av(Dte, J)), ("K10 (livre, sem estrutura)", av(Dte, K))]
    for nome, regra, tent in [("Relógio + apoio ALEATÓRIO (com regra)", True, 0), ("Relógio + apoio ALEATÓRIO (sem regra)", False, 0),
                              ("Relógio + apoio OTIMIZADO (com regra)", True, 30_000), ("Relógio + apoio OTIMIZADO (sem regra)", False, 30_000)]:
        c = [evolui(DT, nuc, regra, s, tent) for s in range(10, 14 if tent else 11)]
        best = max(c, key=lambda J_: (lambda a: a[0] + 4 * a[1])(av(Dsel, J_)))
        linhas.append((nome, av(Dte, best)))
    print(f"TESTE FINAL (800 mil sorteios simulados inéditos); controle E[max] faixa {C[:,0].min():.3f}–{C[:,0].max():.3f}\n")
    print(f"{'grupo':42s} E[max]  P(>=15)  P(>=17)  ganho")
    for n, r in linhas: print(f"{n:42s} {r[0]:.3f}  {100*r[1]:.2f}%   {100*r[2]:.3f}%  {r[0]-C[:,0].mean():+.3f}")
