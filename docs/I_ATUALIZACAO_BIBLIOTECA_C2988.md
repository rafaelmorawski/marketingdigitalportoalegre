# I — ATUALIZAÇÃO DA BIBLIOTECA E DO PENSAMENTO
**Documento nº9 da biblioteca — complementa A, B, C, D, E, F, G, H**
**Processado até C2987 (14/10/2026) | grade para C2988 definida | histórico: 2987 sorteios**

---

## 1. ESTADO ATUAL

**C2987:** 07 12 20 29 31 32 39 43 44 48 50 52 60 61 69 84 85 90 91 99 (soma 1.046, 10 pares, década 70–79 vazia).
Ordem de extração: 52 12 39 61 43 44 32 50 84 60 90 69 07 31 20 29 99 85 91 48 (um único sorteio: sem nada a testar).

**Conferência do C2987 (30 jogos apostados):** melhor 14 (J7 e C30, o de cenário), média 10,13. Espiral J1–J10: 8, 11, 8, 8, 11, 10, 14, 10, 11, 8 (melhor 14, média 9,90). Ninguém fez 20, como esperado (1 em 406 mil com 28 jogos).

**Ciclo (iniciado em C2978):** o C2987 foi o 10º sorteio; saíram 2 das 13 faltantes (44 e 84). **Faltam 11:** 00 01 42 46 47 49 51 62 67 83 88. Repetidas do C2986 no C2987: 7 (07 12 31 39 48 85 90; esperado 4). Fechamento do ciclo atual: mediana ~14 sorteios (10%–90%: 9–22).

---

## 2. A GRADE PARA O C2988 — 24 JOGOS, CADA UM COM SUA RAZÃO DE EXISTIR

| Grupo | Jogos | Razão de existir |
|---|---|---|
| Espiral de núcleo rígido | J1–J10 (os mesmos do C2987, fixos) | Hipótese do Rafael: núcleo de 20 dezenas (2 por década) que anda 2 casas à direita por jogo (período 5; cada dezena em 2 núcleos); apoio de 30 com 4–7 repetidas do último sorteio, ≥4 ausentes do ciclo, ≥3 atrasadas; nunca repete dezenas do núcleo anterior (inversão); consecutivos com ≥20 dezenas diferentes. Núcleo do J1: 00 01 12 13 24 25 37 38 46 47 54 55 67 68 78 79 83 84 92 93 |
| Cobertura da falha | F1–F5 (fixos) | Construídos um a um por hill-climbing contra os sorteios simulados em que a espiral fica em ≤14. Não usam ciclo nem repetidas; dependem só dos J. Região de falha (melhor ≤12): de 27,7% para 13,7% |
| Impopular | U1 | Reduz a divisão do prêmio quando acerta 15–19 (30 pares, 16 dezenas ≥80); ganho estimado ≈ R$ 0,05 por bilhete por concurso |
| Edge das três lentes | E1 | 9 do ciclo menos cobertas, 8 repetidas menos cobertas, resto = dezenas de maior presença na região de falha (as menos cobertas) |
| Jogo do Rafael | Y1 | Hipótese trazida por ele |
| Hill-climbing sobre o conjunto | H1 | Busca pesada (8 reinícios x 5.000 trocas, seleção em 400 mil sorteios) contra os 18 |
| Dois trazidos pelo Rafael | Z1, Z2 | Hipóteses trazidas por ele (Z1 tem 40 dezenas em comum com o U1) |
| Baixa sobreposição | N1 | Mínima colisão para 19+ contra os 19 anteriores |
| Consenso | CA (50 mais presentes nos 22), CB (5 mais presentes por década) | "O que todos os jogos concordam"; CA×CB compartilham 46 |

**Conjunto (24 jogos):** distintos e válidos, 100/100 dezenas, sobreposição 16–46 (média 24,5). Chance de 20: 1 em 476.282 por sorteio (teto 1 em 473.860). 19+: 1 em 14.362. Custo R$ 72/concurso. Simulado: E[max] 13,89, P(≥15) 24,1%, melhor ≤12 em 4,7%.

