# -*- coding: utf-8 -*-
"""Ferramentas do laboratório: simulação uniforme, avaliação de grades, chances exatas, auditoria."""
import random
from itertools import combinations
from math import comb

import numpy as np

DEN = comb(100, 20)
P20 = comb(50, 20) / DEN                                   # 1 em 11.372.636 por bilhete
P19MAIS = (comb(50, 19) * 50 + comb(50, 20)) / DEN         # 1 em 341.951 por bilhete


def valido(jogo):
    """Convenção interna: 50 dezenas distintas entre 00 e 99 e pelo menos 2 por década (não é regra da Caixa)."""
    s = set(jogo)
    if len(s) != 50 or min(s) < 0 or max(s) > 99:
        return False
    return all(len([x for x in s if x // 10 == k]) >= 2 for k in range(10))


def sorteios_simulados(n, seed):
    """n sorteios uniformes de 20 dezenas, em matriz n x 100 (float32)."""
    ix = np.argpartition(np.random.default_rng(seed).random((n, 100)), 19, axis=1)[:, :20]
    Z = np.zeros((n, 100), dtype=np.float32)
    np.put_along_axis(Z, ix, 1, axis=1)
    return Z


def matriz(jogos):
    V = np.zeros((100, len(jogos)), dtype=np.float32)
    for j, g in enumerate(jogos):
        V[list(g), j] = 1
    return V


def avaliar_grade(jogos, n=600_000, seed=1, bloco=50_000):
    """E[max], P(>=14/15/16/17) e P(melhor <=12) da grade em n sorteios simulados."""
    V = matriz(jogos)
    acc = np.zeros(6)
    feitos = 0
    for b in range(n // bloco):
        m = np.rint(sorteios_simulados(bloco, seed * 1000 + b) @ V).max(1)
        acc += [m.sum(), (m >= 14).sum(), (m >= 15).sum(), (m >= 16).sum(), (m >= 17).sum(), (m <= 12).sum()]
        feitos += bloco
    a = acc / feitos
    return {"E_max": a[0], "P14": a[1], "P15": a[2], "P16": a[3], "P17": a[4], "melhor_ate_12": a[5]}


def aleatorios(k, seed=7):
    rs = random.Random(seed)
    saida = []
    while len(saida) < k:
        s = frozenset(rs.sample(range(100), 50))
        if valido(s):
            saida.append(sorted(s))
    return saida


def comparar_com_aleatorios(jogos, n_grades=20, n=300_000, seed=3):
    """Controle obrigatório: compara a grade com n_grades grades aleatórias de mesmo tamanho (faixa, não só a média)."""
    ref = avaliar_grade(jogos, n=n, seed=seed)
    ctrl = [avaliar_grade(aleatorios(len(jogos), seed=100 + i), n=n, seed=seed) for i in range(n_grades)]
    p15 = np.array([c["P15"] for c in ctrl])
    return {"grade": ref, "aleatorias_media": {k: float(np.mean([c[k] for c in ctrl])) for k in ref},
            "P15_aleatorias_faixa": (float(p15.min()), float(p15.max()))}


def _par19(m):
    tot = 0
    for x in range(21):
        for a in range(21 - x):
            for b in range(21 - x - a):
                c = 20 - x - a - b
                if x + a >= 19 and x + b >= 19:
                    tot += comb(m, x) * comb(50 - m, a) * comb(50 - m, b) * comb(m, c)
    return tot / DEN


def chances_exatas(jogos):
    """Chance por sorteio de algum jogo fazer 20 e de algum fazer 19+ (soma menos colisões de 2ª ordem)."""
    ov = [len(set(a) & set(b)) for a, b in combinations(jogos, 2)]
    n = len(jogos)
    s20 = sum(comb(m, 20) / DEN for m in ov if m >= 20)
    s19 = sum(_par19(m) for m in ov)
    p20, p19 = n * P20 - s20, n * P19MAIS - s19
    return {"1_em_20": 1 / p20, "1_em_19mais": 1 / p19, "teto_20": 1 / (n * P20), "teto_19mais": 1 / (n * P19MAIS)}


def auditoria(jogos, nomes=None):
    nomes = nomes or [f"j{i + 1}" for i in range(len(jogos))]
    ov = [(len(set(a) & set(b)), nomes[i], nomes[j]) for (i, a), (j, b) in combinations(list(enumerate(jogos)), 2)]
    v = [o[0] for o in ov]
    cov = np.zeros(100)
    for g in jogos:
        cov[list(g)] += 1
    return {"jogos": len(jogos), "distintos": len({tuple(sorted(g)) for g in jogos}) == len(jogos),
            "validos": all(valido(g) for g in jogos), "uniao": int((cov > 0).sum()),
            "sobreposicao_min": min(v), "sobreposicao_max": max(v), "sobreposicao_media": float(np.mean(v)),
            "pares_acima_de_30": [(o[1], o[2], o[0]) for o in ov if o[0] > 30],
            "cobertura_min": int(cov.min()), "cobertura_max": int(cov.max())}
