# E — BIBLIOTECA CIENTÍFICA (RESUMO DE REFERÊNCIA)
**Documento nº5 da biblioteca — condensado dos 5 relatórios de pesquisa profunda**
**Consultar antes de testar qualquer hipótese nova — pode já estar respondida aqui**

---

## COMO USAR ESTE ARQUIVO

Cada seção resume um relatório completo (originalmente 20-32K caracteres
cada). Este resumo existe para consulta rápida — se uma pergunta específica
não estiver clara aqui, os relatórios completos continuam disponíveis
como artifacts desta conversa para aprofundamento.

---

## 1. MACHINE LEARNING E ANÁLISE PREDITIVA APLICADOS À LOTOMANIA

**Conclusão central:** nenhuma técnica de ML aumenta a probabilidade de
acertar dezenas — cada sorteio é i.i.d. (independente e identicamente
distribuído). Testado empiricamente: rede neural na Loto alemã 6/49 fez
0,7359 acertos/sorteio vs 0,7352 do acaso puro — diferença desprezível
("uma galinha bicando números é tão confiável quanto um modelo complexo").

**Probabilidades oficiais Lotomania (Caixa):**
20ac=1/11.372.635 | 19ac=1/352.551 | 18ac=1/24.235 | 17ac=1/2.776 |
16ac=1/472 | 15ac=1/112

**Por que ML falha aqui:** gradient descent precisa de sinal para
minimizar — em dados aleatórios, a perda de validação não decresce de
forma generalizável, só memoriza ruído. Markov de ordem superior não
ajuda (pressupõe que o futuro depende do estado atual, falso para
sorteios independentes). LSTMs aprendem padrões sequenciais que não
existem em sorteios. Testes de aleatoriedade (qui-quadrado, NIST) em
loterias reais (Lotto 6/49 canadense, N=1798) confirmam: "a hipótese de
equidistribuição não pode ser rejeitada... sugerindo que o mecanismo de
sorteio é justo."

**O único ganho real e legítimo:** covering designs / fechamentos
(wheeling) — garantem prêmios menores condicionais a acertar um mínimo
de dezenas dentro do pool escolhido. É matemática de cobertura, não de
previsão.

**Teorema fundamental:** No Free Lunch — nenhum algoritmo supera busca
aleatória sem viés indutivo aplicável a estrutura real dos dados. Como a
Lotomania não tem estrutura explorável, não há "almoço grátis" possível.

---

## 2. A FRONTEIRA CIENTÍFICA REAL DAS LOTERIAS

**O que a ciência permite:**
1. **Covering designs** com limite de Schönheim — otimização combinatória
   para garantir prêmios menores com mínimo de bilhetes (não muda EV do
   jackpot)
2. **Seleção de combinações impopulares** — reduz probabilidade de dividir
   o prêmio SE ganhar (a única assimetria real: pessoas evitam certos
   padrões ao escolher números, o sorteio não)
3. **Janelas raras de EV positivo** (roll-downs) — dimensionadas via
   critério de Kelly. Caso real: sindicato do MIT no Cash WinFall
   (Massachusetts), 2005-2012, ~US$40mi apostados, ~US$3,5mi de lucro,
   **só nos rolldowns**, nunca por seleção de número. Investigado e
   considerado legal (sem irregularidade).

**O que a ciência proíbe:** prever números específicos. Testes formais de
aleatoriedade em loterias reais (Lotto 6/49 canadense N=1798, UK National
Lottery N=2065, loteria romena N=2706) confirmam consistentemente
uniformidade — sem viés explorável.

**Vieses físicos são reais mas raros e historicamente datados:** roleta
enviesada de Jagger (Monte Carlo, 1881) e García-Pelayo (anos 1990) —
ambos exploraram equipamento mecânico imperfeito, não sorte estatística.
Loterias modernas de bolas são auditadas e certificadas (NIST SP 800-22).

**Teorema de parada opcional (martingale):** prova matematicamente que
nenhuma estratégia de timing (insistir, dobrar aposta, esperar padrão)
transforma um jogo de EV negativo em positivo. Fundamenta por que
"insistir até aparecer" (pergunta 3 do arquivo C) sempre falha.

**Apofenia e "lei dos grandes números verdadeiros":** em qualquer base de
dados grande o suficiente, coincidências aparentemente notáveis são
matematicamente garantidas de acontecer, sem significar nada. Isso
explica por que "padrões" sempre parecem existir quando se olha
retrospectivamente para dados aleatórios.

---

## 3. FERRAMENTAS AVANÇADAS DE CIÊNCIA DE DADOS (rigor analítico geral)

**Foco:** prevenção de p-hacking e "data dredging" — o inimigo real em
grandes bases históricas não é falta de método, é excesso de tentativas.

