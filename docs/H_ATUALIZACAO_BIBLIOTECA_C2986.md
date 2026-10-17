# H — ATUALIZAÇÃO DA BIBLIOTECA E DO PENSAMENTO
**Documento nº8 da biblioteca — complementa A, B, C, D, E, F, G**
**Processado até C2985 | grade para C2986 definida | histórico: 2985 sorteios**

---

## 1. ESTADO ATUAL

| Concurso | Resultado | Melhor jogo da grade | Média da grade |
|---|---|---|---|
| C2984 | 03 05 06 12 20 22 23 25 26 28 41 53 68 70 73 76 79 82 86 90 | 14 (P18, escolha livre aleatória) | 10,12 (26 jogos) |
| C2985 | 02 03 06 07 10 11 12 13 22 25 29 39 48 53 59 63 66 70 74 79 | 15 (HC2, hill-climbing contra a região de falha) | 9,97 (34 jogos distintos) |

- **Ciclo (iniciado em C2978):** 83/100 já saíram. **Faltam 17:** 00 01 18 19 35 42 44 46 47 49 51 62 67 83 84 88 93.
- **Grade do C2986:** 20 jogos. C1–C10 = Claude, composição estruturada (8 faltantes, 10 do C2985, 32 outras já sorteadas) com hill-climbing conjunto. G1–G10 = GPT, apoios livres por hill-climbing sequencial contra os C. Simulação (600 mil sorteios uniformes): E[max] 13,78, P(≥15) 21,2%, P(≥16) 4,9%.
- **Os cinco apoios A1–A5 do GPT não foram apostados.**
- **Chance de 20 acertos:** 1 em 11.372.636 por bilhete; com 20 jogos distintos, cerca de 1 em 569 mil. O valor exato por inclusão–exclusão difere da soma simples na sexta casa (1 em 454.908 contra 454.905 para 25 jogos).

---

## 2. O PENSAMENTO ATUALIZADO

1. **A sorte decide qual sorteio sai; o desenho decide quanto dele a grade cobre.** Nenhuma regra de seleção de dezenas testada (ciclo, faltantes, repetidas, temperatura, atrasadas, paridade, jejum de década, geometria do volante) prevê o próximo sorteio.
2. **O score da grade (E[max], P(≥15)) mede cobertura, não chance de 20.** A chance de 20 por bilhete é fixa; só cresce em linha reta com o número de bilhetes distintos.
3. **As alavancas que existem, por tamanho:** (a) mais bilhetes distintos (dominante); (b) desenho complementar com baixa sobreposição (+0,17 no melhor placar médio por dez jogos); (c) evitar redundância (núcleo fixo custa); (d) mirar a região de falha da grade (+0,1 pp por jogo); (e) perfil menos popular (reduz a divisão do prêmio, segunda ordem); (f) aprendizado (jogos como experimentos registrados antes).
4. **O que não é sorte mas é pequeno:** o melhor jogo único possível chega a 87% do teto teórico de ganho (1,142 pp em P(≥15)); um jogo aleatório chega a 79%. A distância é de ~0,09 pp.
5. **"Nada é confiável na loteria; toda hipótese é uma escolha não realizada por opção."** Construímos para testar e registrar, não para prometer.
6. **Padrão de honestidade:** reproduzir toda simulação com sementes diferentes, comparar com 30 controles aleatórios e reportar a faixa deles; nunca confirmar achado de retroteste isolado.

---

## 3. DESCOBERTAS NOVAS (validadas)