```
J1: 00 01 03 07 12 13 14 15 16 17 18 21 24 25 26 27 28 30 31 34 37 38 40 42 46 47 48 51 54 55 57 60 61 62 64 67 68 69 73 74 78 79 83 84 88 89 92 93 97 98
J2: 02 03 05 06 07 08 14 15 16 19 21 22 26 27 28 30 32 33 35 39 40 42 44 45 48 49 50 53 56 57 59 60 61 62 66 69 70 71 72 74 80 82 85 86 88 89 94 95 97 99
J3: 01 04 05 11 16 17 19 24 25 28 29 31 32 34 35 40 41 44 46 50 51 53 55 58 59 61 62 63 64 65 66 68 72 73 74 75 77 78 79 80 87 88 89 90 91 92 93 96 97 98
J4: 00 01 03 06 07 09 11 15 18 19 20 21 22 23 24 26 27 33 34 37 38 39 42 43 45 46 50 51 54 55 56 57 60 63 64 69 70 74 75 76 77 78 80 82 83 86 89 94 98 99
J5: 00 02 04 05 08 09 10 11 12 13 14 15 22 23 25 28 31 32 35 36 41 44 45 47 48 52 53 54 58 60 61 65 66 67 69 71 72 73 76 77 81 82 83 86 90 91 92 93 94 97
J6: 00 01 02 04 05 06 12 13 15 18 20 24 25 29 30 32 33 34 37 38 39 42 46 47 48 49 50 51 54 55 58 59 62 67 68 73 75 78 79 83 84 85 86 87 88 92 93 94 95 99
J7: 02 03 04 07 08 09 14 15 17 18 20 23 26 27 28 29 30 31 32 39 41 43 44 48 49 51 56 57 59 60 62 63 64 65 66 69 70 71 73 80 81 85 86 87 88 90 91 94 95 98
J8: 01 04 05 06 07 08 09 10 13 16 17 19 21 22 23 28 29 31 32 33 35 36 37 40 41 43 45 47 50 52 53 54 58 59 61 62 63 64 67 72 73 76 80 84 87 88 96 97 98 99
J9: 01 02 06 07 10 11 13 14 18 19 20 21 26 33 34 36 42 43 44 47 48 49 50 51 52 53 57 63 64 65 66 67 70 71 74 75 76 77 78 79 80 81 85 89 90 91 92 93 98 99
J10: 01 03 08 09 10 11 14 15 16 22 23 24 27 29 30 35 36 38 39 40 41 44 45 46 49 52 53 54 55 56 62 65 66 68 69 72 76 77 78 79 81 82 83 84 90 91 92 94 95 96
F1: 02 03 05 10 11 12 13 14 15 16 17 18 19 20 21 23 25 26 27 30 31 32 34 35 36 38 39 40 47 51 58 59 60 61 63 65 67 68 70 75 78 82 86 87 90 91 95 96 97 99
F2: 00 06 08 11 12 13 17 20 21 22 23 24 25 27 28 29 30 31 33 34 37 41 42 43 46 48 49 56 59 61 62 64 65 69 71 72 75 77 82 83 84 86 87 89 90 91 93 95 96 99
F3: 03 05 07 10 11 17 18 22 24 26 28 31 33 35 36 37 39 42 43 44 46 47 49 52 53 54 56 57 59 65 68 71 72 74 75 76 79 80 82 83 84 85 86 87 89 92 93 95 96 98
F4: 00 02 03 04 05 06 08 09 10 12 14 17 18 22 24 26 28 29 33 34 35 36 39 40 41 43 45 46 47 50 52 55 57 58 61 63 64 70 71 73 77 80 81 83 86 90 93 95 97 99
F5: 00 01 02 03 04 06 07 08 09 10 12 15 16 17 20 22 25 29 30 32 33 34 38 39 43 44 45 52 53 55 60 61 63 65 67 68 69 70 72 73 74 75 76 79 80 81 84 85 93 97
U1: 00 05 06 10 14 15 16 20 25 28 29 30 33 34 35 40 45 46 47 50 55 56 58 59 60 64 65 66 70 75 76 77 78 79 80 82 84 85 86 87 88 89 90 91 92 93 94 95 96 98
E1: 00 01 04 08 09 12 13 16 19 20 21 23 25 27 36 37 38 41 42 43 45 48 49 50 51 52 54 55 56 57 58 62 66 67 68 70 71 74 77 81 82 83 84 85 87 88 89 94 96 97
Y1: 00 02 05 06 09 12 13 15 19 22 23 27 32 33 34 35 37 38 39 40 41 42 46 48 50 52 53 56 57 61 63 64 68 70 71 72 73 78 79 81 83 84 85 87 88 90 91 92 96 97
H1: 03 04 07 08 12 14 16 17 18 19 20 22 24 25 26 27 29 33 35 38 41 43 44 46 48 50 51 52 58 61 66 69 70 71 73 76 77 78 79 82 83 87 88 89 91 92 94 95 98 99
Z1: 00 02 04 08 09 10 12 16 19 21 24 25 26 31 36 37 38 40 41 42 43 45 49 51 52 54 55 56 57 58 59 60 62 66 67 68 70 71 74 75 77 81 84 85 87 88 89 90 94 96
Z2: 01 02 03 06 07 11 13 15 17 20 24 26 28 30 31 32 33 36 37 40 41 43 44 45 46 47 49 51 52 56 57 58 61 63 67 68 69 74 77 78 81 83 86 87 88 90 91 92 94 99
N1: 00 02 09 10 12 13 16 17 18 19 21 23 24 29 30 31 32 37 39 40 42 44 45 47 49 55 56 57 58 59 60 61 63 66 69 71 72 74 76 77 78 79 81 85 87 93 94 96 98 99
CA: 00 02 06 09 10 12 13 15 16 17 20 22 24 25 26 29 30 31 32 33 40 41 43 45 46 47 52 56 57 58 61 63 68 69 70 71 74 77 78 79 83 84 87 88 89 90 91 93 94 96
CB: 00 02 03 06 09 10 12 15 16 17 20 24 25 26 29 30 31 32 33 37 40 41 43 45 46 52 55 56 57 58 61 63 66 68 69 70 71 77 78 79 83 84 87 88 89 90 91 93 94 96
```

