# -*- coding: utf-8 -*-
"""Construtor de grades do laboratório (cobertura, nunca previsão).
Mantém jogos FIXOS (ex.: espiral J) e otimiza N jogos NOVOS que mais complementam o conjunto inteiro, em 3 bancos separados
(construção / seleção / teste), com controle de 40 grades aleatórias, e relatório com: custo, E[max], P(>=15), P(>=17),
chance exata de 20 e de 20-ou-0, piso garantido (adversário exato) e retorno esperado aproximado.
Exemplos:
  python3 lab/construtor.py --novos 10 --nome K10b
  python3 lab/construtor.py --fixos data/jogos_C2988.json --grupos J --novos 6 --nome J_mais6
  python3 lab/construtor.py --nucleo-relogio --novos 10 --nome R10b      # núcleo girando do Rafael, apoio otimizado
Objetivos: --obj emax (E[max] + 4·P(≥15), padrão) | p15 (só P(≥15)) | cauda (P(≥15) + 20·P(≥17))."""
import argparse, json, os, sys
import numpy as np
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(RAIZ, "lab"))
from ferramentas import sorteios_simulados, valido
from zero_acertos import p_uniao

def objetivo(nome):
    if nome == "p15": return lambda m: (m >= 15).mean()
    if nome == "cauda": return lambda m: (m >= 15).mean() + 20 * (m >= 17).mean()
    return lambda m: m.mean() + 4 * (m >= 15).mean()

def hits(DT, jogo): return DT[sorted(jogo)].sum(0, dtype=np.int16).astype(np.int8)

def construir(fixos, n_novos, DT, seed, tent, obj, sobrep_max=40, nucleos=None):
    """Otimiza só os n_novos jogos; os fixos entram na conta de cobertura. nucleos (opcional): 20 dezenas fixas por jogo novo."""
    rng = np.random.default_rng(seed); f = objetivo(obj)
    mxf = np.max([hits(DT, g) for g in fixos], axis=0) if fixos else np.zeros(DT.shape[1], np.int8)
    novos, livres = [], []
    for k in range(n_novos):
        nuc = set(nucleos[k]) if nucleos else set()
        liv = sorted(set(range(100)) - nuc); livres.append(liv)
        while True:
            g = nuc | set(rng.choice(liv, 50 - len(nuc), replace=False).tolist())
            if valido(g): break
        novos.append(g)
    H = np.stack([hits(DT, g) for g in novos]); cur = f(np.maximum(mxf, H.max(0)))
    for _ in range(tent):
        j = int(rng.integers(n_novos)); g = novos[j]; nuc = set(nucleos[j]) if nucleos else set()
        movel = sorted(g - nuc); s = int(rng.choice(movel)); e = int(rng.choice(sorted(set(livres[j]) - g)))
        nv = (g - {s}) | {e}
        if not valido(nv): continue
        if any(len(nv & o) > sobrep_max for k, o in enumerate(novos) if k != j) or any(len(nv & set(o)) > sobrep_max for o in fixos): continue
        old = H[j].copy(); H[j] = old - DT[s] + DT[e]; v = f(np.maximum(mxf, H.max(0)))
        if v > cur: cur, novos[j] = v, nv
        else: H[j] = old
    return [sorted(g) for g in novos]

def metricas(D, jogos):
    V = np.zeros((100, len(jogos)), np.float32)
    for j, g in enumerate(jogos): V[g, j] = 1
    m = (D @ V).max(1); return m.mean(), (m >= 15).mean(), (m >= 17).mean()

def carregar_fixos(arq, grupos):
    d = json.load(open(arq, encoding="utf-8")); return [g["dezenas"] for gr in d["grupos"] if gr["id"] in grupos for g in gr["jogos"]]

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--novos", type=int, required=True); ap.add_argument("--nome", default="NOVO")
    ap.add_argument("--fixos"); ap.add_argument("--grupos", default="J"); ap.add_argument("--obj", default="emax"); ap.add_argument("--tent", type=int, default=30000)
    ap.add_argument("--reinicios", type=int, default=4); ap.add_argument("--nucleo-relogio", action="store_true"); ap.add_argument("--sem-garantia", action="store_true")
    ap.add_argument("--acumulado", type=float, default=14.0, help="prêmio estimado em milhões, só para o retorno aproximado")
    a = ap.parse_args()
    fixos = carregar_fixos(a.fixos, a.grupos.split(",")) if a.fixos else []
    nucleos = None
    if a.nucleo_relogio:
        from relogio import nucleo; nucleos = [sorted(nucleo(k)) for k in range(a.novos)]
    DT = np.ascontiguousarray(sorteios_simulados(150_000, 1).T.astype(np.int8)); Dsel = sorteios_simulados(400_000, 555); Dte = sorteios_simulados(800_000, 777)
    f = objetivo(a.obj); cands = [construir(fixos, a.novos, DT, 100 + s, a.tent, a.obj, nucleos=nucleos) for s in range(a.reinicios)]
    def pontua(novos):
        V = np.zeros((100, len(fixos) + len(novos)), np.float32)
        for j, g in enumerate(fixos + novos): V[g, j] = 1
        return f((Dsel @ V).max(1))
    melhor = cands[int(np.argmax([pontua(c) for c in cands]))]; grade = fixos + melhor
    rng = np.random.default_rng(2026); ctrl = []
    while len(ctrl) < 40:
        g = [sorted(rng.choice(100, 50, replace=False).tolist()) for _ in range(len(grade))]
        if all(valido(x) for x in g): ctrl.append(metricas(Dte, g))
    C = np.array(ctrl); m = metricas(Dte, grade)
    S = [set(g) for g in grade]; u20, t, _ = p_uniao(S); u20_0, _, _ = p_uniao(S + [set(range(100)) - s for s in S])
    N = len(grade); ev = (0.61 + 0.0887 * a.acumulado)
    print(f"\n=== {a.nome}: {len(fixos)} fixos + {a.novos} novos = {N} jogos | custo R$ {3*N} ===")
    print(f"teste 800 mil inéditos: E[max] {m[0]:.3f} (aleatórios {C[:,0].mean():.3f}, faixa {C[:,0].min():.3f}–{C[:,0].max():.3f}) | P(>=15) {100*m[1]:.2f}% (aleat. {100*C[:,1].mean():.2f}%) | P(>=17) {100*m[2]:.3f}% (aleat. {100*C[:,2].mean():.3f}%)")
    print(f"ganho de cobertura sobre aleatórios: {m[0]-C[:,0].mean():+.3f} em E[max]")
    print(f"chance de 20: 1 em {1/u20:,.0f} | de 20 ou 0: 1 em {1/u20_0:,.0f} | teto {N}/11,37 mi")
    if not a.sem_garantia:
        from garantia import pior_sorteio
        print(f"piso garantido (pior sorteio possível): melhor jogo >= {pior_sorteio(grade, 60)[0]}")
    print(f"retorno esperado aproximado a R$ {a.acumulado:.0f} mi: ≈ R$ {N*ev:.0f} sobre R$ {3*N} gastos ({100*ev/3:.0f}% do preço; supõe ser o único ganhador)")
    out = os.path.join(RAIZ, "data", f"jogos_{a.nome}.json")
    json.dump({"nome": a.nome, "objetivo": a.obj, "fixos": len(fixos), "jogos": {f"{a.nome}{k+1}": g for k, g in enumerate(melhor)}}, open(out, "w"), indent=1)
    print("salvo em", os.path.relpath(out, RAIZ))
    for k, g in enumerate(melhor): print(f"{a.nome}{k+1}: " + " ".join(f"{x:02d}" for x in g))
