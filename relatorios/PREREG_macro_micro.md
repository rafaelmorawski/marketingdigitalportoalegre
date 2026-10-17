# Pré-registro — macro × micro: quentes/mornas/frias e ciclo por fase (17/10/2026)
Hipótese do Rafael: o histórico inteiro é uniforme (macro), mas janelas recentes têm tendências (micro).
Nulo: 300 históricos sintéticos de 2.988 sorteios; p empírico bilateral. **13 testes → Bonferroni p < 0,0038.**
- T1–T5: janelas W = 5, 10, 20, 50, 100. A cada sorteio t, classificar as 100 dezenas pelas saídas nos W anteriores em tercis (frio/morno/quente; desempate ALEATÓRIO). Estatística: χ² de homogeneidade da taxa de saída em t entre os 3 estados.
- P1–P5: persistência. Blocos disjuntos de b = 5, 10, 20, 50, 100 sorteios; correlação entre a contagem de cada dezena no bloco j e no j+1 (agregada).
- O1–O2: sobredispersão em blocos de 20 e 50 (χ² médio por bloco das contagens por dezena vs binomial).
- C1: ciclo por fase: taxa de saída de cada pendente em t, estratificada pelo nº de pendentes restantes (1–3, 4–6, 7–10, 11+); χ² contra 0,20.
Decisão: passa se p < 0,0038 E replicar nas duas metades (C1–C1494 / C1495–C2988) com mesmo sinal. Senão: sem sinal.

## Resultado (400 históricos sintéticos, `python3 lab/macro_micro.py 400`)
**Nenhum dos 13 testes passou (p < 0,0038).** Menores p: persistência b=100 = 0,010 e temperatura W=100 = 0,020 (quente 20,27% vs fria 19,92%, o mesmo fenômeno medido de dois jeitos); os demais entre 0,085 e 0,86. Janelas de 5 a 50 sorteios: taxas de frio/morno/quente entre 19,8% e 20,2% (indistinguíveis). Sobredispersão em blocos de 20 e 50: 0,99 e 1,00 (binomial). Ciclo por fase: p = 0,33.
Conclusão: não há tendência micro detectável nas escalas curtas. Sem sinal.