---

## 3. O PENSAMENTO ATUALIZADO

1. **Nenhuma regra de seleção de dezenas prevê o sorteio, em nenhuma escala.** Reconfirmado do micro (janelas de 3 sorteios) ao macro (300), com modelos de ML fortes e com testes de viés físico.
2. **O score de cobertura (E[max], P(≥15)) NÃO é retorno financeiro.** Cada bilhete é pago pelos próprios acertos; o retorno esperado de N jogos é N x o de um bilhete (≈ R$ 1,12 com os prêmios médios, ≈ R$ 1,53 com o acumulado de R$ 10,47 mi), qualquer que seja a sobreposição. A cobertura muda só a chance de pelo menos um jogo ver 15+.
3. **A chance de 19+ de N jogos é a soma das chances de cada um** (1 em 341.951 por bilhete) menos a colisão entre jogos. Nosso conjunto de 19 jogos fica a 0,00077% do teto; o melhor desenho possível (recozimento) ganharia 0,0007%. O único jeito de aumentar é pôr mais bilhetes distintos.
4. **Errar 20 (zero acerto) é a mesma loteria que acertar 20** (1 em 11.372.636 por bilhete; o espelho de um jogo que faz 20 faz 0). Cada bilhete já carrega as duas pontas.
5. **As alavancas que existem, por tamanho:** (a) mais bilhetes distintos (dominante); (b) desenho complementar de baixa sobreposição (≈ +0,1 em E[max], +0,5 pp em P(≥15) sobre aleatórios); (c) cobrir a região de falha (prêmio de qualidade ≈ +0,05 a +0,2 pp sobre aleatório); (d) perfil impopular (≈ +R$ 0,05 por bilhete); (e) aprendizado com experimentos registrados antes.
6. **Padrão de honestidade:** comparar sempre com 30–60 controles aleatórios e reportar a faixa; medir fora da amostra; nunca aceitar achado de retroteste isolado.

---

## 4. DESCOBERTAS NOVAS (validadas)