### 3.1 Popularidade e divisão do prêmio
- Os ganhadores das faixas de 15 a 18 acertos variam entre sorteios **18 vezes** o ruído de Poisson: os apostadores não escolhem dezenas de forma uniforme. A razão de popularidade = ganhadores observados / (arrecadação ÷ R$3 × P(k acertos)).
- A estrutura do sorteio prevê a popularidade **fora da amostra** (treino nos antigos, teste nos 175 mais recentes): correlação 0,47, R² ≈ 0,19.
- Sorteios com **mais dezenas de 80 a 99** são menos populares (rho −0,162, p = 0,0001); mais concentração em poucas décadas e mais décadas vazias são mais populares. **Datas (≤31) e meses (01–12) não passam:** rho +0,065 (p = 0,12) e +0,050 (p = 0,23).
- Terço menos popular: 16 ganhadores de 20 acertos contra 28 esperados (p = 0,010); mais popular: 37 contra 30.
- Efeito prático: a chance de dividir o prêmio cai de ~14,3% para ~13,2% num jogo inclinado. **Não altera a chance de ganhar.**
- **Armadilha do otimizador:** sem restrição, o jogo menos popular vai a um canto extremo (34 pares, 18 dezenas ≥80) fora do que já foi observado. Exigir que ≥90% dos sorteios possíveis do bilhete fiquem dentro da faixa 1%–99% histórica.
- **Previsão pendente:** o modelo (ajustado até C2983) prevê o C2984 com popularidade 1,093 (percentil 88). Conferir quando a planilha com ganhadores chegar.

### 3.2 Sequências sem ganhador e retorno
- 24,2% dos concursos têm ganhador de 20 acertos (721 de 2983). Recorde de sequência sem ganhador: 18. Sequência de 10 (C2974–C2983) tem ~20% de chance com as vendas atuais: **não é anomalia nem "dívida"**.
- Ganhadores esperados por concurso ≈ 0,15 (arrecadação ÷ R$3 ÷ 11.372.636). Nos últimos 400 concursos: 60,3 esperados, 57 observados.
- **Devolução:** nos últimos 500 concursos os prêmios pagos somaram ~33% do arrecadado. Decomposição do retorno esperado por bilhete de R$3 (últimos 300 concursos, ~R$1,12 somados): 20 acertos R$0,51 (prêmio médio R$5,78 mi); 19 acertos R$0,22; 18 acertos R$0,10; 17, 16 e 15 acertos ~R$0,09 cada; zero acerto R$0,012 (prêmio médio R$130.728, mesma chance que 20 acertos).
- **O desenho da grade não muda o retorno esperado por bilhete.**

### 3.3 Desenho da grade
- **Núcleo fixo custa:** 10 jogos com 20 dezenas fixas: E[max] 12,75 contra 13,06 de dez aleatórios (grade GPT do C2985). Em organizações de 10 jogos: livres 13,065 / espelhos 13,119 / núcleo fixo 12,860 (P(≥15) 10,87% / 10,91% / 10,17%).
- **Cotas de composição custam um pouco:** composição (faltantes, repetidas, outras) com hill-climbing: 13,15; sem composição, mesma otimização: 13,23. Três dezenas ficam fixas em todos os jogos quando só há uma faltante na década.
- **Décadas sem faltante** (C2986: 20–29 e 70–79) impedem "uma faltante por década"; a receita vira 8 faltantes (uma por década com faltante).
- **Espelho:** acertos(jogo) + acertos(espelho) = 20; o melhor do par fica ≥10. P(≥15) do par = 2p exato (eventos disjuntos), contra 1−(1−p)² de dois independentes (diferença 0,013 pp). Para 19 e 20 nada muda.
- **Overlap ótimo depende do tamanho:** par isolado, quanto menor melhor; com ≥7 jogos, faixa 18–27. Média de sobreposição 30 em grade grande é sinal de redundância.
- **Cada jogo extra** soma hoje ~0,8–0,9 pp em P(≥15) (grade de 20 a 33 jogos), qualquer que seja o método; o melhor construído supera o aleatório em ~0,1 pp.

