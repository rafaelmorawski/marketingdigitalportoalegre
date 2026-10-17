# CLAUDE.md — Laboratório Lotomania do Rafael

Leia este arquivo inteiro antes de qualquer ação. Ele reúne tudo que já sabemos, tudo que já foi feito e a missão deste projeto. A pasta `docs/` tem a biblioteca completa (A a I); o documento **I** é o mais recente e o resumo mais denso do que foi validado e refutado.

---

## 1. QUEM E COMO TRABALHAR

- **Usuário:** Rafael, brasileiro. **Escreva sempre em português.**
- **Estilo pedido por ele:** trabalhar com autonomia (planejar, executar, testar, corrigir) com o mínimo de ida e volta, mas sempre **honesto**. Ele valora rigor estatístico e enquadra o projeto como um desafio intelectual adversarial. Ele cria hipóteses próprias (a espiral é dele) e quer que sejam testadas, não elogiadas.
- **Formato:** respostas diretas, tabelas quando comparam, listas de jogos em blocos de código para copiar. Dezenas sempre com dois dígitos (00 a 99).
- **O propósito dele:** ele disse que tem um propósito difícil de conseguir e que ganhar o prêmio máximo faz parte dele. Trate isso com cuidado e sem alimentar a esperança de ganho (ver seção 3). Lembre, de vez em quando e sem sermão, que o gasto deve caber num limite que ele aceite perder; se ele parecer pressionado financeiramente, ofereça ajuda para pensar outros caminhos.

---

## 2. A MISSÃO

**Declarada pelo Rafael:** encontrar uma combinação de dezenas que leve aos **20 acertos** (e, como meta mais próxima, **19 ou mais**) da Lotomania, usando matemática e ciência de dados.

**Missão técnica deste projeto (o que você deve desenvolver):**
1. **Manter e evoluir um laboratório rigoroso, automatizado e honesto** para a Lotomania: ingestão de resultados, conferência por grupo, ledger acumulado, atualização do ciclo, simulação e auditoria de grades.
2. **Procurar, de forma falsificável, qualquer desvio estatisticamente válido** do sorteio uniforme. Isso inclui rodar o painel de predição (`lab/painel_predicao.py`) a cada resultado e propor novos testes pré-registrados.
3. **Construir grades de jogos como estruturas de cobertura**, sempre medidas contra controles aleatórios, e nunca vendidas como previsão.
4. **Registrar tudo** (resultados, grupos, refutações, armadilhas) para que nada precise ser redescoberto.

**Regra inegociável:** nenhuma afirmação de "vantagem preditiva" sem passar no protocolo da seção 6 (fora da amostra, controle embaralhado, correção para vários testes e replicação). Se nada passar, **o relatório honesto é "sem sinal"**, e isso é um bom resultado, não uma falha. Nunca fabrique, infle ou reinterprete resultados para agradar. Se o Rafael pedir para "provar que consegue o resultado", diga o que os dados mostram: hoje a prova disponível é o contrário (ver 4.11 do documento I).

---

## 3. O QUE A MATEMÁTICA JÁ DEIXOU CLARO (leia antes de propor qualquer coisa)

- Lotomania: o apostador marca 50 dezenas entre 00 e 99; saem 20. Pagam 20, 19, 18, 17, 16, 15 e **0 acertos**. Aposta de R$ 3,00 por jogo.
- Chance por bilhete, **igual para qualquer conjunto de 50 dezenas**: 20 acertos = 1 em 11.372.636 (igual à de 0 acerto, por simetria: o espelho de um jogo que faz 20 faz 0); 19 ou mais = 1 em 341.951; 15 ou mais = 1,142%; exatamente 14 = 2,781%; 13 = 6,61%; 12 = 12,16%. Média de acertos 10,00, desvio 2,01.
- **A chance de N jogos distintos de ter pelo menos um 20 é N x 1/11.372.636** (menos colisões desprezíveis). A de 19+ é N x 1/341.951 menos a colisão por sobreposição. **O único lever real é o número de bilhetes distintos.** Nosso conjunto de 19+ está a 0,00077% do teto; o melhor desenho possível ganharia 0,0007%.
- **Score de cobertura não é retorno.** Cada bilhete é pago pelos próprios acertos, então o retorno esperado de N jogos é N x o de um bilhete (≈ R$ 1,12 com prêmios médios; ≈ R$ 0,61 sem o jackpot; ≈ R$ 1,53 com o acumulado de R$ 10,47 mi). E[max], P(≥15) e afins medem só a chance de **ver** 15+; não aumentam o retorno. Igualar o preço exigiria acumulado ≈ R$ 30 mi (nunca ocorreu nos últimos 600 concursos).
- Prêmios médios por ganhador (últimos 300 concursos): 15 ac R$ 10; 16 R$ 44; 17 R$ 263; 18 R$ 2.445; 19 R$ 77.491; 20 R$ 5,75 mi; zero R$ 130.728. Devolução global ≈ 33% do arrecadado.
- Sorteio por sorteio, as dezenas são independentes; o sorteio uniforme prevê com precisão os limites do histórico (ver tabela 4.9 do documento I).

