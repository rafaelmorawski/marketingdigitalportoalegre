# -*- coding: utf-8 -*-
"""Pergunta 10/86: qual a menor distorção que nossos detectores pegam, e quanto valeria uma distorção invisível?
Gera S históricos sintéticos de N=2.988 sorteios com viés injetado (amostragem de 20 sem reposição por Gumbel top-k com pesos).
  A) 10 dezenas 'quentes' fixas (peso r)      -> detector: χ² de frequências; detector genérico: top-50 por frequência (janela 300)
  B) repetição: dezenas do sorteio anterior com peso 1+a -> detector: taxa de repetição
  C) vizinhança vertical (±10) com peso 1+a·nº de vizinhas sorteadas antes -> detector: taxa com vizinha
Poder = fração de históricos com p < 0,05 (e < 0,0033). Valor = ganho em acertos de um bilhete 'oráculo' que conhece o viés."""
import numpy as np
from scipy.stats import chi2, norm

N, S = 2988, 200
rng = np.random.default_rng(20261017)

def gerar(peso_fn):
    M = np.zeros((S, N, 100), np.int8); prev = np.zeros((S, 100), np.int8)
    for t in range(N):
        w = peso_fn(prev)
        key = np.log(w) + rng.gumbel(size=(S, 100))
        ix = np.argpartition(-key, 20, axis=1)[:, :20]
        cur = np.zeros((S, 100), np.int8); np.put_along_axis(cur, ix, 1, 1); M[:, t] = cur; prev = cur
    return M

def viz_v(prev):
    v = np.zeros_like(prev, dtype=np.int16); v[:, 10:] += prev[:, :-10]; v[:, :-10] += prev[:, 10:]; return v

def p2(z): return 2 * norm.sf(np.abs(z))

def detectores(M):
    out = {}
    c = M.sum(1).astype(float); out["freq χ²"] = chi2.sf(((c - 0.2 * N) ** 2 / (N * 0.16)).sum(1), 99)
    cs = np.cumsum(M, 1, dtype=np.int16); hits = []
    for t in range(300, N):
        cnt = cs[:, t - 1] - cs[:, t - 301]; top = np.argpartition(-(cnt + rng.random((S, 100)) * 1e-3), 50, axis=1)[:, :50]
        hits.append(np.take_along_axis(M[:, t], top, 1).sum(1))
    hm = np.mean(hits, 0); out["top-50 freq300"] = p2((hm - 10) / (2.01 / np.sqrt(N - 300)))
    rep = (M[:, 1:] & M[:, :-1]).sum((1, 2)); n = 20.0 * (N - 1); out["repetição"] = p2((rep / n - 0.2) / np.sqrt(0.16 / n))
    nb = np.stack([viz_v(M[:, t - 1]) for t in range(1, N)], 1); msk = nb >= 1
    h = (M[:, 1:] * msk).sum((1, 2)); nn = msk.sum((1, 2)); out["vizinha coluna"] = p2((h / nn - 0.2) / np.sqrt(0.16 / nn))
    return out, nb

def oraculo(M, tipo, hot=None, nb=None):
    g = []
    for t in range(1, N):
        if tipo == "A": score = np.zeros((S, 100)); score[:, hot] = 1
        elif tipo == "B": score = M[:, t - 1].astype(float)
        else: score = nb[:, t - 1].astype(float)
        top = np.argpartition(-(score + rng.random((S, 100)) * 1e-3), 50, axis=1)[:, :50]
        g.append(np.take_along_axis(M[:, t], top, 1).sum(1))
    return np.mean(g) - 10

def linha(nome, det, M, tipo, extra, **kw):
    pv = det[extra]; gan = oraculo(M, tipo, **kw)
    print(f"{nome:34s} {extra:16s} poder@0,05={100*(pv<0.05).mean():5.1f}%  poder@0,0033={100*(pv<0.0033).mean():5.1f}%  | ganho do bilhete-oráculo {gan:+.3f} acertos")

if __name__ == "__main__":
    M0 = gerar(lambda p: np.ones((S, 100))); d0, _ = detectores(M0)
    print("CONTROLE (sem viés): taxa de falsos positivos a p<0,05:", {k: f"{100*(v<0.05).mean():.1f}%" for k, v in d0.items()}, "\n")
    hot = np.arange(10)
    for r in (1.03, 1.06, 1.12, 1.25):
        M = gerar(lambda p, r=r: np.where(np.arange(100) < 10, r, 1.0)[None, :].repeat(S, 0)); d, nb = detectores(M)
        dlt = 100 * (M[:, :, :10].mean() - 0.2)
        for det in ("freq χ²", "top-50 freq300"): linha(f"A) 10 dezenas fixas, δ={dlt:+.2f} pp", d, M, "A", det, hot=hot)
    for a in (0.03, 0.06, 0.12, 0.25):
        M = gerar(lambda p, a=a: 1 + a * p); d, nb = detectores(M)
        dlt = 100 * ((M[:, 1:] * M[:, :-1]).sum() / (M[:, :-1].sum()) - 0.2)
        linha(f"B) repetição, δ={dlt:+.2f} pp", d, M, "B", "repetição")
    for a in (0.03, 0.06, 0.12, 0.25):
        M = gerar(lambda p, a=a: 1 + a * viz_v(p)); d, nb = detectores(M)
        dlt = 100 * ((M[:, 1:] * (nb >= 1)).sum() / (nb >= 1).sum() - 0.2)
        linha(f"C) vizinha na coluna, δ={dlt:+.2f} pp", d, M, "C", "vizinha coluna", nb=nb)