**Deflated Sharpe Ratio / False Strategy Theorem:** quanto mais hipóteses
testadas numa base fixa, mais garantido que uma delas parece boa por
acaso. Fórmula do teorema: o Sharpe máximo esperado in-sample CRESCE com
o número de tentativas independentes N — não importa se a estratégia
tem skill real ou zero.

**Aplicação direta ao projeto:** sempre perguntar "quantas hipóteses
diferentes já testei hoje?" antes de confiar num resultado "significativo".
Considerar limiar mais exigente que p<0.05 quando testando muitas
hipóteses na mesma sessão (correção Bonferroni ou False Discovery Rate).

**Validação cruzada purgada (Purged K-Fold / CPCV):** para dados
temporais/dependentes, k-fold padrão vaza informação. Sempre usar
walk-forward (treino sempre precede teste cronologicamente).

**Teoria da informação como teste de sinal:** informação mútua e entropia
condicional dão um teste agnóstico de domínio — se a informação mútua
entre uma feature e o alvo não é distinguível de zero sob permutação, não
há relação a explorar, e nenhum modelo criará sinal onde não existe.

**Conformal prediction:** framework que dá garantias de cobertura de
amostra finita para qualquer modelo, sem assumir distribuição — útil para
quantificar incerteza honestamente quando há dados limitados.

---

## 4. FERRAMENTAS GERAIS DE RACIOCÍNIO E DECISÃO ITERATIVA

**Multi-armed bandits:** framework formal de decisão sob incerteza com
feedback repetido. Equilibrar exploração (testar hipóteses incertas) com
explotação (usar o que já sabe funcionar) — orçar exploração
explicitamente, reduzir conforme evidência se acumula.

**Superforecasting (Tetlock/Good Judgment Project):** treinamento
probabilístico melhora precisão em 6-12%/ano; o pacote completo de
métodos (treino+times+agregação estatística) supera controle em >50%.
Hábitos dos melhores previsores: decompor questões (Fermi), começar pela
taxa-base (visão externa) antes da interna, atualizar em pequenos
incrementos, granularidade probabilística.

**Distinção aleatória vs. epistêmica:** incerteza aleatória é
variabilidade irredutível do processo gerador (ex: qual dezena sai);
incerteza epistêmica é ignorância redutível com mais dados. Reconhecer
qual domina informa a decisão — alta incerteza aleatória (como na
Lotomania) sinaliza que buscar mais sinal é fútil.

**Apofenia / ilusão de agrupamento:** o erro central de tratar ruído como
sinal. Dados aleatórios verdadeiros parecem MENOS aleatórios do que se
espera intuitivamente (produzem clusters) — respeitar essa "irregularidade
natural" é a defesa.

**Robust Decision Making (RDM):** quando distribuições de probabilidade
são desconhecíveis, abandonar otimização preditiva e testar decisões
candidatas contra muitos cenários plausíveis, buscando robustez, não
otimalidade para um único futuro previsto.

**Separar decisão de resultado (Annie Duke):** julgar a qualidade de uma
decisão pelo resultado isolado é o erro de "resulting" — uma boa decisão
pode ter mau resultado por azar. Avaliar o processo, não só o desfecho.
Diretamente formalizado na Etapa 9 do protocolo (arquivo B).

---

## 5. WIDE-NET LOTTERY STRATEGIES (rede ampla, cobertura vs. agrupamento)

**A pergunta que originou a pesquisa:** existe alguma técnica que quebre
o teto matemático de "melhor entre N palpites"?

**Resposta central:** o objetivo correto não é "cobrir o universo" nem
"agrupar os sorteados" — é **maximizar E[máximo de acertos entre N
palpites]**, e isso é alcançado via **dependência negativa** (bilhetes o
mais complementares/disjuntos possível). A função "máximo" é
**submodular**; correlações positivas (overlap alto) só diminuem esse
valor esperado.

**O teto teórico duro:** limite de Bertsimas-Natarajan-Teo,
E[máximo] ≤ μ + σ√(N-1). Para 10 palpites (μ=10, σ≈2,01): teto ≈16
acertos — mas exige estrutura de "um único bilhete vencedor por sorteio",
inatingível com bilhetes de 50 números. Nosso resultado real (~13-14) já
está próximo do fisicamente possível.

**Nenhum algoritmo faz melhor que o guloso submodular** (garantia
(1-1/e)≈63% do ótimo, comprovadamente o melhor possível em tempo
polinomial — Feige 1998). Nosso hill-climbing já está na vizinhança
desse limite prático.

**Sindicatos profissionais reais não usam agrupamento superior — usam
economia:** Moffitt-Ziemba (2018) formalizam que a estratégia ótima de
sindicato é "trump ticket" (apostar em uma de cada combinação), e o
sindicato do MIT visava exclusivamente rolldowns (estrutura de prêmio),
nunca seleção de número.