---

## 4. O QUE JÁ SABEMOS (resumo; detalhes e números em `docs/I_ATUALIZACAO_BIBLIOTECA_C2988.md`)

**Nenhuma regra de seleção de dezenas prevê o sorteio, em nenhuma escala.** Testado e refutado, não retestar sem hipótese nova pré-registrada:
- Frequência, quentes/frias/atrasadas (janelas de 3 a 300 sorteios), ciclo (faltantes saem 19,93% vs 20,00%), repetidas do sorteio anterior (20,07%), paridade, décadas, geometria do volante, distância entre sorteios, correlação entre linhas, "dezenas que escaparam do melhor jogo", dia da semana, deriva no tempo.
- Dependência entre sorteios próximos (lags 1 a 10: maior |z| 2,35, limiar 2,81) e agrupamento em janelas curtas (sobredispersão 1,000–1,004).
- **ML forte** (gradiente boosting e regressão logística, 28 variáveis por dezena, treino C300–C1999, teste C2000–C2986): AUC 0,4992 e 0,4988; top-50 = 9,990 e 9,997 acertos (esperado 10,000); **controle com rótulos embaralhados rende o mesmo** (AUC 0,4986; 9,970).
- Retroteste de 103 palpites x 2.986 sorteios: máximo 19 (uma vez, C2827), nenhum 20; tudo dentro do esperado pelo acaso. Monte Carlo de 7 milhões de sorteios contra 20 jogos: 11 sorteios com 20 acertos (esperado 12,3).

**O que as construções de grade rendem (sempre medido contra 30–60 controles aleatórios):**
- Complementaridade entre jogos (baixa sobreposição, cobrir a região de falha): ≈ +0,1 em E[max] e +0,5 pp em P(≥15) sobre jogos aleatórios; o prêmio de "qualidade" de um jogo extra ficou em +0,04 a +0,11 pp; o resto do ganho é ser mais um jogo (≈ +0,9 a +1,0 pp de P(≥15) cada).
- **Paridade do bilhete não importa** (25/25, 38/12, 12/38: mesma distribuição). Grades polarizadas são piores (E[max] 12,72 vs 13,06).
- **30 dezenas fixas + 20 girando custam cobertura** (sobreposição 30–40 entre os jogos do grupo): 5 jogos assim somam ~+4,25 pp contra +4,98 pp de 5 aleatórios.
- Região de falha (melhor jogo ≤12 ou <15) é difusa; as dezenas mais presentes nela são as **menos cobertas** (correlação −0,98), e o ciclo e as repetidas não a explicam.
- Jogos feitos sobre dois "resultados imaginários", sobre 100 sorteios simulados, "proibidos" sem regras ou por "consenso" dos jogos: iguais a um aleatório ou piores.
- **Popularidade:** a estrutura do sorteio prevê o número de ganhadores (correlação fora da amostra 0,41; R² 0,11). Um bilhete "impopular" otimizado soma ≈ R$ 0,05 de retorno esperado por concurso (U1). Pequeno demais para mudar decisão.

**Ciclo:** iniciado no C2978. Comprimento médio histórico 24,4 sorteios (122 ciclos; uniforme 24,0). Fechamento do atual: mediana ~14 sorteios a partir do C2987.

---

## 5. O QUE JÁ FOI FEITO (jogos, grupos e decisões)

