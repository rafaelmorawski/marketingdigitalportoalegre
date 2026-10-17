# -*- coding: utf-8 -*-
"""Risco e orçamento (perguntas 73, 77, 78, 79). Aproximação: N bilhetes por concurso, independentes (ignora a correlação entre jogos).
Prêmios por ganhador = médias dos últimos 300 concursos (CLAUDE.md seção 3); o jackpot (20 acertos) é parâmetro, supondo ganhador único.
  python3 lab/risco.py --jogos 24 --jackpot 14 --concursos 52"""
import argparse
import numpy as np
from math import comb, log
DEN = comb(100, 20)
PREMIO = {15: 10.0, 16: 44.0, 17: 263.0, 18: 2445.0, 19: 77491.0, 0: 130728.0}

def p_k(k): return comb(50, k) * comb(50, 20 - k) / DEN

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--jogos", type=int, default=24); ap.add_argument("--jackpot", type=float, default=14.0)
    ap.add_argument("--concursos", type=int, default=52); ap.add_argument("--sim", type=int, default=100_000)
    a = ap.parse_args(); N = a.jogos; custo = 3.0 * N
    premios = dict(PREMIO); premios[20] = a.jackpot * 1e6
    ks = [0, 15, 16, 17, 18, 19, 20]; ps = np.array([p_k(k) for k in ks]); pr = np.array([premios[k] for k in ks])
    ev = float((ps * pr).sum()); var = float((ps * pr ** 2).sum() - ev ** 2)
    print(f"{N} jogos, custo R$ {custo:,.0f}/concurso, jackpot R$ {a.jackpot:.0f} mi (ganhador único)")
    print(f"retorno esperado por bilhete R$ {ev:.2f} ({100*ev/3:.0f}% do preço) | por concurso R$ {N*ev:,.2f} (perda esperada R$ {custo-N*ev:,.2f})")
    print(f"P(algum prêmio em um concurso) ≈ {100*(1-(1-ps.sum())**N):.1f}% | P(15+ em um concurso) ≈ {100*(1-(1-ps[1:].sum())**N):.1f}%")
    print("\nTempo até ter 50% de chance de ver pelo menos um (supondo concursos independentes e jogos independentes):")
    for nome, p in (("15 acertos ou mais", ps[1:].sum()), ("19 ou mais", ps[5:].sum()), ("20 acertos", p_k(20)), ("20 ou 0 acertos", 2 * p_k(20))):
        c = log(0.5) / log(1 - min(1, N * p)); print(f"  {nome:20s} {c:>14,.0f} concursos (≈ {c/156:,.1f} anos a 3 concursos por semana)")
    rng = np.random.default_rng(1); C = a.concursos
    cont = rng.multinomial(N, np.r_[1 - ps.sum(), ps], size=(a.sim, C))[:, :, 1:]
    ganho = (cont * pr).sum((1, 2)); liq = ganho - custo * C
    print(f"\nSimulação: {C} concursos seguidos ({a.sim:,} trajetórias), gasto total R$ {custo*C:,.0f}")
    for q in (5, 25, 50, 75, 95): print(f"  percentil {q:2d} do resultado líquido: R$ {np.percentile(liq, q):>12,.0f}")
    print(f"  média R$ {liq.mean():,.0f} | P(terminar no lucro) = {100*(liq > 0).mean():.2f}% | P(perder mais de 90% do gasto) = {100*(liq < -0.9*custo*C).mean():.1f}%")
    print("  Observação: a média inclui o jackpot, que quase nunca ocorre; a mediana mostra o que de fato acontece.")
