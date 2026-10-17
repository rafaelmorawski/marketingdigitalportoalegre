# -*- coding: utf-8 -*-
"""1) Cálculo exato: chance de o jogo 2 fazer 20 dado que o jogo 1 fez 8..14, em função da sobreposição a=|G1∩G2|.
   2) Construção sequencial (cada jogo otimizado só nos sorteios em que os anteriores falham) vs otimização conjunta (K10)."""
import json, os, sys
import numpy as np
from math import comb
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(RAIZ, "lab"))
from ferramentas import sorteios_simulados, valido

DEN = comb(100, 20)

def p20_dado_falha(a, lo=8, hi=14):
    """P(G2=20 | h1 em lo..hi) e P(G2=20 e h1 em lo..hi); a = |G1∩G2|, G2 tem a dentro de G1 e 50-a fora."""
    conj = sum(comb(a, h) * comb(50 - a, 20 - h) for h in range(lo, hi + 1))      # sorteios com G2=20 e h1=h (h em G1∩G2)
    ph = sum(comb(50, h) * comb(50, 20 - h) for h in range(lo, hi + 1)) / DEN     # P(h1 em lo..hi)
    return conj / DEN / ph, conj / DEN

def sequencial(DT, seed, tent, n=10):
    rng = np.random.default_rng(seed); jogos = []; mx = np.zeros(DT.shape[1], np.int8)
    for k in range(n):
        while True:
            g = set(rng.choice(100, 50, replace=False).tolist())
            if valido(g): break
        h = DT[sorted(g)].sum(0, dtype=np.int16).astype(np.int8)
        f = lambda h: (lambda m: m.mean() + 4 * (m >= 15).mean())(np.maximum(mx, h)); cur = f(h)
        for _ in range(tent):
            s = int(rng.choice(sorted(g))); e = int(rng.choice(sorted(set(range(100)) - g)))
            nv = (g - {s}) | {e}
            if not valido(nv): continue
            hn = h - DT[s] + DT[e]; v = f(hn)
            if v > cur: cur, g, h = v, nv, hn
        jogos.append(sorted(g)); mx = np.maximum(mx, h)
    return jogos

def av(D, J):
    V = np.zeros((100, len(J)), np.float32)
    for j, g in enumerate(J): V[g, j] = 1
    m = (D @ V).max(1); return m.mean(), (m >= 15).mean(), (m >= 17).mean()

if __name__ == "__main__":
    base = 1 / DEN * comb(50, 20)
    print(f"chance incondicional de um jogo fazer 20: 1 em {1/base:,.0f}\n")
    print(" a=|G1∩G2|   P(G2=20 | G1 fez 8–14)   lift vs incondicional   P(G2=20 e G1 fez 8–14)")
    melhor = (0, 0)
    for a in (0, 10, 15, 20, 22, 25, 28, 30, 35, 40, 50):
        c, j = p20_dado_falha(a)
        print(f"  {a:3d}        " + ("impossível" if c == 0 else f"1 em {1/c:>12,.0f}           x{c/base:5.2f}               1 em {1/j:>12,.0f}"))
    r = [(p20_dado_falha(a)[0], a) for a in range(0, 51)]; print("\nmelhor sobreposição para o jogo 2 (condicional):", max(r)[1])
    r2 = [(p20_dado_falha(a)[1], a) for a in range(0, 51)]; print("melhor sobreposição para P(G2=20 E G1 fez 8–14):", max(r2)[1])
    Dc = sorteios_simulados(150_000, 1); DT = np.ascontiguousarray(Dc.T.astype(np.int8))
    Dsel = sorteios_simulados(400_000, 555); Dte = sorteios_simulados(800_000, 777)
    c = [sequencial(DT, s, 8000) for s in range(30, 34)]
    best = max(c, key=lambda J: (lambda a: a[0] + 4 * a[1])(av(Dsel, J)))
    K = list(json.load(open(os.path.join(RAIZ, "data", "jogos_C2989_K10.json")))["jogos"].values())
    R = list(json.load(open(os.path.join(RAIZ, "data", "jogos_C2989_R10.json")))["jogos"].values())
    print("\nTESTE 800 mil simulados inéditos:        E[max]  P(>=15)  P(>=17)")
    for nome, J in [("sequencial (jogo k cobre onde 1..k-1 falham)", best), ("K10 (otimização conjunta)", K), ("R10 (relógio + apoio otimizado)", R)]:
        a = av(Dte, J); print(f"  {nome:46s} {a[0]:.3f}  {100*a[1]:.2f}%   {100*a[2]:.3f}%")
