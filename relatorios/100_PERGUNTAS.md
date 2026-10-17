# As 100 perguntas do laboratório

✅ respondida · 🟡 parcial · ⚪ aberta · ★ prioridade alta entre as abertas

**Total 100: 36 respondidas, 16 parciais, 48 abertas (23 de prioridade alta).**

## 1. O globo é uniforme? (integridade)

| # | Pergunta | Status | Resposta / nota |
|---|---|---|---|
| 1 | Cada uma das 100 dezenas sai com 20%? | ✅ | sim, χ² uniforme |
| 2 | O nº de acertos de bilhetes quaisquer segue a hipergeométrica nos 2.988 sorteios? | ✅ | média 10,00, dp 2,01 |
| 3 | Houve quebra de regime (troca de globo, método ou regra) em algum ponto de C1–C2988? | 🟡 | deriva testada; quebra pontual aberta |
| 4 | Alguma dezena específica tem viés em janelas longas (500 sorteios)? | ⚪ |  |
| 5 | A ordem de saída das bolas tem padrão? | ✅ | não (15 testes) |
| 6 | Dia da semana, local ou horário mudam algo? | 🟡 | dia da semana: não; local e horário abertos |
| 7 | Concursos especiais diferem dos comuns? | ⚪ |  |
| 8 | Depois de concursos acumulados o sorteio muda? | ⚪ |  |
| 9 | O volume de apostas (arrecadação) se relaciona com algo do sorteio? (não deveria) | ⚪ |  |
| 10 | Qual a menor distorção que nossos testes conseguiriam detectar (poder estatístico)? | ⚪★ | pergunta-chave de honestidade |

## 2. Memória temporal

| # | Pergunta | Status | Resposta / nota |
|---|---|---|---|
| 11 | O sorteio t depende de t−1 … t−10? | ✅ | não |
| 12 | Existe dependência em lags longos (50, 100, 52 semanas)? | ⚪ |  |
| 13 | Dezenas quentes e frias persistem? | ✅ | não (janelas 5–100) |
| 14 | As pendentes do ciclo saem mais? | ✅ | 19,93% vs 20,00% |
| 15 | As repetidas do anterior passam de 4 por sorteio? | ✅ | não (20,07%) |
| 16 | O tempo de espera de cada dezena é geométrico? | ⚪ |  |
| 17 | Dezena atrasada volta mais (hazard por dezena)? | 🟡 | por evento: não; por dezena aberto |
| 18 | Há periodicidade (FFT) na soma ou nas contagens? | ✅ | não |
| 19 | Há sobredispersão em blocos de sorteios? | ✅ | 1,00 (binomial) |
| 20 | A duração do ciclo bate com o esperado (24,4 vs 24,0)? | ✅ | sim |
| 21 | Existe memória de segunda ordem (t depende de t−1 e t−2 juntos)? | ⚪ |  |
| 22 | Pares de dezenas saem juntos além do acaso? | ⚪★ | co-ocorrência 100×100 |
| 23 | Pares de dezenas se repelem? | ⚪★ |  |
| 24 | Existem grupos (comunidades) de dezenas afins? | ⚪★ |  |

## 3. Formas do sorteio

