# Construção sequencial ("cada jogo nasce após os outros falharem") — 17/10/2026
Script: `lab/sequencial.py`.

## 1. Cálculo exato (hipergeométrico): jogo 2 fazer 20 dado que o jogo 1 fez 8–14
Incondicional: 1 em 11.372.636. a = |G1∩G2|.
| a | P(G2=20 \| G1 fez 8–14) | lift |
|---|---|---|
| 15 | 1 em 58,3 mi | ×0,19 |
| 20 | 1 em 16,4 mi | ×0,70 |
| 25 | 1 em 10,9 mi | ×1,04 |
| **28** | **1 em 10,5 mi** | **×1,08** |
| 30 | 1 em 10,8 mi | ×1,05 |
| 35 | 1 em 16,2 mi | ×0,70 |
Pico em a ≈ 28, com ganho máximo de 8% — apenas a fatia "G1 fez 8–14", que é ~90% dos sorteios. P(G2=20 e G1 fez 8–14) nunca passa de 1 em 11,9 mi (menor que a incondicional, como deve ser).

## 2. Construção sequencial vs conjunta (teste 800 mil simulados)
| Grupo | E[max] | P(≥15) | P(≥17) |
|---|---|---|---|
| Sequencial (jogo k cobre onde 1..k−1 falham) | 13,174 | 11,03% | 0,407% |
| K10 (otimização conjunta) | 13,234 | 11,21% | 0,402% |
| R10 (relógio + apoio otimizado) | 13,229 | 11,20% | 0,399% |
A sequência gulosa é pior que a conjunta: os primeiros jogos ficam travados e não podem se ajustar aos últimos.

## 3. Por que não passa disso
As 10 apostas são feitas antes do sorteio; o "falhou" do jogo 1 nunca é observado. Sequencial = ordem de otimização, e a conjunta já contém isso. A chance de 20 de 10 jogos distintos é 10 × 1/11.372.636 (1 em 1.137.264), independente da estrutura. Sequência real só existiria entre concursos, e não há dependência entre sorteios (lags 1–10, mutual information t→t+1, p = 0,84).
