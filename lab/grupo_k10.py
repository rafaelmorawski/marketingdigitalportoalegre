# -*- coding: utf-8 -*-
"""Grupo K de 10 jogos: hill-climbing de cobertura com 3 bancos separados (construção / seleção / teste).
Restrições opcionais do Rafael (repetidas do último sorteio e pendentes do ciclo) entram como restrição dura,
para medir o seu custo. Nada aqui prevê o sorteio: mede cobertura em sorteios uniformes simulados."""
import json, sys, time
import numpy as np
from ferramentas import sorteios_simulados, valido

PESO_P15 = 4.0

def avaliar(D, jogos):
    V = np.zeros((100, len(jogos)), np.float32)
    for j, g in enumerate(jogos): V[list(g), j] = 1
    mx = (D @ V).max(1)
    return mx.mean(), (mx >= 15).mean(), (mx >= 17).mean()

def construir(rest, pend, seed, tentativas, n=150_000):
    rng = np.random.default_rng(seed)
    DT = np.ascontiguousarray(sorteios_simulados(n, seed + 1000).T.astype(np.int8))   # 100 x n
    jogos = []
    for _ in range(10):
        while True:
            g = set(rng.choice(100, 50, replace=False).tolist())
            if valido(g) and ok(g, rest, pend): break
        jogos.append(g)
    H = np.stack([DT[sorted(g)].sum(0, dtype=np.int16) for g in jogos]).astype(np.int8)   # 10 x n
    def obj(H): m = H.max(0); return m.mean() + PESO_P15 * (m >= 15).mean()
    atual = obj(H)
    for t in range(tentativas):
        j = int(rng.integers(10)); g = jogos[j]
        sai = int(rng.choice(sorted(g))); entra = int(rng.choice(sorted(set(range(100)) - g)))
        novo = (g - {sai}) | {entra}
        if not valido(novo) or not ok(novo, rest, pend): continue
        if any(len(novo & o) > 40 for k, o in enumerate(jogos) if k != j): continue
        h = H[j] - DT[sai] + DT[entra]
        old = H[j].copy(); H[j] = h
        v = obj(H)
        if v > atual: atual, jogos[j] = v, novo
        else: H[j] = old
    return [sorted(g) for g in jogos]

def ok(g, rest, pend):
    if not rest: return True
    rep, pe = rest
    return len(g & rep) >= 4 and len(g & pend) >= 4

if __name__ == "__main__":
    pass
