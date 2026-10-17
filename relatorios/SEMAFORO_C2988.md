# Painel de semáforos — estado no C2988

Nulo: sorteio uniforme (300 mil simulados). Limiar de evidência: |z| > 3.45 (90 testes, Bonferroni). **Nenhuma hipótese abaixo está confirmada: o selo existe para isso.**

| | Indicador | Valor | Normal (média±dp) | z | Sequência do mesmo lado | Hipótese apontada | Evidência histórica |
|---|---|---|---|---|---|---|---|
| 🟡 | borda | 11 | 7.2±1.9 | +1.97 | 2 sorteio(s) acima | voltar à média no próximo | após alto: z=-1.03; LB p=0.44 → não confirmada |
| 🟡 | maior buraco | 23 | 15.7±4.2 | +1.74 | 1 sorteio(s) acima | repetir o lado no próximo | após alto: z=+0.32; LB p=0.72 → não confirmada |
| 🟡 | primos | 8 | 5.0±1.7 | +1.72 | 1 sorteio(s) acima | repetir o lado no próximo | após alto: z=+0.67; LB p=0.58 → não confirmada |
| 🟡 | desvio das dezenas | 33 | 28.1±2.7 | +1.66 | 1 sorteio(s) acima | voltar à média no próximo | após alto: z=-0.16; LB p=0.33 → não confirmada |
| 🟢 | múltiplos de 3 | 4 | 6.8±1.9 | -1.47 | 1 sorteio(s) abaixo | — | — |
| 🟢 | máx por coluna | 3 | 4.1±0.8 | -1.39 | 8 sorteio(s) abaixo | — | — |
| 🟢 | dezenas ≤31 | 9 | 6.4±1.9 | +1.39 | 1 sorteio(s) acima | — | — |
| 🟢 | décadas vazias | 2 | 1.0±0.8 | +1.31 | 8 sorteio(s) acima | — | — |
| 🟢 | repetidas do anterior | 2 | 4.0±1.6 | -1.24 | 1 sorteio(s) abaixo | — | — |
| 🟢 | múltiplos de 5 | 6 | 4.0±1.6 | +1.24 | 2 sorteio(s) acima | — | — |
| 🟢 | vizinhas coluna | 5 | 3.4±1.5 | +1.01 | 1 sorteio(s) acima | — | — |
| 🟢 | pares | 8 | 10.0±2.0 | -0.99 | 1 sorteio(s) abaixo | — | — |
| 🟢 | vizinhas linha | 2 | 3.5±1.5 | -0.95 | 1 sorteio(s) abaixo | — | — |
| 🟢 | repetidas na maior década | 1 | 1.5±0.6 | -0.82 | 1 sorteio(s) abaixo | — | — |
| 🟢 | mín por década | 0 | 0.3±0.5 | -0.67 | 8 sorteio(s) abaixo | — | — |
| 🟢 | soma | 1060 | 989.9±115.9 | +0.60 | 2 sorteio(s) acima | — | — |
| 🟢 | maior sequência | 3 | 2.6±0.7 | +0.56 | 1 sorteio(s) acima | — | — |
| 🟢 | vizinhas diagonal | 5 | 6.2±2.1 | -0.56 | 2 sorteio(s) abaixo | — | — |
| 🟢 | vizinhos-8 (agrupamento) | 12 | 13.1±3.1 | -0.36 | 2 sorteio(s) abaixo | — | — |
| 🟢 | amplitude | 93 | 91.4±5.6 | +0.29 | 2 sorteio(s) acima | — | — |
| 🟢 | consecutivos | 4 | 3.8±1.6 | +0.13 | 4 sorteio(s) acima | — | — |
| 🟢 | máx por década | 4 | 4.1±0.8 | -0.09 | 2 sorteio(s) abaixo | — | — |
| 🟢 | colunas vazias | 1 | 1.0±0.8 | +0.06 | 3 sorteio(s) acima | — | — |
| 🟢 | quadrante mínimo | 3 | 3.0±0.9 | -0.00 | 4 sorteio(s) abaixo | — | — |
| 🟢 | acima50 | 10 | 10.0±2.0 | +0.00 | 2 sorteio(s) acima | — | — |
| 🟢 | pares inferior−superior | 0 | 0.0±2.8 | -0.00 | 2 sorteio(s) abaixo | — | — |

## Tempo de ocorrência (há quanto tempo cada evento não acontece)

| Evento | Prob. por sorteio | Sem ocorrer há | Depois de m sorteios sem o evento, a taxa sobe? | Evidência |
|---|---|---|---|---|
| 🔴 pares ≥13 | 0.105 | 37 sorteios (m=13) | taxa 0.090 vs 0.105, z=-1.43 | não confirmada (limiar 3.45) |
| 🟢 pares ≤7 | 0.107 | 12 sorteios (m=13) | taxa 0.127 vs 0.107, z=+1.56 | não confirmada (limiar 3.45) |
| 🟢 2+ colunas vazias | 0.229 | 4 sorteios (m=6) | taxa 0.195 vs 0.229, z=-2.22 | não confirmada (limiar 3.45) |
| 🟢 acima50 ≥13 | 0.105 | 7 sorteios (m=13) | taxa 0.098 vs 0.105, z=-0.59 | não confirmada (limiar 3.45) |
| 🟢 soma ≥ decil 90 | 0.101 | 5 sorteios (m=14) | taxa 0.099 vs 0.101, z=-0.10 | não confirmada (limiar 3.45) |
| 🟢 repetidas ≤1 | 0.049 | 8 sorteios (m=28) | taxa 0.058 vs 0.049, z=+0.97 | não confirmada (limiar 3.45) |
| 🟢 soma ≤ decil 10 | 0.101 | 3 sorteios (m=13) | taxa 0.119 vs 0.101, z=+1.49 | não confirmada (limiar 3.45) |
| 🟢 sequência ≥4 | 0.099 | 3 sorteios (m=14) | taxa 0.106 vs 0.099, z=+0.64 | não confirmada (limiar 3.45) |
| 🟢 acima50 ≤7 | 0.106 | 2 sorteios (m=13) | taxa 0.133 vs 0.106, z=+2.04 | não confirmada (limiar 3.45) |
| 🟢 repetidas ≥8 | 0.018 | 3 sorteios (m=76) | taxa 0.028 vs 0.018, z=+1.58 | não confirmada (limiar 3.45) |
| 🟢 década vazia | 0.689 | 0 sorteios (m=2) | taxa 0.647 vs 0.689, z=-1.64 | não confirmada (limiar 3.45) |
| 🟢 2+ décadas vazias | 0.230 | 0 sorteios (m=6) | taxa 0.209 vs 0.230, z=-1.33 | não confirmada (limiar 3.45) |

## Como ler
- 🟢 normal (|z|<1,5) · 🟡 atenção (1,5–2) · 🔴 extremo (>2). Extremo acontece sozinho: com 26 indicadores, em torno de 1 deles fica 🔴 em qualquer sorteio.
- A hipótese é só a direção observada no histórico; nenhuma passou o limiar e nenhuma replicou. Não use para escolher dezenas.

