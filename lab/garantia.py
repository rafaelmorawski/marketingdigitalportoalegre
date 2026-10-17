# -*- coding: utf-8 -*-
"""Pergunta 54: qual o mínimo de acertos GARANTIDO do melhor jogo, para qualquer sorteio possível?
Adversário exato (MILP): escolhe 20 dezenas que minimizam o máximo de acertos entre os jogos. + limites de contagem (nº mínimo de jogos para garantir k+)."""
import json, os, sys
import numpy as np
from math import comb
from scipy.optimize import milp, LinearConstraint, Bounds
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def pior_sorteio(jogos, limite=60):
    n = len(jogos); c = np.r_[np.zeros(100), 1.0]
    A = np.zeros((n, 101)); 
    for j, g in enumerate(jogos): A[j, list(g)] = 1; A[j, 100] = -1
    cons = [LinearConstraint(A, -np.inf, 0), LinearConstraint(np.r_[np.ones(100), 0].reshape(1, -1), 20, 20)]
    r = milp(c, constraints=cons, integrality=np.r_[np.ones(100), 0], bounds=Bounds(np.r_[np.zeros(100), 0], np.r_[np.ones(100), 20]), options={"time_limit": limite})
    x = np.round(r.x[:100]).astype(int); return int(round(r.fun)), [int(i) for i in np.flatnonzero(x)], r.status

if __name__ == "__main__":
    J = [g["dezenas"] for gr in json.load(open(os.path.join(RAIZ, "data", "jogos_C2988.json")))["grupos"] if gr["id"] == "J" for g in gr["jogos"]]
    TODOS = [g["dezenas"] for gr in json.load(open(os.path.join(RAIZ, "data", "jogos_C2988.json")))["grupos"] for g in gr["jogos"]]
    K = list(json.load(open(os.path.join(RAIZ, "data", "jogos_C2989_K10.json")))["jogos"].values())
    R = list(json.load(open(os.path.join(RAIZ, "data", "jogos_C2989_R10.json")))["jogos"].values())
    rng = np.random.default_rng(1); rand = [[sorted(rng.choice(100, 50, replace=False).tolist()) for _ in range(10)] for _ in range(3)]
    comp = [sorted(set(range(100)) - set(K[0]))]
    print(f"{'grupo':44s} pior sorteio possível: melhor jogo ≥")
    for nome, G in [("J espiral (10)", J), ("K10", K), ("R10", R), ("24 jogos do C2988", TODOS), ("aleatório #1 (10)", rand[0]), ("aleatório #2 (10)", rand[1]),
                    ("K10 + complemento de K1 (11 jogos)", K + comp), ("K1 + complemento (2 jogos)", [K[0]] + comp)]:
        v, d, st = pior_sorteio(G); print(f"{nome:44s} {v}   (status {st})")
    # limites de contagem: cada jogo 'cobre' no máximo P(>=k) dos sorteios; garantir k+ exige N >= 1/P(>=k)
    DEN = comb(100, 20); print("\nLIMITE MÍNIMO de nº de jogos para GARANTIR k+ acertos em qualquer sorteio (contagem; na prática precisa de bem mais):")
    for k in (11, 12, 13, 14, 15, 16, 17, 18, 19, 20):
        p = sum(comb(50, h) * comb(50, 20 - h) for h in range(k, 21)) / DEN; N = int(np.ceil(1 / p))
        print(f"  garantir {k:2d}+: N ≥ {N:>10,}   (custo ≥ R$ {3*N:>14,.0f})")
