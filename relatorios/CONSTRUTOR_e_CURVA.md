# Capacidade de construção e curva de tamanho (17/10/2026)

## Ferramentas novas
- `lab/construtor.py`: mantém jogos FIXOS e otimiza N novos (3 bancos, controle de 40 aleatórios); objetivos emax | p15 | cauda; `--nucleo-relogio` (núcleo girando do Rafael); relatório com custo, E[max], P(≥15), P(≥17), chance de 20 e de 20-ou-0, piso garantido (adversário exato) e retorno aproximado.
- Exemplo: J fixo + 5 novos (15 jogos, R$ 45): E[max] 13,561 (aleatórios 13,444), P(≥15) 16,38% (15,83%), chance de 20 1 em 758.176, de 20-ou-0 1 em 379.089, piso garantido 10.
- `lab/repeticoes.py`: nunca terem repetido as 20 dezenas era o esperado (probabilidade 8e-15); quase-repetidos (12+ em comum) ocorrem no ritmo do acaso (26 observados vs 32,6 esperados).

## Curva de tamanho (`lab/curva_tamanho.py`; teste 500 mil inéditos)
| N | custo | P(≥15) otimizado | P(≥15) aleatório | ganho P15 por jogo extra | chance 20 ou 0 |
|---|---|---|---|---|---|
| 1 | 3 | 1,13% | 1,14% | 1,13 pp | 1 em 5,7 mi |
| 5 | 15 | 5,70% | 5,59% | 1,14 | 1 em 1,14 mi |
| 10 | 30 | 11,13% | 10,85% | 1,06 | 1 em 568.632 |
| 20 | 60 | 21,30% | 20,55% | 0,98 | 1 em 284.316 |
| 24 | 72 | 25,00% | 24,02% | 0,92 | 1 em 236.930 |
| 40 | 120 | 38,34% | 36,78% | 0,79 | 1 em 142.158 |
- Sem joelho: cada jogo vale ~1 pp de P(≥15) (cai devagar de 1,1 para 0,8 pp). A chance de 20 ou 0 cresce linearmente: 2N/11,37 mi.
- O ganho da otimização sobre aleatórios cresce com N: P(≥15) +0,28 pp (10 jogos), +0,98 pp (24), +1,56 pp (40). Em grades grandes, a construção evita desperdiçar sobreposição.