**Confirmação prática:** testamos explicitamente buscar mais dependência
negativa (menos overlap) do que o hill-climbing já encontrava — sem
ganho adicional. Já estávamos na fronteira prática correta antes mesmo
de conhecer a teoria formal.

**Nada disponível (2023-2026) — annealing quântico, DPPs, novos limites
de covering — quebra esse teto.** É consequência de teoremas (No Free
Lunch + submodularidade), não de ferramenta insuficiente.

---

## SÍNTESE TRANSVERSAL DOS 5 RELATÓRIOS

Todos convergem para a mesma conclusão central por caminhos diferentes:

1. **Seleção de dezena individual:** sem sinal, comprovado por ML (1),
   teoria de aleatoriedade (2), e teoria da informação (3)
2. **A única alavanca real é estrutural:** cobertura/dependência negativa
   entre múltiplos bilhetes (1 e 5), nunca escolha de número
3. **O rigor do PROCESSO é onde a inteligência realmente ajuda:**
   prevenção de p-hacking (3), calibração e decisão sob incerteza (4)
4. **Os limites são teoremas, não falta de esforço:** No Free Lunch (1),
   parada opcional/martingale (2), Bertsimas-Natarajan-Teo (5) — três
   provas matemáticas independentes do mesmo teto fundamental

---

## 6. AUDITORIA FÍSICA REAL DA LOTOMANIA (C2960 — categoria nova de investigação)

**Por que isso é diferente de tudo acima:** os 5 relatórios anteriores
são estatística sobre os RESULTADOS. Esta seção é sobre o MECANISMO
FÍSICO que gera os resultados — o único tipo de evidência que o nosso
próprio critério de falseabilidade #4 (arquivo B) classifica como
causal, não inferida. Nunca tínhamos verificado isso especificamente
para Lotomania — só assumíamos por analogia com loterias em geral.

**Mecanismo confirmado (Regulamento oficial CAIXA):** Lotomania usa
**1 globo único**, carregado com 100 bolas numeradas de 00 a 99. A cada
sorteio, a bola sorteada retorna ao globo antes do próximo número ser
sorteado — mecanismo de reposição com re-sorteio em caso de repetição
dentro do mesmo concurso.

**Auditoria dupla e real, não simbólica:**
- Auditores populares (escolhidos da plateia presente) acompanham a
  abertura das maletas lacradas, a conferência do lacre com o relatório
  do sorteio anterior, a colocação das bolas no suporte, e a confirmação
  final dos números sorteados
- Funcionários da Secretaria de Acompanhamento Econômico do Ministério
  da Fazenda (SEAE) e da Controladoria-Geral da União (CGU) também podem
  acompanhar os sorteios
- Transmissão ao vivo pelo YouTube da Caixa, com plateia presencial
  aberta ao público sem necessidade de agendamento

**Controle físico das bolas:**
- Cada conjunto de bolinhas é pesado, numerado e conferido
  individualmente antes de cada sorteio
- Fabricadas por empresa francesa especializada (mesma fornecedora de
  sorteios na França e Suíça), em borracha maciça
- Analisadas pelo Inmetro (instituto de metrologia)

**O que isso confirma:** não encontramos nenhuma brecha ou irregularidade
documentada — pelo contrário, encontramos evidência direta de controle
de peso individual das bolas (o tipo de controle que, se ausente,
permitiu os vieses históricos reais de roleta — Jagger 1881,
García-Pelayo anos 1990) e dupla auditoria independente. Isso não
enfraquece o framework — fortalece a mesma conclusão que já tínhamos,
agora com evidência causal direta, não só inferência estatística.

**Teste complementar — desgaste progressivo das bolas gera drift?**
Hipótese testável a partir do achado acima: se bolas se desgastassem
fisicamente ao longo do tempo (mudando peso/tamanho gradualmente),
isso deveria aparecer como TENDÊNCIA LINEAR na frequência de dezenas
específicas ao longo de blocos sequenciais do histórico — diferente de
ruído aleatório sem direção.

Testado: histórico completo (2957 sorteios) dividido em 10 blocos
sequenciais, regressão linear da frequência de cada dezena ao longo
dos blocos. Resultado: apenas 1 dezena (67) mostrou tendência
significativa (p<0.01) — exatamente o esperado por PURO ACASO ao
testar 100 dezenas nesse limiar (~1 falso positivo esperado). **Sem
evidência de desgaste sistemático.** Consistente com o controle de
peso pré-sorteio documentado acima — se uma bola degradasse, o
protocolo de pesagem individual antes de cada sorteio deveria
substituí-la antes de causar viés duradouro.

**Fonte:** Regulamento oficial dos sorteios, Portal Loterias CAIXA
(caixa.gov.br/loterias/regras-sorteio), consultado em 2026.
