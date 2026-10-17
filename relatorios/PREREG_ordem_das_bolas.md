# Pré-registro — ordem de saída das bolas e física do sorteio (17/10/2026)

Dados novos: `data/historico_ordem.csv` (ordem de saída das 20 bolas, C1–C2988). Nulo: 1.000 históricos sintéticos de 2.988 sorteios
(permutação uniforme das 100 dezenas, primeiras 20 em ordem). p empírico bilateral. **15 testes → limiar de Bonferroni p < 0,0033.**

1. Posição × valor: soma de z² das médias por posição (gl 20).
2. Primeira bola: χ² da uniformidade nas 100 dezenas.
3. Última bola: idem.
4. Correlação (Spearman) entre bolas consecutivas dentro do sorteio.
5. Runs test de paridade ao longo da ordem de saída.
6. Frequência de bolas consecutivas da mesma década (esperado 9/99).
7. Posição média de saída de cada dezena (soma de z², gl 100).
8. Primeira bola de t × década da primeira de t−1 (χ² 10×10).
9. Primeira bola de t × década da última bola de t−1 (continuidade física do globo).
10. Posição média das repetidas do sorteio anterior (esperado 10,5).
11. Runs test por dezena ao longo dos sorteios; KS da uniformidade dos 100 p-valores.
12. Periodograma (Fisher g) da contagem de dezenas 00–49 por sorteio.
13. Periodograma (Fisher g) da soma das 20 dezenas.
14. Compressibilidade (zlib) da sequência de sorteios.
15. Informação mútua sorteio t → t+1 (χ² da matriz 100×100 de co-ocorrência).

Regra de decisão: um teste só "passa" se p < 0,0033; depois precisa replicar em C1–C1494 vs C1495–C2988 (metades). Se nada passar: sem sinal.

## Resultado (1.000 históricos sintéticos, `python3 lab/bateria_ordem.py 1000`)
**Nenhum teste passou o limiar (p < 0,0033).** Menores p: teste 9 (primeira bola de t × última de t−1) = 0,034 e teste 2 (primeira bola) = 0,039; os outros 13 ficaram entre 0,17 e 0,94. Com 15 testes, esperam-se ~0,75 testes com p < 0,05 por acaso.
Primeira rodada teve um defeito de código (média com `nan` no runs test, p falso = 0,001); corrigido com `nanmean`, mesma semente e mesmos testes. Ordem de saída validada contra `historico.csv` (2.988/2.988 conjuntos iguais).
Conclusão: o processo físico (ordem das bolas, continuidade entre sorteios, periodicidade, compressibilidade, informação mútua) é indistinguível de um sorteio uniforme. Sem sinal.
