# -*- coding: utf-8 -*-
"""O prêmio de 0 acertos: relação com os 20, sobreposição entre jogos, valor esperado e o que os dados de ganhadores ensinam."""
import csv, itertools, json, os, sys
import numpy as np
from math import comb
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(RAIZ, "lab"))
DEN = comb(100, 20)

def p_uniao(sets):
    """P(sorteio ⊂ algum conjunto), Bonferroni de 2ª ordem: Σ P_i − Σ P_ij  (P_ij = C(|Si∩Sj|,20)/C(100,20))."""
    s1 = len(sets) * comb(50, 20); s2 = sum(comb(len(a & b), 20) for a, b in itertools.combinations(sets, 2))
    return (s1 - s2) / DEN, s1 / DEN, s2 / DEN

def num(s):
    s = s.replace("R$", "").replace(".", "").replace(",", ".").strip()
    try: return float(s)
    except ValueError: return np.nan

if __name__ == "__main__":
    J = [g["dezenas"] for gr in json.load(open(os.path.join(RAIZ, "data", "jogos_C2988.json")))["grupos"] if gr["id"] == "J" for g in gr["jogos"]]
    TODOS = [g["dezenas"] for gr in json.load(open(os.path.join(RAIZ, "data", "jogos_C2988.json")))["grupos"] for g in gr["jogos"]]
    K = list(json.load(open(os.path.join(RAIZ, "data", "jogos_C2989_K10.json")))["jogos"].values())
    R = list(json.load(open(os.path.join(RAIZ, "data", "jogos_C2989_R10.json")))["jogos"].values())
    print("1) MATEMÁTICA: 0 acertos de T = 20 acertos do espelho de T (complemento). P por bilhete = 1 em", f"{DEN/comb(50,20):,.0f}", "para os dois.\n")
    print("   chance de 'algum jogo faz 20' e de 'algum jogo faz 20 OU 0' (a união conta os 2N conjuntos: jogos e espelhos):")
    print(f"   {'grupo':22s} {'só 20':>16s} {'20 ou 0':>16s} {'teto 2N/11,37mi':>18s} {'perda por sobreposição':>24s}")
    for nome, G in [("J", J), ("K10", K), ("R10", R), ("24 jogos", TODOS)]:
        S = [set(g) for g in G]; M = [set(range(100)) - s for s in S]
        a, _, _ = p_uniao(S); b, t, c = p_uniao(S + M)
        print(f"   {nome:22s} 1 em {1/a:>11,.0f}  1 em {1/b:>11,.0f}  1 em {1/t:>13,.0f}   {100*c/t:.2e}%")
    print("\n   Sobreposição entre jogo j e espelho de k: |Gj \\ Gk| = 50 − a. Um mesmo sorteio faz 20 em j e 0 em k só se |Gj \\ Gk| ≥ 20, isto é, a ≤ 30.")
    print("   Nunca dá para evitar toda colisão (precisaria a < 20 e 50−a < 20), mas ela vale ~1e-9 do prêmio. Praticamente 2N chances independentes.\n")
    # ---- dados de ganhadores
    Rw = list(csv.reader(open(os.path.join(RAIZ, "data", "Lotomania.csv"), encoding="latin1"))); ix = {n: i for i, n in enumerate(Rw[0])}
    c20 = ix["Ganhadores 20 acertos"]; c0 = ix["Ganhadores Nenhum Número"]; r0 = ix["Rateio Nenhum Número"]; r20 = ix["Rateio 20 acertos"]; ar = ix["Arrecadação Total"]
    rows = []
    for r in Rw[1:]:
        rows.append((int(r[0]), [int(x) for x in r[2:22]], num(r[c20]), num(r[c0]), num(r[r0]), num(r[r20]), num(r[ar])))
    ult = [x for x in rows if x[0] > rows[-1][0] - 300 and x[4] == x[4] or x[0] > rows[-1][0] - 300]
    ult = [x for x in rows[-300:]]
    w20 = np.array([x[2] for x in ult]); w0 = np.array([x[3] for x in ult]); a = np.array([x[6] for x in ult]); pr0 = np.array([x[4] for x in ult])
    bil = a / 3.0; esp = bil / DEN * comb(50, 20)
    print("2) DADOS DA CAIXA (últimos 300 concursos): se todos apostassem uniformemente, 20 e 0 teriam o mesmo nº esperado de ganhadores")
    print(f"   bilhetes médios por concurso ≈ {bil.mean():,.0f}  | esperado de ganhadores de cada tipo ≈ {esp.mean():.3f} por concurso")
    print(f"   observado: 20 acertos {w20.mean():.3f}  | 0 acertos {np.nanmean(w0):.3f}  | razão 0/20 = {np.nanmean(w0)/w20.mean():.2f}")
    print(f"   concursos com ao menos 1 ganhador de 0 acertos: {100*np.mean(w0>0):.1f}%  | de 20 acertos: {100*np.mean(w20>0):.1f}%")
    pg0 = pr0[w0 > 0]; print(f"   prêmio médio por ganhador de 0 acertos: R$ {np.nanmean(pg0):,.0f} (mediana R$ {np.nanmedian(pg0):,.0f})")
    todos = [x for x in rows if x[3] == x[3]]; W0 = sum(x[3] for x in todos); W20 = sum(x[2] for x in todos)
    print(f"   histórico todo: ganhadores de 0 = {W0:.0f} | de 20 = {W20:.0f}")
    # valor esperado por bilhete
    p = comb(50, 20) / DEN; ev0 = p * np.nanmean(pg0) * 1.0
    print(f"\n3) VALOR: 0 acertos rende ≈ R$ {ev0:.4f} por bilhete por concurso (P=1/11,37mi × R$ {np.nanmean(pg0):,.0f}). Com 24 jogos: R$ {24*ev0:.3f} sobre R$ 72 gastos.")
    print(f"   O jackpot de 20 acertos a R$ 14 mi: R$ {p*14e6:.3f} por bilhete (se único ganhador).")
    # popularidade do prêmio de zero: o que a estrutura do sorteio prevê?
    from sklearn.linear_model import Ridge
    def feats(d):
        a = np.array(d); return [(a <= 31).sum(), (a % 5 == 0).sum(), (a % 10 == 0).sum(), a.sum(), (a % 2 == 0).sum(), (a >= 80).sum(), (np.diff(a) == 1).sum(), (a <= 9).sum(), len(set(a // 10))]
    use = [x for x in rows if x[0] >= 1500 and x[3] == x[3] and x[6] == x[6]]
    X = np.array([feats(sorted(x[1])) for x in use], float); y = np.log((np.array([x[3] for x in use]) + 1) / np.array([x[6] for x in use]) * 1e6)
    cut = int(len(use) * .75); m = Ridge(1.0).fit(X[:cut], y[:cut]); pr = m.predict(X[cut:])
    print(f"\n4) A estrutura do sorteio prevê QUANTOS ganhadores de 0 acertos haverá? (fora da amostra, n={len(use)-cut}): correlação {np.corrcoef(pr, y[cut:])[0,1]:+.3f}")
    print("   coeficientes (dezenas ≤31, múlt. 5, múlt. 10, soma, pares, ≥80, consecutivos, ≤9, décadas):", np.round(m.coef_, 3))