### 3.4 Região de falha da grade
- Com 28 jogos, o melhor jogo fica em ≤12 em 2,93% dos sorteios; com 33, em 1,36%. **Todos os 28 jogos entre 9 e 12:** 0,001% (25 em 2 milhões).
- A falha é **difusa**: cobertura por dezena 11–18 de 28, nenhum par de dezenas sem aparecer junto. Direção: nos sorteios de falha as dezenas menos cobertas aparecem 1,12–1,34× o normal (correlação cobertura × presença −0,87). Não há efeito de década.
- **Resgate medido (jogo extra em sorteios de falha):** adversarial 21,7% chegam a 13+ e 3,6% a 15+, contra 10,4% e 1,1% de aleatório. As 50 dezenas menos cobertas: melhor resgate que aleatório, mas pior efeito geral. Núcleo das 30 mais presentes + 20 distribuídas e "40 mais presentes + 10 menos agrupadas": pior que aleatório (redundantes com a grade).
- Os 10 jogos menos agrupados do conjunto (soma de pares coexistindo 288 contra 368 de um conjunto aleatório) reunidos num jogo: +0,09 pp sobre aleatório.
- **Sorteio-testemunha por programação inteira** (todos os jogos entre 7 e 10): a inclusão obrigatória das 20 dezenas dele (X1) não rendeu mais que um jogo aleatório (+0,037 pp sobre completar o mesmo núcleo ao acaso). Retirar a obrigação das 20 dezenas não custa nada mensurável (z = −0,41).

### 3.5 Teto de um único jogo
- Ganho máximo de um jogo extra em P(≥15) = a chance do próprio jogo chegar a 15+ = **1,142 pp**. Busca pesada (250 mil sorteios de treino, 14 reinícios, seleção em 400 mil, teste em 1,2 milhão): melhor jogo +0,992 pp (87% do teto); 60 aleatórios +0,900 pp em média (máx +0,957).

### 3.6 19 ou mais acertos em dois jogos
- Dois jogos com 19+ juntos exigem sorteio quase todo na interseção deles (forma típica: 18 comuns + 1 de cada, 92,7% dos casos para m = 28). Para os 20 jogos do C2986: pelo menos um com 19+ ≈ 1 em 17.098; pelo menos dois ≈ 1 em 5,4 bilhões (soma exata das 190 duplas). Um sorteio-exemplo que realiza a condição tem a mesma chance de qualquer outro conjunto de 20 dezenas (1 em ~5,4×10²⁰).

---

## 4. REFUTADO OU SEM SINAL (não retestar)

- **Quentes, frias e atrasadas** (regra definida antes, janela de 100 concursos, controle de 150 históricos embaralhados): quentes z = +1,45; frias z = −0,89; mistura 35+15 z = +2,00 (p ≈ 0,053 contra embaralhados) mas **não replica** nas janelas 30 (+0,17) e 300 (−0,32) e **não passa Bonferroni** (12 testes, |z| > 2,64); atrasadas z = +0,66. Mesmo se real, seria +0,07 acerto por concurso.
- **Geometria do volante** (tabuleiro de xadrez e espelho): retroteste em 2985 sorteios deu 67 sorteios com 15+ contra 68,2 esperados; 7 com 17+ contra 2,4 (p ≈ 1% sem correção, não significativo após os seis cortes). Retroteste financeiro (C2484–C2983, R$3 por jogo): prêmios R$1.586 para R$3.000 de custo; percentil 96 de 2.000 pares aleatórios (mediana deles R$225): sorte de amostra.
- **ESP** (pares 11/88, 32/67, 10/89): refutada com z-scores e teste de persistência (ver arquivos A e D).
- **Posição de ciclo, jejum de década, regime, paridade do último sorteio** (r = −0,036, p = 0,048, fraco e contraditório com o teste vizinho): sem sinal.
- **CVaR / otimização de cauda:** não supera E[max] puro; objetivos de cauda (15/16, faixa 13–14, 16+) ficam todos dentro da faixa dos aleatórios.
- **"Mais comuns reúnem as espalhadas":** 40 mais frequentes capturam 8,005 dezenas por sorteio (esperado 8,00), 10 mais fracas 2,007 (esperado 2,00).

---

## 5. ARMADILHAS CATALOGADAS (acréscimo ao arquivo B)

