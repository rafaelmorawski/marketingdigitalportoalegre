# -*- coding: utf-8 -*-
"""O que o histórico mostra sobre as repetidas de um sorteio para o outro."""
import os, sys
import numpy as np
from math import comb
from scipy.stats import chi2, hypergeom, binomtest, norm
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(RAIZ, "lab"))
from dados import carregar_historico
M = carregar_historico()["D"].astype(np.int8); N = len(M)
rep = (M[1:] & M[:-1]).sum(1); n = len(rep)
print(f"{N} sorteios | repetidas do sorteio anterior: média {rep.mean():.3f} (esperado 4,000), desvio {rep.std():.3f} (esperado {hypergeom(100,20,20).std():.3f})")
obs = np.bincount(rep, minlength=14)[:14]; esp = hypergeom.pmf(np.arange(14), 100, 20, 20) * n
print("\nDistribuição (nº de repetidas): observado × esperado")
for k in range(0, 11): print(f"  {k:2d}: {obs[k]:4d}  {esp[k]:7.1f}   {'#'*int(obs[k]/12)}")
m = esp >= 5; c2 = ((obs[m] - esp[m]) ** 2 / esp[m]).sum(); print(f"  χ² = {c2:.1f} (gl {m.sum()-1}) p = {chi2.sf(c2, m.sum()-1):.3f}")
print(f"  0 repetidas: {100*obs[0]/n:.2f}% (esperado {100*hypergeom.pmf(0,100,20,20):.2f}%) | 8+ repetidas: {100*obs[8:].sum()/n:.2f}% (esperado {100*hypergeom.sf(7,100,20,20):.2f}%)")
print("\nPor lag: taxa de uma dezena sair dado que saiu k sorteios antes (esperado 0,2000)")
for k in (1, 2, 3, 5, 10, 20):
    a = M[k:].astype(float); b = M[:-k].astype(float); h = (a * b).sum(); t = b.sum(); p = binomtest(int(h), int(t), 0.2).pvalue
    print(f"  lag {k:2d}: {h/t:.4f}  p = {p:.3f}")
print("\nSaiu r sorteios seguidos → sai no próximo? (esperado 0,2000)")
for r in (1, 2, 3, 4):
    L = N - r; c = np.ones((L, 100), bool)
    for j in range(r): c &= M[j: j + L].astype(bool)
    nx = M[r:].astype(bool); L2 = min(len(c), len(nx)); h = (c[:L2] & nx[:L2]).sum(); t = c[:L2].sum(); p = binomtest(int(h), int(t), 0.2).pvalue
    print(f"  saiu {r} seguido(s) ({t} casos): próxima taxa {h/t:.4f}  p = {p:.3f}")
print("\nHeterogeneidade por dezena: taxa de repetição de cada dezena (saiu t−1 → saiu t)")
h = (M[1:] & M[:-1]).sum(0); t = M[:-1].sum(0); tx = h / t; z = (tx - 0.2) / np.sqrt(0.16 / t); q = (z ** 2).sum()
print(f"  mín {tx.min():.3f} (dezena {tx.argmin():02d}) | máx {tx.max():.3f} (dezena {tx.argmax():02d}) | χ² de homogeneidade {q:.1f} (gl 100) p = {chi2.sf(q, 100):.3f} | maior |z| {np.abs(z).max():.2f} (limiar Bonferroni 100 testes 3,29)")
print("\nO nº de repetidas de um sorteio prevê o do seguinte? Autocorrelação lags 1–5:", [f"{np.corrcoef(rep[:-l], rep[l:])[0,1]:+.3f}" for l in range(1, 6)], f"(±{2/np.sqrt(n):.3f})")
print("Janelas de 100 sorteios: média de repetidas por janela (esperado 4,00; dp da média 0,16):", np.round([rep[i:i+100].mean() for i in range(0, n - 99, 500)], 2))
print("Últimas repetidas:", rep[-12:].tolist(), "(C2977..C2988)")
print("\nDe onde vêm as repetidas? posição na ordem de saída: ver bateria_ordem teste 10 (média 10,47 vs 10,50, p = 0,51).")