A estratégia central é a **espiral de núcleo rígido do Rafael** (grupo J). Regra dele: núcleo de 20 dezenas (2 por década, par adjacente) que anda 2 casas à direita dentro da década a cada jogo (período 5; cada dezena em 2 núcleos; núcleos consecutivos disjuntos); apoio de 30 com 4 a 7 repetidas do último sorteio, dezenas pendentes do ciclo e zonas de atraso; **nunca repete dezenas do núcleo anterior** (efeito "armadilha": se o núcleo k acerta 0–2, o jogo k+1 faz em média 11,45 acertos); entre jogos consecutivos pelo menos 20 dezenas diferentes. Núcleo do J1: `00 01 12 13 24 25 37 38 46 47 54 55 67 68 78 79 83 84 92 93`. Os J1–J10 foram feitos com os dados do C2986 e **ficam fixos** (decisão dele). Refazer a espiral com ciclo/repetidas novos rende o mesmo (E[max] 13,15 vs 13,18).

**Grade apostada para o C2988 (24 jogos, em `data/jogos_C2988.json`, com a razão de cada grupo):**
J (espiral, 10), F (cobertura da falha, 5), U1 (impopular), E1 (edge das três lentes), Y1 (do Rafael), H1 (hill-climbing sobre o conjunto), Z1 e Z2 (trazidos pelo Rafael), N1 (baixa sobreposição para 19+), CA e CB (consenso). Custo R$ 72 por concurso; chance de 20 acertos 1 em 476.282 por sorteio; 19+ 1 em 14.362; simulado E[max] 13,89, P(≥15) 24,1%.

**Histórico de apostas:** ele apostou grades de 20 a 30 jogos nos concursos recentes; o C2987 (14/10/2026: `07 12 20 29 31 32 39 43 44 48 50 52 60 61 69 84 85 90 91 99`) teve melhor placar 14 (J7), média ~10,1. **Nunca houve 20 acertos.** Melhor já visto nos jogos reais: 15–16.

**Decisões dele a respeitar:** quer acompanhar **cada grupo separado** a cada resultado; quer manter os J fixos; gosta da lógica da espiral; quer que se pense em "construções com uma razão de existir". Ele aceita que "só a sorte ganha".

**Pendências:** (1) conferir o C2988 e os seguintes (grupo a grupo) e atualizar ledger e ciclo; (2) rodar o painel de predição a cada resultado; (3) testar a previsão de popularidade quando a planilha de ganhadores estiver completa; (4) acompanhar o acumulado (só vale ajustar gasto quando o retorno esperado se aproximar do preço).

---

## 6. PROTOCOLO DE RIGOR (obrigatório)

1. **Controle aleatório sempre.** Compare cada grade/jogo com 30–60 aleatórios do mesmo tamanho e reporte a **faixa**, não só a média. `lab/ferramentas.py: comparar_com_aleatorios`.
2. **Fora da amostra.** Três bancos de sorteios separados: construção, seleção (escolher o melhor candidato) e teste final. Nunca avaliar no banco em que se otimizou. Sementes diferentes ao reproduzir.
3. **Hipótese antes do dado.** Defina a regra, a métrica, as janelas e o número de testes **antes**; corrija por Bonferroni (ex.: 14 testes → |z| > 2,91). Um z alto isolado, entre muitos testes, é esperado por acaso.
4. **Replicar.** Um desvio só conta se se repetir em janelas diferentes e em dados novos.
5. **Distinguir comparação de grades:** ~170 sorteios para dois erros-padrão (diferença esperada +0,32, desvio por sorteio 2,07). Um sorteio isolado não compara estratégias.
6. **Validar jogos:** 50 dezenas distintas, mínimo de 2 por década (convenção interna, não regra da Caixa). Espelhos e complementos **sempre por código** (`range(100)` menos o jogo), nunca à mão.
7. **Reportar nulos.** "Sem sinal" é resultado válido. Não esconder testes que falharam.
8. **Não otimizar métrica errada:** coverage score não é dinheiro (seção 3).

