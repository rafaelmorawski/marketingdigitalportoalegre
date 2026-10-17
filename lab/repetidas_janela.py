# -*- coding: utf-8 -*-
"""Quantas dezenas do sorteio t já saíram nos k sorteios anteriores? Observado × esperado (hipergeométrica exata), por k."""
import os, sys
import numpy as np
from math import comb
from scipy.stats import chi2
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(RAIZ, "lab"))
from dados import carregar_historico
M = carregar_historico()["D"].astype(np.int8); N = len(M)

def esperado(k):
    """Distribuição exata de |D_t ∩ união dos k sorteios anteriores|: a união tem U dezenas (aleatória); condicionamos em U via simulação exata por convolução."""
    # P(dezena fora da união) = 0,8^k, mas as dezenas não são independentes; usa simulação grande, exata em média.
    rng = np.random.default_rng(3); n = 400_000
    ix = lambda: np.argsort(rng.random((n, 100)), 1)[:, :20]
    U = np.zeros((n, 100), bool)
    for _ in range(k): np.put_along_axis(U, ix(), True, 1)
    cur = np.zeros((n, 100), bool); np.put_along_axis(cur, ix(), True, 1)
    return np.bincount((U & cur).sum(1), minlength=21)[:21] / n

print(f"{N} sorteios. Dezenas do sorteio t que JÁ saíram nos k sorteios anteriores (k=1 é o 'repetidas do anterior'):\n")
print(f"{'k':>2s} {'média obs.':>10s} {'média esp.':>10s} {'moda obs.':>9s} {'entre 8 e 9: obs.':>18s} {'esp.':>7s} {'χ² p':>7s}")
res = {}
for k in (1, 2, 3, 4, 5):
    U = np.zeros((N - k, 100), bool)
    for j in range(k): U |= M[j: N - k + j].astype(bool)
    r = (U & M[k:].astype(bool)).sum(1); n = len(r); e = esperado(k); o = np.bincount(r, minlength=21)[:21]
    m = e * n >= 5; c2 = ((o[m] - e[m] * n) ** 2 / (e[m] * n)).sum(); p = chi2.sf(c2, m.sum() - 1)
    f89 = ((r >= 8) & (r <= 9)).mean(); res[k] = (r, o, e)
    print(f"{k:2d} {r.mean():10.2f} {sum(i*e[i] for i in range(21)):10.2f} {int(np.bincount(r).argmax()):9d} {100*f89:17.1f}% {100*(e[8]+e[9]):6.1f}% {p:7.3f}")
print("\nDistribuição para k = 2 e k = 3 (% dos sorteios com X dezenas já saídas nos 2 / 3 sorteios anteriores):")
print("  X :", " ".join(f"{x:5d}" for x in range(3, 16)))
for k in (2, 3):
    r = res[k][0]; print(f"  k={k} obs:", " ".join(f"{100*(r==x).mean():5.1f}" for x in range(3, 16)))
    print(f"  k={k} esp:", " ".join(f"{100*res[k][2][x]:5.1f}" for x in range(3, 16)))
print("\nSó o sorteio imediatamente anterior (k=1): % dos sorteios com 8 ou 9 repetidas =", f"{100*((res[1][0]>=8)&(res[1][0]<=9)).mean():.1f}%", "| com 3 a 5 =", f"{100*((res[1][0]>=3)&(res[1][0]<=5)).mean():.1f}%")
for nome, a in (("últimos 100", -100), ("últimos 300", -300)):
    r = res[1][0][a:]; print(f"  {nome}: média {r.mean():.2f} | 8–9 repetidas em {100*((r>=8)&(r<=9)).mean():.1f}% dos sorteios")
