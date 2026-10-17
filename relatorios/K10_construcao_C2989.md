# Grupo K10 para o C2989 — construção e teste (17/10/2026)

**Hipótese do Rafael:** ciclo e repetidas, aplicados a cada sorteio, capturam o "quando e onde".

## 1. Teste walk-forward no histórico real (`lab/walkforward_adaptativo.py`)
A cada sorteio t (C1001–C2988, 1.988 sorteios) montou-se 10 jogos só com informação anterior a t (espiral de núcleo + apoio por pendente do ciclo=3, repetida=2, atrasada=1).
- Média de acertos por jogo: **10,032** (esperado 10,000; z = +1,21) → sem sinal.
- E[max]: 12,22 contra 13,06 de 10 jogos aleatórios. Concentrar os jogos nos sinais derruba a cobertura (apoios quase iguais entre os jogos).

## 2. Otimização de cobertura (`lab/grupo_k10.py`), 3 bancos separados
Construção 150 mil sorteios simulados (6 reinícios × 40 mil trocas), seleção 400 mil, teste final 800 mil inéditos.

| Grupo | E[max] | P(≥15) | P(≥16) | P(≥17) |
|---|---|---|---|---|
| 40 aleatórios (média) | 13,064 | 10,87% | 2,50% | 0,403% |
| J espiral (fixo) | 13,177 | 11,11% | 2,50% | 0,404% |
| K livre | 13,234 | 11,24% | 2,50% | 0,406% |
| **K com restrições (≥4 repetidas e ≥4 pendentes)** | 13,234 | 11,21% | 2,51% | 0,402% |

Faixa dos aleatórios: E[max] 13,021–13,110; P(≥15) 10,75–11,02%. O ganho de K sobre J (+0,057 em E[max]) é pequeno; as restrições não custam nada, mas também não ganham nada. P(≥16) e P(≥17) não mudam.

## 3. Chance de 20 acertos
10 jogos distintos: 1 em 1.137.264 por sorteio (teto). 19+: 1 em 34.195 (teto). Nenhuma construção passa disso.

Jogos em `data/jogos_C2989_K10.json` (feitos com ciclo e repetidas do C2988).