### 4.1 Probabilidades por bilhete (qualquer conjunto de 50 dezenas)
P(exatamente 14) = 2,781% (1 em 36); P(13) = 6,61%; P(12) = 12,16%; P(≥15) = 1,142%. Todos os bilhetes têm a mesma distribuição (média 10,00, desvio 2,01). Simulado: de 2,758% a 2,795% entre os 19 jogos (erro ±0,015).

### 4.2 Paridade do bilhete não importa
Bilhetes com 25, 38, 12 ou 45 pares: média 9,999–10,002, desvio 2,010–2,012, P(≥15) 1,143%–1,157%. Condicionado ao sorteio muda (38 pares faz 11,83 com ≥13 pares, 8,17 com ≤7), mas o saldo é zero. Grade polarizada (45/5 e 5/45) piora: E[max] 12,720 contra 13,061 balanceada. O equilíbrio 25/25 nunca foi imposto: saiu natural (um bilhete aleatório tem 25 pares, desvio 2,5). 24º jogo por faixa de pares: +0,915 a +0,942 pp contra +0,86 aleatório (ruído).

### 4.3 Desenhos de espiral
- Espiral refeita com C2987 e ciclo/repetidas novos (S1–S10): E[max] 13,152 ± 0,007 (5 sementes), igual ao Grupo 1 (13,175; diferença = esforço de busca). Atualizar não melhora nem piora.
- **30 fixas + 20 girando (5 jogos) custam cobertura:** sobreposição 30–40 entre eles; sozinhos E[max] 11,91 e P(≥15) 4,84% (5 aleatórios: 12,33 / 5,59%); somados a J1–J10: +4,25 pp contra +4,98 pp de aleatórios e +4,94 pp de S1–S5. Otimizar as 30 fixas muda só +0,04–0,1 pp.
- Plano J + R + C (3 grupos): P(≥15) 19,60% contra 20,55% de 20 aleatórios. **J + S1–S5 + 5 contra a falha: 21,01%** (melhor desenho de 20). J + 5 contra a falha (15 jogos): 16,25% (J + 5 aleatórios: 16,02%).
- Efeito "armadilha" (condicional): quando o núcleo do jogo k acerta 0–2 (17,6% dos sorteios), o jogo k+1 faz em média 11,45 acertos (contra 10,00). Não eleva a chance de 20.

### 4.4 Região de falha da grade
A falha é difusa: nos sorteios onde o melhor jogo fica em ≤12, as dezenas mais presentes são as menos cobertas (correlação cobertura x presença −0,98/−0,99). Ciclo (lift ~1,00), repetidas (~1,00) e duplas (~1,01) NÃO explicam a falha; por década não há efeito (0,98–1,06). Com 16 jogos: P(melhor <15) = 82,8%, P(≤12) = 12,15%.

### 4.5 Viés nos próprios jogos (auditoria dos 16)
Contra 1.500 portfólios aleatórios: desvio da cobertura entre dezenas 0,97 contra 2,00 ± 0,13 (z −7,7; desenho nosso, intencional); pares de dezenas consecutivas por jogo 26,7 contra 24,4 ± 0,6 (z +3,7; vem do núcleo de pares vizinhos; inofensivo). Sem inclinação para quentes, frias, do último sorteio ou do ciclo.

### 4.6 Conjuntos de 15–24 jogos
J + F + G (20): P(≥15) 21,00% (J + F + 5 aleatórios 20,90%; 20 aleatórios 20,52%). Cada jogo extra soma ~0,9–1,0 pp em P(≥15); o prêmio de qualidade (contra aleatório) ficou em +0,04 a +0,11 pp (H1: +0,044; edge das lentes: +0,11). Jogo "proibido" sem regras: +0,942 pp contra +0,870 aleatório; resgata sorteios em 14 para 15+ em 1,04% (aleatório 1,14%). Dois resultados imaginários + 10 dezenas: +0,825/+0,857 pp contra +0,811/+0,809. Consenso (CA/CB): +0,725/+0,715 pp contra +0,879 aleatório (mais redundante, perde ~0,16 pp).

