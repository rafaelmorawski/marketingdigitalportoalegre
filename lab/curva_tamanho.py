# -*- coding: utf-8 -*-
"""Quanto cada jogo a mais acrescenta? Grades otimizadas de N jogos (N = 1..40) vs aleatórias de mesmo tamanho, no mesmo banco de teste."""
import os, sys
import numpy as np
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(RAIZ, "lab"))
from construtor import construir, metricas
from ferramentas import sorteios_simulados, valido
from zero_acertos import p_uniao

DT = np.ascontiguousarray(sorteios_simulados(60_000, 1).T.astype(np.int8)); Dsel = sorteios_simulados(200_000, 555); Dte = sorteios_simulados(500_000, 777)
rng = np.random.default_rng(7); linhas = []
print(f"{'N':>3s} {'custo':>6s} {'E[max] otim.':>13s} {'E[max] aleat.':>14s} {'P(>=15) otim.':>14s} {'P(>=15) aleat.':>15s} {'ganho P15 por jogo extra':>26s} {'chance 20 ou 0':>16s}")
ant = 0
for N in (1, 2, 3, 5, 8, 10, 15, 20, 24, 30, 40):
    c = [construir([], N, DT, 50 + s, min(1500 * N, 40_000), "emax") for s in range(2)]
    g = max(c, key=lambda J: (lambda a: a[0] + 4 * a[1])(metricas(Dsel, J))); m = metricas(Dte, g)
    ct = []
    while len(ct) < 15:
        r = [sorted(rng.choice(100, 50, replace=False).tolist()) for _ in range(N)]
        if all(valido(x) for x in r): ct.append(metricas(Dte, r))
    C = np.array(ct).mean(0); S = [set(x) for x in g]; u, _, _ = p_uniao(S + [set(range(100)) - s for s in S])
    print(f"{N:3d} {3*N:6d} {m[0]:13.3f} {C[0]:14.3f} {100*m[1]:13.2f}% {100*C[1]:14.2f}% {100*(m[1]-ant)/max(1,N-(linhas[-1] if linhas else 0)):25.2f}pp 1 em {1/u:>11,.0f}", flush=True)
    ant = m[1]; linhas.append(N)
