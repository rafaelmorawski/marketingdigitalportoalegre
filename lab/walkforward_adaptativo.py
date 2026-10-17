# -*- coding: utf-8 -*-
"""Teste walk-forward da hipótese 'saber quando e onde': a cada sorteio t, monta 10 jogos (espiral de núcleo + apoio por
sinais: pendente do ciclo=3, repetida do último=2, atrasada=1) usando SÓ sorteios < t, e mede acertos em t.
Pré-registro: H0 = média de acertos por jogo 10,00 e E[max] de 10 jogos aleatórios = 13,064 (40 grades, ver grupo_k10)."""
import numpy as np
from dados import carregar_historico

def estado(H, t):
    ult = H[t - 1]
    vis = np.zeros(100, bool); ini = 0
    for s in range(t - 1, -1, -1):
        vis |= H[s].astype(bool)
        if vis.all(): ini = s + 1; break
    pen = np.ones(100, bool)
    for s in range(ini, t): pen &= ~H[s].astype(bool)
    gap = np.array([t - (np.flatnonzero(H[:t, d])[-1] + 1) if H[:t, d].any() else t for d in range(100)])
    atr = np.zeros(100, bool); atr[np.argsort(-gap)[:20]] = True
    return ult.astype(bool), pen, atr

def grupo(ult, pen, atr):
    score = 3 * pen + 2 * ult + 1 * atr
    # núcleo base: em cada década, o par vizinho com maior soma de score (circular dentro da década)
    base = []
    for dec in range(10):
        pares = [(score[dec*10+i] + score[dec*10+(i+1) % 10], i) for i in range(10)]
        base.append(max(pares)[1])
    jogos, nucleo_ant = [], set()
    for k in range(10):
        n = set()
        for dec in range(10):
            i = (base[dec] + 2 * (k % 5)) % 10
            n |= {dec*10 + i, dec*10 + (i + 1) % 10}
        livres = [d for d in np.argsort(-score, kind="stable") if d not in n and d not in nucleo_ant]
        jogos.append(sorted(n | set(int(x) for x in livres[:30]))); nucleo_ant = n
    return jogos

def main():
    M = carregar_historico()["D"]
    T = range(1000, len(M))
    mx, md = [], []
    for t in T:
        g = grupo(*estado(M, t))
        h = [int(M[t, x].sum()) for x in g]
        mx.append(max(h)); md.append(np.mean(h))
    mx, md = np.array(mx), np.array(md); n = len(mx)
    print(f"sorteios testados: {n} (C{T[0]+1} a C{T[-1]+1})")
    print(f"média de acertos por jogo: {md.mean():.3f} (H0 10,000) z={(md.mean()-10)/(md.std(ddof=1)/np.sqrt(n)):+.2f}")
    print(f"E[max] do grupo adaptativo: {mx.mean():.3f} (H0 13,064) z={(mx.mean()-13.064)/(mx.std(ddof=1)/np.sqrt(n)):+.2f}")
    print(f"P(max>=15): {100*(mx>=15).mean():.2f}% (H0 10,87%) | maior max: {mx.max()} | vezes >=17: {(mx>=17).sum()} (esperado ~{0.0040*n:.1f})")

if __name__ == "__main__":
    main()