### 4.7 Perfil de décadas e paridade do SORTEIO (grade de 17–22)
Perfil espalhado (sem década vazia, ≤3 por década) = 11,2% dos sorteios; a grade vai melhor que aleatória em todos os perfis; ponto mais fraco: 2+ décadas vazias (P(≥15) 17,24% contra 17,62%). Por pares do sorteio (≤7 a ≥13) nenhuma faixa fica abaixo do aleatório de forma relevante.

### 4.8 Popularidade (retorno por ganhador)
A estrutura do sorteio prevê a popularidade (razão de ganhadores de 15 acertos): correlação fora da amostra 0,41 (R² 0,11; ajuste C2400–C2700, teste C2701–C2986). Efeito de um bilhete "impopular" no retorno esperado: aleatórios 0,000 ± 0,007; J +0,004; F −0,005; impopular otimizado +R$ 0,053 por bilhete. Pequeno demais para mudar decisão.

### 4.9 Limites do histórico (2.987 sorteios) = limites do sorteio uniforme
Maior ausência de uma dezena 49 (simulado: média 52, faixa 43–92); maior sequência seguida 6 (simulado 7,5); soma média 987, 1%–99% de 712–1.262 (uniforme 715–1.262); repetidas do anterior média 4,01; 4+ numa década 77,9% (igual); ciclo de 100 dezenas média 24,4 (122 ciclos; uniforme 24,0); frequência das dezenas qui-quadrado p=0,90. Dia da semana: homogêneo (7 dezenas p<0,05, esperado 5; KS p=0,58; soma ANOVA p=0,17). Estabilidade no tempo (10 blocos): 7 dezenas p<0,05, KS p=0,22.

### 4.10 Micro x macro
Correlação entre sorteios próximos (lags 1–10): −0,0043 a +0,0014 (maior |z| 2,35; limiar 2,81). Sobredispersão em janelas de 2–50 sorteios: 1,000–1,004 (z −0,86 a +0,49). P(dezena sai | n vezes nos últimos 3): 20,06/19,82/20,35/20,40%. Quentes/frias em janelas de 3, 5, 10, 20, 30, 100 e 300: média 9,93–10,06; maior |z| 1,81 (14 testes; limiar 2,91). Repetida do último sorteio: 20,07% (z +0,44); faltante do ciclo: 19,93% (z −0,41); por tamanho do ciclo 19,4%–20,1%.

### 4.11 ML forte (a prova mais dura disponível)
Gradiente boosting e regressão logística, 28 variáveis por dezena (últimos 10 sorteios, 6 janelas, gap, posição no ciclo, década, paridade, etc.), treino C300–C1999 e teste C2000–C2986 (987 sorteios nunca vistos): AUC 0,4992 e 0,4988 (acaso 0,5000); top-50 faz 9,990 e 9,997 acertos (esperado 10,000; z −0,16 e −0,05); top-20 faz 3,976 e 3,963 (esperado 4,000). **Controle com rótulos embaralhados rende o mesmo** (AUC 0,4986; top-50 9,970). Conclusão: modelos mais poderosos não acham nada que não exista nos dados; qualquer promessa de "script de predição" para a Lotomania deve passar por este mesmo teste.

### 4.12 Retroteste dos palpites e Monte Carlo
103 palpites recuperados x 2.986 sorteios (307.558 combinações): máximo 19 (uma vez, C2827); nenhum 20. ≥15: 3.618 (esperado 3.511); ≥18: 17 (13,6); ≥19: 1 (0,9). Monte Carlo de 100 sorteios contra 28 jogos: 16 chegam a 15+ (esperado 19 ± 4; todos abaixo de 15 tem chance 5×10⁻¹⁰); os "buracos" que aparecem em 100 sorteios são ruído (dezena que mais escapa 11 vezes = percentil 11 do acaso). 7 milhões de sorteios contra 20 jogos: 11 sorteios com 20 acertos (esperado 12,3); o primeiro só no 2.105.480º.

### 4.13 Retorno e momento
Retorno esperado por bilhete R$ 3: faixas 15–19 e zero ≈ R$ 0,61; jackpot ≈ R$ 0,51 (média). Com o acumulado de R$ 10,47 mi: ≈ R$ 1,53 por bilhete. Igualar o preço exigiria acumulado ≈ R$ 30 mi (nunca ocorreu nos últimos 600 concursos; máximo R$ 2,05 de retorno no C2675, acumulado R$ 17,2 mi).

