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

## Relógio do Rafael com apoio otimizado (`lab/relogio.py`, teste 800 mil simulados)
| Grupo | E[max] | P(≥15) | ganho |
|---|---|---|---|
| 40 aleatórios | 13,064 | 10,87% | — |
| J real (apoio do Rafael) | 13,177 | 11,11% | +0,113 |
| K10 (livre) | 13,234 | 11,21% | +0,170 |
| Relógio + apoio aleatório | 13,074–13,094 | 10,63–10,85% | +0,01 a +0,03 |
| Relógio + apoio otimizado (com ou sem a regra "nunca o núcleo anterior") | 13,229–13,231 | 11,19% | +0,166 |
O núcleo girando não custa cobertura; o ganho vem da escolha do apoio. A regra do núcleo anterior é neutra. R10 em `data/jogos_C2989_R10.json`.