| # | Pergunta | Status | Resposta / nota |
|---|---|---|---|
| 25 | A soma das 20 dezenas tem distribuição esperada e tendência? | ✅ | sim, sem tendência |
| 26 | Pares × ímpares: muda a quantidade ou repete? | ✅ | χ² p=0,85; sem memória |
| 27 | Acima × abaixo de 50? | ✅ | uniforme |
| 28 | Décadas vazias: frequência e tempo para ocorrer? | ✅ | sem memória |
| 29 | Sequências de números consecutivos? | ✅ | sem desvio |
| 30 | Agrupamento ou repulsão no volante (vizinhas)? | ✅ | sem desvio |
| 31 | Borda × centro do volante? | ✅ | sem desvio |
| 32 | Simetria: pares de espelho (d e 99−d) dentro do mesmo sorteio? | ⚪ |  |
| 33 | Quadrantes e diagonais? | ✅ | sem desvio |
| 34 | Formas geométricas (linha cheia, cruz, L)? | ⚪ |  |
| 35 | Distribuição conjunta de dois indicadores (soma × pares)? | ⚪★ | combinações |
| 36 | Terminações (colunas) repetidas ou ausentes? | ✅ | sem desvio |
| 37 | Primos, múltiplos de 3 e de 5? | ✅ | sem desvio |
| 38 | Quantas dezenas em comum entre sorteios consecutivos? | ✅ | média 4,0 |
| 39 | Deslocamento médio do sorteio t−1 para t no volante? | ⚪ |  |
| 40 | A forma do sorteio muda com a posição no ciclo? | 🟡 | ciclo por fase: p=0,33 |

## 4. Predição

| # | Pergunta | Status | Resposta / nota |
|---|---|---|---|
| 41 | ML forte (boosting, logística) consegue AUC > 0,5? | ✅ | não (0,4955–0,5020) |
| 42 | Um aprendiz online sobre muitas lentes acerta mais? | ✅ | não |
| 43 | A lente coluna±10 se confirma com dados novos? | 🟡 | pré-registrada, em acompanhamento |
| 44 | Um ensemble dos melhores modelos melhora? | ⚪ | esperado: não |
| 45 | Modelos sequenciais (LSTM, transformer) acham algo que o boosting não achou? | ⚪ |  |
| 46 | É possível prever eventos raros (≥17 acertos)? | ⚪ |  |
| 47 | Alguma variável externa (calendário, lua, clima) tem sinal? | ⚪★ | teste barato |
| 48 | O modelo de popularidade (nº de ganhadores) calibra? | 🟡 | ordena, não calibra |
| 49 | A soma ou a paridade do próximo sorteio são previsíveis? | ✅ | não |
| 50 | Um meta-modelo escolhe a lente certa em cada janela? | ✅ | não (viés de seleção) |
| 51 | O histórico é compressível ou tem estrutura de baixa entropia? | ✅ | não |
| 52 | Algum subconjunto fixo de dezenas tem taxa diferente de 20%? | ⚪ |  |

## 5. Cobertura e construção

| # | Pergunta | Status | Resposta / nota |
|---|---|---|---|
| 53 | Qual o teto teórico de E[max] com 10 jogos? | ⚪★ |  |
| 54 | Qual o mínimo de acertos garantido do melhor jogo com N jogos (covering design)? | ⚪★ | 2 jogos complementares garantem ≥10 |
| 55 | Qual a sobreposição ótima entre jogos por objetivo (≥15, ≥17, ≥19)? | 🟡 | ≈25–28 |
| 56 | Quanto sobe P(≥15) por jogo adicional (retorno decrescente)? | ⚪★ |  |
| 57 | Qual o nº de jogos de melhor razão benefício/custo? | ⚪★ |  |
| 58 | O espelho (complemento) de um jogo ajuda para 0 e 20 acertos? | 🟡 | mesma probabilidade |
| 59 | Os 24 jogos atuais têm redundância desperdiçada? | 🟡 | auditoria |
| 60 | Hill-climbing sobre o histórico generaliza? | ✅ | não (82% some) |
| 61 | Hill-climbing sobre simulados melhora com mais amostra? | 🟡 | sim, até ~+0,17 |
| 62 | A paridade do bilhete importa? | ✅ | não |
| 63 | A restrição de 2 por década custa algo? | ✅ | nada |
| 64 | Relógio com apoio otimizado vs jogo livre? | ✅ | igual (+0,166 vs +0,170) |
| 65 | Construção sequencial vs conjunta? | ✅ | conjunta é melhor |
| 66 | Estruturas matemáticas (códigos, designs, espaços finitos F₂⁷) cobrem melhor que hill-climbing? | ⚪★ | matemática avançada |
| 67 | Qual a melhor cobertura para o prêmio de 0 acertos? | ⚪ |  |
| 68 | Qual construtor maximiza a cauda (≥17)? | ⚪ |  |
| 69 | Quanto E[max] compra cada R$ 3 extras? | ⚪ |  |
| 70 | A grade de 24 jogos está perto do teto de 19+? | 🟡 | a 0,00077% do teto |