6. **Tautologia temporal (olhar para frente):** um jogo "já saíram" construído depois de C2978–C2980 acerta 20 neles por definição. Testar só contra sorteios posteriores à construção; jogos feitos com pool de ciclo não valem contra os sorteios que formam o pool.
7. **Espelho transcrito à mão:** P16 saiu com 00 e 99 no lugar de 12 e 14. Calcular espelhos sempre por código (`range(100) − jogo`) e conferir overlap 0.
8. **Escala incompatível:** comparar a soma de um bilhete de 50 dezenas com a soma de um sorteio de 20. O z-score resultante não tem sentido.
9. **Retroteste de uma regra fixa não "ajusta" nada:** sorteios independentes; qualquer par espelho produz a mesma distribuição. O sinal só existe se a mesma regra, definida antes, sobrevive a janelas e controles embaralhados.
10. **Extrapolação do otimizador:** otimizar contra um modelo sem restringir ao domínio observado leva a cantos extremos (ver 3.1).
11. **Sorteio-testemunha não é região:** o "buraco" de um conjunto de jogos é um ponto entre ~5×10²⁰; cobri-lo não torna esse sorteio mais provável.
12. **Reprodução de terceiros:** com as mesmas sementes dá número idêntico; com outras, diferenças de centésimos são ruído. Conferir sempre sobreposição, composição e estatísticas declaradas antes de aceitar.

---

## 6. MUDANÇAS NO PROTOCOLO (arquivo B)

- **Etapa 5:** universo completo; ESP não é restrição. Mínimo de 2 dezenas por década é **convenção interna**, não regra da Caixa (não altera a média de acertos; só a variância).
- **Etapa 5.5:** não reotimizar o arsenal inteiro em grades de ~10; adicionar jogo novo por edge/adversarial.
- **Nova etapa de auditoria:** comparar cada jogo novo com **30 jogos aleatórios** (ganho e faixa), e reportar a distância ao teto de 1 jogo.
- **Nova regra de composição:** antes de fixar dezenas em todos os jogos (núcleo) ou cotas (ciclo), medir o custo contra a versão livre. Evitar núcleos de dezenas mais presentes.
- **Para comparar duas estratégias** (ex.: Claude × GPT), registrar por concurso o melhor placar e a média de cada grupo, e a contribuição do grupo de apoio ao melhor dos grupos principais. Um sorteio não distingue as abordagens: diferença esperada +0,32 no melhor placar, desvio por sorteio 2,07, **~170 sorteios** para dois erros-padrão.
- **Experimentos pré-registrados:** o jogo "35 quentes + 15 frias" (últimos 100 concursos C2886–C2985, desempate pelo menor número) fica como teste puro da regra; não misturar com cotas do ciclo.
- **Lean:** não instalado no ambiente; o Lean puro não tem conjuntos finitos nem binomiais (exige Mathlib). Teoremas certificáveis: identidade do espelho, simetria hipergeométrica de P(k acertos) por tamanho de bilhete, limite superior da união. Afirmações empíricas (simulações, modelo de popularidade) não são verificáveis em Lean.

---

## 7. PENDÊNCIAS

1. Conferir C2986 com a tabela por grupo (C, G, melhores, médias).
2. Atualizar ciclo (17 faltantes) e continuar o ledger do jogo quentes/frias (acertos contra 10,00).
3. Quando chegar a planilha com ganhadores de C2984 e C2985, testar a previsão do modelo de popularidade (previsto 1,093 para C2984).
4. Acumular o placar C × G ao longo dos concursos antes de qualquer conclusão sobre estratégias.
5. Se houver nova construção em grade, medir núcleos e cotas contra a versão livre antes de usar.

---

## 8. RESSALVA FINAL, VÁLIDA PARA TUDO ACIMA

Todos os ganhos acima são **cobertura em sorteios simulados uniformes** e **estatística descritiva do histórico**. Nenhum prevê o próximo sorteio. A chance de 20 acertos continua 1 em 11.372.636 por bilhete, e a de qualquer sorteio específico, 1 em 5,36×10²⁰. O valor do método é reduzir erro de construção, medir honestamente e não se convencer de padrão onde só existe acaso.
