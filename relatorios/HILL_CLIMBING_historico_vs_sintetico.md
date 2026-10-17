# Hill-climbing cria hipóteses melhores? (17/10/2026)
Script: `lab/hc_historico_vs_sintetico.py`. Construção C1–C1000, seleção C1001–C1700, teste C1701–C2988 (1.288 sorteios reais nunca vistos). Controle: 40 grades aleatórias de 10 jogos (E[max] 13,056; faixa 12,959–13,138; P(≥15) 10,85%).

| Grupo de 10 jogos | E[max] no teste | P(≥15) | ganho vs aleatório |
|---|---|---|---|
| Hill-climbing no histórico real | 13,207 | 12,34% | +0,150 |
| Hill-climbing em 1.000 sorteios sintéticos | 13,166 | 10,87% | +0,110 |
| K10 (150 mil sorteios simulados) | 13,262 | 12,42% | +0,205 |
| J espiral | 13,162 | 10,02% | +0,106 |

- Sobreajuste: o hill-climbing no histórico real mostrou +0,852 de ganho onde otimizou (E[max] 13,90; P(≥15) 41%) e entregou +0,150 fora (82% de encolhimento).
- O ganho de ~+0,1 a +0,2 é cobertura (jogos complementares), e vem igual de dados sintéticos. O K, que nunca viu o histórico, foi o melhor.