## 6. Economia e risco

| # | Pergunta | Status | Resposta / nota |
|---|---|---|---|
| 71 | Retorno esperado por bilhete em função do acumulado? | ✅ | ≈R$ 0,61 + 0,089/mi |
| 72 | A partir de qual acumulado o retorno iguala o preço? | ✅ | ≈R$ 30 mi, nunca visto |
| 73 | Qual a chance de ganhar qualquer prêmio por concurso com 24 jogos? | ⚪★ |  |
| 74 | Prêmio esperado e variância por faixa (15–19 e 0)? | 🟡 |  |
| 75 | Quantos co-ganhadores esperar no 20 acertos? | ⚪ |  |
| 76 | Bilhetes impopulares valem quanto? | ✅ | ≈R$ 0,05/concurso |
| 77 | Probabilidade de perder X reais em N concursos (risco de ruína)? | ⚪★ | decisão de orçamento |
| 78 | Quantos concursos até 50% de chance de ver um 19+ com 24 jogos? | ⚪★ | ≈10.000 |
| 79 | Quanto tempo até 50% de chance de um 20 acertos com 24 jogos? | ⚪★ | ≈330 mil concursos |
| 80 | O imposto sobre prêmios altera o retorno? | ⚪ |  |
| 81 | Arrecadação por dia e mês: quando acumula mais? | ⚪ |  |
| 82 | Há sazonalidade nos valores acumulados? | ⚪ |  |
| 83 | Retorno real das nossas apostas vs esperado? | 🟡 | ledger ainda curto |
| 84 | Valor esperado de apostar só acima de R$ X mi? | ⚪★ |  |
| 85 | Outra loteria (Lotofácil, Quina, Mega-Sena) tem melhor retorno por real? | ⚪★ | só se você pedir |

## 7. Rigor e decisões

| # | Pergunta | Status | Resposta / nota |
|---|---|---|---|
| 86 | Qual o poder do painel de predição? (viés injetado de 0,5, 1 e 2 pp) | ⚪★ |  |
| 87 | O p do nosso protocolo é calibrado (falsos positivos na taxa nominal)? | ⚪★ |  |
| 88 | Quantos sorteios para confirmar a coluna±10 (efeito 0,25 pp)? | ✅ | milhares |
| 89 | Quantos sorteios para distinguir dois grupos de jogos? | ✅ | ≈170 |
| 90 | O ledger por grupo já distingue algo? | ⚪ | n pequeno |
| 91 | O robô reproduz os números de referência após cada mudança (teste de regressão)? | ⚪★ |  |
| 92 | Há divergências entre a planilha e a API (correções, duplicatas, datas)? | 🟡 | 2.987/2.987 iguais |
| 93 | As conclusões mudam com a semente ou com o tamanho dos bancos? | 🟡 |  |
| 94 | Que fração dos 'achados' o nosso auditor derruba? | ⚪ |  |
| 95 | Qual critério para encerrar a busca por sinal se tudo continuar nulo? | ⚪★ | decisão |
| 96 | Qual orçamento você aceita perder, e que meta além do prêmio máximo faria sentido? | ⚪★ | decisão sua |
| 97 | Quais perguntas ainda não pensamos? (revisão periódica por mim e pelo auditor) | ⚪ |  |
| 98 | Que dados novos poderíamos coletar (ordem, local, arrecadação) para testar mais? | ⚪ |  |
| 99 | O que mudaria nossa conclusão? (qual evidência bastaria para virar a mesa) | ⚪★ | critério de refutação |
| 100 | Estamos medindo o que importa (acertos intermediários) ou o que o dinheiro paga? | 🟡 | cobertura ≠ retorno |

