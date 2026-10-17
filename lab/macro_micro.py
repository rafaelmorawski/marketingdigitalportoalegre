# -*- coding: utf-8 -*-
"""Bateria pré-registrada macro×micro (relatorios/PREREG_macro_micro.md)."""
import sys
import numpy as np
from scipy.stats import chi2
from dados import carregar_historico

S = int(sys.argv[1]) if len(sys.argv) > 1 else 300
rng0 = np.random.default_rng(20261017)

def temp_chi(M, W, rng):
    N = len(M); C = np.vstack([np.zeros((1, 100)), np.cumsum(M, 0)])
    hit = np.zeros(3); tot = np.zeros(3)
    jit = rng.random((N, 100))
    for t in range(W, N):
        cnt = C[t] - C[t - W]
        rank = np.lexsort((jit[t], cnt)).argsort()          # 0 = mais fria ... 99 = mais quente (desempate aleatório)
        est = np.minimum(rank * 3 // 100, 2)
        for s in range(3): hit[s] += M[t][est == s].sum(); tot[s] += (est == s).sum()
    p = hit.sum() / tot.sum()
    return (((hit - tot * p) ** 2) / (tot * p * (1 - p))).sum(), hit / tot

def persist(M, b):
    nb = len(M) // b; B = M[:nb * b].reshape(nb, b, 100).sum(1).astype(float); B = B - B.mean(0)
    return (B[:-1] * B[1:]).sum() / (B ** 2).sum()

def overdisp(M, b):
    nb = len(M) // b; B = M[:nb * b].reshape(nb, b, 100).sum(1).astype(float)
    return (((B - 0.2 * b) ** 2) / (b * 0.16)).sum(1).mean() / 100

def ciclo_chi(M):
    N = len(M); vis = np.zeros(100, bool); pen = np.ones(100, bool)
    hit = np.zeros(4); tot = np.zeros(4)
    for t in range(N):
        m = int(pen.sum())
        if t > 0 and 0 < m < 100:
            s = 0 if m <= 3 else 1 if m <= 6 else 2 if m <= 10 else 3
            hit[s] += M[t][pen].sum(); tot[s] += m
        pen &= ~M[t].astype(bool)
        if not pen.any(): pen[:] = True
    return (((hit - 0.2 * tot) ** 2) / (tot * 0.16)).sum(), hit / tot

def estat(M, rng, completo=True):
    o = {}
    for W in (5, 10, 20, 50, 100): o[f"T W={W}"] = temp_chi(M, W, rng)[0]
    for b in (5, 10, 20, 50, 100): o[f"P b={b}"] = persist(M, b)
    for b in (20, 50): o[f"O b={b}"] = overdisp(M, b)
    o["C ciclo por fase"] = ciclo_chi(M)[0]
    return o

def sint(N, rng):
    M = np.zeros((N, 100), np.int8); ix = np.argsort(rng.random((N, 100)), 1)[:, :20]; np.put_along_axis(M, ix, 1, 1); return M

if __name__ == "__main__":
    M = carregar_historico()["D"].astype(np.int8); N = len(M)
    real = estat(M, np.random.default_rng(1)); nul = {k: [] for k in real}
    for i in range(S):
        for k, v in estat(sint(N, rng0), rng0).items(): nul[k].append(v)
    lim = 0.05 / len(real)
    print(f"{N} sorteios | {S} sintéticos | {len(real)} testes | limiar p < {lim:.4f}\n")
    print(f"{'teste':20s} {'real':>10s} {'média nulo':>11s} {'p emp.':>8s}")
    for k in real:
        v = np.array(nul[k]); mu = v.mean(); p = (1 + (np.abs(v - mu) >= abs(real[k] - mu)).sum()) / (S + 1)
        print(f"{k:20s} {real[k]:10.4f} {mu:11.4f} {p:8.4f}{'   <-- PASSA' if p < lim else ''}")
    print("\ntaxas de saída por estado (frio, morno, quente):")
    for W in (5, 10, 20, 50, 100): print(f"  W={W:3d}", np.round(temp_chi(M, W, np.random.default_rng(1))[1], 4))
    print("ciclo, taxa por fase (1–3, 4–6, 7–10, 11+ pendentes):", np.round(ciclo_chi(M)[1], 4))