**Armadilhas já cometidas** (listas completas em `docs/B_PROTOCOLO_CONSTRUCAO.md` e na seção 6 do documento I): tautologia temporal; espelho transcrito à mão; escala incompatível; retroteste de regra fixa que "ajusta" nada; extrapolação do otimizador fora do domínio observado; sorteio-testemunha não é região explorável; ajuste a poucos sorteios (100 simulados) rende como aleatório fora deles; premissa "todos os 100 sorteios ficam abaixo de 15" é falsa; ler "buraco" numa amostra pequena; confundir cobertura com retorno; restringir sinais conhecidos não ganha nada.

---

## 7. FLUXO QUANDO O RESULTADO DO PRÓXIMO SORTEIO CHEGAR

1. `python3 lab/conferir.py --concurso <n> --dezenas "<20 dezenas>" --data dd/mm/aaaa` → confere os jogos por grupo (melhor, média, acertos por jogo), atualiza o ciclo e as repetidas, grava `data/ledger_grupos.csv` e `relatorios/C<n>.md`, e acrescenta o sorteio a `data/extras.csv`.
2. `python3 lab/painel_predicao.py --csv data/Lotomania.csv --extras-file data/extras.csv --log data/painel_log.csv` → roda o teste de predição fora da amostra e registra a linha.
3. Responder ao Rafael com a tabela por grupo, o ciclo e (se for o caso) o veredito do painel. **Sem inventar tendência** a partir de um sorteio. Só propor mudar jogos se houver razão medida.
4. A cada ~20 sorteios, resumir o ledger por grupo (esperado: média 10,0 por jogo e melhor de um grupo de 10 ≈ 13,2) e dizer se já dá para distinguir grupos (~170 sorteios).

Se a planilha da Caixa for atualizada (`data/Lotomania.csv`), os concursos que já estiverem nela têm prioridade sobre `extras.csv`.

---

## 8. ESTRUTURA DO REPOSITÓRIO

```
CLAUDE.md                 este arquivo
README.md                 uso rápido
requirements.txt          numpy, scipy, scikit-learn
data/
  Lotomania.csv           planilha da Caixa até o C2986 (colunas: Concurso, Data Sorteio, Bola1..Bola20, ganhadores e rateios)
  extras.csv              sorteios depois do fim da planilha (concurso,data,dezenas) — já tem o C2987
  jogos_C2988.json        os 24 jogos, grupos e razões
  ledger_grupos.csv       melhor e média por grupo e concurso (semeado com o C2987)
docs/                     biblioteca A–I (I = mais recente)
lab/
  dados.py                carga do histórico e estado do ciclo
  ferramentas.py          simulação uniforme, avaliação de grade, comparação com aleatórios, chances exatas, auditoria
  conferir.py             conferência por grupo + ledger + relatório
  painel_predicao.py      teste de predição fora da amostra (boosting, logística, controle)
relatorios/               relatórios de conferência por concurso
```

Antes de alterar scripts: rode-os, confira que reproduzem os números de referência (painel: AUC 0,4992 / 0,4988 / controle 0,4986; conferência do C2987: grupo J melhor 14, média 9,90).

---

## 9. IDEIAS QUE AINDA VALEM O TEMPO (sempre sob o protocolo)

- Painel de predição rodando em todo resultado, com o log servindo como detector de qualquer mudança futura no sorteio.
- Teste do modelo de popularidade com a planilha de ganhadores completa (C2984–C2987 e depois).
- Acompanhar o acumulado e o retorno esperado por concurso (alerta quando se aproximar do preço).
- Extensão do ledger para o teste J (fixo) contra espiral refeita a cada sorteio (comparação só a partir de ~170 sorteios).
- Outras loterias do Rafael (Lotofácil, Quina, Mega-Sena, Dupla Sena, Dia de Sorte) só se ele pedir; a mesma regra de honestidade vale.

**Não vale o tempo:** novos modelos "mais poderosos" sem hipótese nova (o resultado já é conhecido), regras de dezenas quentes/frias, paridade, ciclo como previsão, "construções" sobre resultados imaginários.

---

## 10. RESSALVA FINAL

Tudo que este projeto mostra de "ganho" é **cobertura em sorteios simulados uniformes** e **estatística descritiva do histórico**. Nada prevê o próximo sorteio. A chance de 20 acertos permanece 1 em 11.372.636 por bilhete. O valor do projeto é reduzir erros de construção, medir honestamente, registrar o que foi testado e não se convencer de padrão onde só existe acaso.
