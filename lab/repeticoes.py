# -*- coding: utf-8 -*-
"""'Nunca se repetiram as mesmas 20 dezenas': é esperado? E os quase-repetidos (12+ dezenas em comum) ocorrem no ritmo do acaso?"""
import os, sys
import numpy as np
from math import comb
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(RAIZ, "lab"))
from dados import carregar_historico
from scipy.stats import poisson

D = carregar_historico()["D"].astype(np.float32); N = len(D); DEN = comb(100, 20)
O = D @ D.T; iu = np.triu_indices(N, 1); ov = O[iu].astype(int); pares = len(ov)
print(f"{N} sorteios, {pares:,} pares. Sorteios possíveis: {DEN:.3e}")
print(f"P(algum par idêntico) ≈ pares/C(100,20) = {pares/DEN:.2e}  -> não haver repetição é o ESPERADO (esperaríamos {pares/DEN:.1e} repetições)\n")
print(f"{'dezenas em comum ≥':20s} {'pares observados':>17s} {'esperados':>11s} {'p (Poisson)':>12s}")
for k in (10, 12, 13, 14, 15, 16, 17):
    t = sum(comb(20, h) * comb(80, 20 - h) for h in range(k, 21)) / DEN; e = pares * t; o = int((ov >= k).sum())
    p = 2 * min(poisson.sf(o - 1, e), poisson.cdf(o, e)); print(f"{k:20d} {o:17d} {e:11.1f} {min(p,1):12.3f}")
print(f"\nmaior sobreposição entre quaisquer dois sorteios do histórico: {ov.max()} dezenas")
print(f"efeito de 'excluir' os {N} sorteios passados: a chance do próximo ser um deles é {N/DEN:.1e}; o espaço restante é {1-N/DEN:.15f} do total (nenhuma cobertura ganha com isso)")