---

## 5. REFUTADO OU SEM SINAL (não retestar)

- Qualquer modelo de ML (boosting, logística) com features de lag, janela, gap, ciclo e estrutura.
- Dezenas "que escaparam do melhor jogo" como regra (portfólios aleatórios, 5 sementes, janelas 10 e 20: média 10,00–10,06; maior |z| 1,62).
- Quentes, frias e atrasadas em janelas de 3 a 300; repetidas e faltantes do ciclo como sinais.
- Dia da semana e deriva no tempo (conjunto/máquina de bolas).
- Paridade do bilhete, décadas e perfil do sorteio como critério de vantagem.
- Construir sobre dois resultados imaginários, sobre sorteios simulados curtos (100) ou sobre "consenso" dos próprios jogos: iguais a aleatório ou pior.

---

## 6. ARMADILHAS NOVAS (acréscimo ao arquivo B)

13. **Score de cobertura não é retorno:** E[max]/P(≥15) medem só a chance de ver 15+; o retorno esperado é aditivo por bilhete.
14. **Ajuste a poucos sorteios (overfitting):** um jogo otimizado em 100 sorteios simulados rende como aleatório fora deles.
15. **Premissa "todos os 100 sorteios ficam abaixo de 15" é falsa:** em 100 sorteios, ~19 (±4) chegam a 15+ com 28 jogos.
16. **Ler "buraco" em amostra pequena:** com 100 sorteios, qualquer dezena que escapa 11 vezes está dentro do acaso.
17. **Restrição de sinais conhecidos custa ~0, mas não ganha nada:** forçar ausentes/repetidas não muda a cobertura nem a chance.
18. **Confundir a escolha do conjunto com a chance de 20:** a chance de 20 de N jogos distintos é N x 1/11.372.636 (menos colisões desprezíveis).

---

## 7. MUDANÇAS NO PROTOCOLO (arquivo B)

- **Acompanhamento por grupo a cada resultado:** J, F, U1, E1, Y1, H1, Z1/Z2, N1, CA/CB; registrar melhor placar e média de cada grupo (esperado: melhor do grupo de 10 ≈ 13,2; média 10,0). Distinguir grupos exige ~170 sorteios.
- **Painel de teste de predição (opcional):** rodar a cada resultado novo o modelo forte (4.11) fora da amostra e registrar AUC e acertos do top-50; só um desvio sustentado e corrigido por múltiplos testes justificaria ação. **Script reproduzível: `painel_predicao.py`** (anexo desta biblioteca): `python3 painel_predicao.py --csv Lotomania.csv --extra "<20 dezenas do sorteio novo>"`; reproduz os números da seção 4.11 (AUC 0,4992 / 0,4988 / controle 0,4986) e acrescenta uma linha ao `painel_log.csv` a cada rodada.
- **Tratar a espiral como estrutura de cobertura, nunca como previsão.** Manter fixa ou refazer com ciclo/repetidas novos tem a mesma chance.
- **Limite de gasto:** definir um valor mensal aceitável de perda antes de apostar (retorno esperado ≈ 37% do custo).

---

## 8. PENDÊNCIAS

1. Conferir o C2988 por grupo (J, F, U1, E1, Y1, H1, Z1/Z2, N1, CA/CB) e atualizar o ciclo (11 faltantes).
2. Registrar a primeira linha do painel de ML (opcional) e o ledger de grupos.
3. Testar a previsão de popularidade (modelo ajustado até C2983) quando a planilha com ganhadores de C2984–C2987 estiver completa.
4. Acompanhar o acumulado: só vale ajustar o gasto quando o retorno esperado se aproximar do preço (≈ R$ 30 mi).

---

## 9. RESSALVA FINAL

Todos os ganhos acima são **cobertura em sorteios simulados uniformes** e **estatística descritiva do histórico**. Nenhum prevê o próximo sorteio. A chance de 20 acertos continua 1 em 11.372.636 por bilhete (1 em 476.282 com os 24 jogos). O valor do método é reduzir erro de construção, medir honestamente e não se convencer de padrão onde só existe acaso.
