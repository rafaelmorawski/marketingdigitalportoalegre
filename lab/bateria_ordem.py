# -*- coding: utf-8 -*-
"""Bateria pré-registrada (relatorios/PREREG_ordem_das_bolas.md): 15 testes sobre a ordem de saída e a dinâmica temporal."""
import csv, zlib, sys
import numpy as np
from scipy.stats import spearmanr

S = int(sys.argv[1]) if len(sys.argv) > 1 else 1000

def carregar(f="data/historico_ordem.csv"):
    return np.array([[int(x) for x in r[2:22]] for r in list(csv.reader(open(f)))[1:]])

def runs_z(b):
    """z de Wald-Wolfowitz por linha de matriz binária (colunas = sequência)."""
    n1 = b.sum(1); n0 = b.shape[1] - n1; n = b.shape[1]
    r = 1 + (b[:, 1:] != b[:, :-1]).sum(1)
    mu = 2 * n1 * n0 / n + 1; var = (mu - 1) * (mu - 2) / (n - 1)
    return (r - mu) / np.sqrt(var)

def fisher_g(x):
    x = x - x.mean(); p = np.abs(np.fft.rfft(x))[1:-1] ** 2
    return p.max() / p.sum()

def estat(O):
    n = len(O); out = {}; idx = np.arange(100)
    D = np.zeros((n, 100), np.int8); np.put_along_axis(D, O, 1, axis=1)
    m = O.mean(0); out["1 posição×valor"] = (((m - 49.5) / (28.866 * np.sqrt((100 - 20) / 99) / np.sqrt(n))) ** 2).sum()
    for k, nm in ((0, "2 primeira bola"), (19, "3 última bola")):
        c = np.bincount(O[:, k], minlength=100); out[nm] = ((c - n / 100) ** 2 / (n / 100)).sum()
    a, b = O[:, :-1].ravel(), O[:, 1:].ravel(); out["4 spearman consecutivas"] = spearmanr(a, b)[0]
    out["5 runs paridade na ordem"] = np.nanmean(runs_z((O % 2).astype(int)))
    out["6 consecutivas mesma década"] = ((O[:, :-1] // 10) == (O[:, 1:] // 10)).mean()
    pos = np.full((n, 100), np.nan); np.put_along_axis(pos, O, np.arange(1, 21)[None, :].repeat(n, 0).astype(float), axis=1)
    cnt = (~np.isnan(pos)).sum(0); mp = np.nanmean(pos, 0)
    out["7 posição média por dezena"] = (((mp - 10.5) / (np.sqrt((400 - 1) / 12) / np.sqrt(cnt))) ** 2).sum()
    def tab(x, y):
        T = np.zeros((10, 10)); np.add.at(T, (x // 10, y // 10), 1); e = T.sum(1, keepdims=True) * T.sum(0, keepdims=True) / T.sum()
        return ((T - e) ** 2 / e).sum()
    out["8 primeira(t)×primeira(t−1)"] = tab(O[1:, 0], O[:-1, 0])
    out["9 primeira(t)×última(t−1)"] = tab(O[1:, 0], O[:-1, 19])
    rep = D[1:] & D[:-1]; pr = np.where(rep == 1, pos[1:], np.nan); out["10 posição das repetidas"] = np.nanmean(pr)
    z = runs_z(D.T.astype(int)); from scipy.stats import norm, kstest
    out["11 runs por dezena (KS)"] = kstest(2 * norm.sf(np.abs(z)), "uniform").statistic
    out["12 periodograma 00-49"] = fisher_g(D[:, :50].sum(1).astype(float))
    out["13 periodograma soma"] = fisher_g((D * idx).sum(1).astype(float))
    out["14 compressibilidade"] = len(zlib.compress(np.sort(O, axis=1).astype(np.uint8).tobytes(), 9))
    C = D[:-1].T.astype(float) @ D[1:].astype(float); e = np.outer(D[:-1].sum(0), D[1:].sum(0)) / (n - 1)
    out["15 informação mútua t→t+1"] = ((C - e) ** 2 / e).sum()
    return out

def sintetico(n, rng):
    return np.argsort(rng.random((n, 100)), axis=1)[:, :20]

if __name__ == "__main__":
    O = carregar(); n = len(O); real = estat(O); rng = np.random.default_rng(20261017)
    nul = {k: [] for k in real}
    for _ in range(S):
        for k, v in estat(sintetico(n, rng)).items(): nul[k].append(v)
    lim = 0.05 / len(real)
    print(f"{n} sorteios com ordem | {S} sintéticos | {len(real)} testes | limiar p < {lim:.4f}\n")
    print(f"{'teste':32s} {'real':>12s} {'média nulo':>12s} {'p empírico':>10s}")
    for k in real:
        v = np.array(nul[k]); mu = v.mean(); p = (1 + (np.abs(v - mu) >= abs(real[k] - mu)).sum()) / (S + 1)
        print(f"{k:32s} {real[k]:12.4f} {mu:12.4f} {p:10.4f}{'   <-- PASSA' if p < lim else ''}")
