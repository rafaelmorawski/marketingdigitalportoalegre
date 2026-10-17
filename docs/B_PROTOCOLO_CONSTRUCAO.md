# B — PROTOCOLO DE CONSTRUÇÃO E AUDITORIA DE PALPITES
**Documento nº2 da biblioteca — checklist operacional**
**Atualizado com a correção do erro de escopo ESP e o método de otimização de conjunto**

---

## FILOSOFIA

Este protocolo existe para uma coisa só: **não nos atrapalharmos**. Cada
etapa corresponde a um erro real já cometido e corrigido neste projeto.
Seguir o protocolo não garante acertos — garante que não desperdiçamos
apostas em falhas estruturais já conhecidas.

Se qualquer etapa contradisser um dado novo e validado, **o dado vence**.
Nada aqui é imutável — exceto a matemática pura (identidades de conjuntos,
teoremas de probabilidade).

---

## ETAPA 0 — LER A BIBLIOTECA ANTES DE COMEÇAR

- [ ] **Arquivo A (Framework Vivo)** — leis do sistema, hipóteses refutadas
- [ ] **Arquivo E (Biblioteca Científica)** — para não repetir perguntas já pesquisadas
- [ ] **Pós-mortem dos últimos 3-5 sorteios** — padrão real recente, não só o teórico

**Erro que evita:** redescobrir algo que o walk-forward já refutou.

---

## ETAPA 1 — PÓS-MORTEM COMPLETO DO ÚLTIMO RESULTADO

- [ ] Soma, regime (B/M/A), delta vs sorteio anterior
- [ ] L-vector completo, décadas vazias e com L≥4
- [ ] Repetições do sorteio anterior
- [ ] Baixas vs Altas, temperatura (frias/mornas/quentes)
- [ ] **Verificar pares ESP no resultado real** — ambos os membros de algum
  par saíram juntos? Isso é dado real sobre a validade da regra, não só
  auditoria de acerto
- [ ] Acertos de CADA palpite do arsenal — não só o melhor
- [ ] Blind spots reais — dezenas ausentes de TODO o arsenal (deve ser
  zero desde a correção do ESP; se não for zero, há erro novo a investigar)

**Erro que evita:** avaliar só o vencedor e ignorar o resto do arsenal.

---

## ETAPA 1.5 — VERIFICAR CONDIÇÃO "DNA REPLICADO" (⚠️ REBAIXADO — ver nota)

**⚠️ Status revisado:** validado apenas 1 vez (N=520/514, uma única
análise histórica) + 2 observações ao vivo sem confirmação estatística
formal. Nosso próprio critério de falseabilidade (arquivo B, seção
final) exige 3+ validações independentes para qualquer efeito
condicional. DNA replicado NÃO atinge esse padrão ainda — deve ser
tratado como **hipótese em observação**, não regra ativa automática.

- [ ] Contar repetições entre os DOIS últimos sorteios (não o pós-mortem
  do resultado mais recente — é sorteio-1 vs sorteio-2 antes do atual)
- [ ] **≥6 repetições:** registrar a condição, mas NÃO dar peso
  automático na construção até termos mais confirmações independentes
  (+1.28ac medido, N=520 — promissor, não confirmado)
- [ ] **3-5 repetições:** neutro, não priorizar nem evitar
- [ ] **≤2 repetições:** registrar, mas com a mesma cautela acima
  (-1.37ac medido, N=514 — promissor, não confirmado)
- [ ] Tratar cada nova observação como ponto de dados rumo às 3
  confirmações independentes necessárias — não como regra já provada

---

## ETAPA 2 — ATUALIZAR ESTADO MACRO (30 sorteios) E MICRO (3-5 sorteios)

- [ ] Recalcular frias/mornas/quentes atuais (muda a cada sorteio)
- [ ] Comportamento recente pode contradizer a média histórica — registrar
  ambas as leituras se houver ambiguidade real (ex: "Globo evita frias"
  vs "Globo vai compensar")
- [ ] Jejum por linha, vácuo por dezena, posição no ciclo das 100 dezenas

---

## ETAPA 3 — SINAIS ESTRUTURAIS ATIVOS (restrição, nunca ranking de dezena)

- [ ] L=0 no último sorteio → garantir presença mínima na linha (não
  escolher QUAIS dezenas por score)
- [ ] L≥4 no último sorteio → não concentrar peso extra nessa linha
- [ ] Regime atual → orientar faixa de soma do palpite, nunca >60% de certeza
- [ ] Lembrar: 2 eventos extremos seguidos NÃO aumentam pressão de
  correção além de 1 evento isolado (testado, p=0.38)

**Erro que evita:** usar sinais estruturais para escolher dezenas
específicas — isso já foi refutado com N=2888.

---

## ETAPA 4 — DECIDIR QUANTOS PALPITES

- [ ] Checar orçamento
- [ ] Com otimização de conjunto genuína: ganho real até ~12-15 palpites
  (diferente do antigo teto heurístico de 10-11)
- [ ] Calcular o custo/benefício marginal antes de decidir (ex: 12→15
  ainda vale, mas rende menos por palpite que 6→10)

---

## ETAPA 5 — CONSTRUÇÃO: MÉTODO ATUAL (otimização de conjunto)

### Regra de universo — CORRIGIDA (não usar a versão antiga)

- [ ] **Universo completo disponível: 100 dezenas.** NUNCA banir 11, 67,
  89 permanentemente do arsenal inteiro — esse era o erro de escopo
  corrigido em C2953/C2954.
- [ ] Restrição ESP aplicada **apenas dentro de cada palpite individual**:
  nunca (11,88), (32,67) ou (10,89) juntos NO MESMO palpite. Diferentes
  palpites do arsenal podem e devem alternar qual dos dois números de
  cada par incluem.

### Checklist técnico obrigatório, por palpite

- [ ] Todas as 10 décadas presentes (nunca 0, a menos que hipótese
  explícita testada)
- [ ] Nunca L=1 em nenhuma linha (mínimo 2)
- [ ] Nenhuma linha com >8 dezenas
- [ ] ESP respeitado dentro do palpite (ver acima)
- [ ] Tamanho exato: 50 dezenas
- [ ] Registrar a razão/hipótese do palpite antes de construir

### Método de otimização (substituiu a heurística "5 por linha + diversidade")

1. Gerar arsenal inicial válido (aleatório, corrigido para estrutura)
2. Simular milhares de sorteios (5.000-8.000) como banco de teste
3. Hill-climbing: trocar 1 dezena por vez em 1 palpite, manter a troca
   só se aumentar **E[máximo de acertos entre todos os palpites]**
   contra o banco de sorteios simulados
4. Repetir por 1.500-2.500 iterações (satura depois disso)
5. **Auditar CADA palpite individualmente após a otimização** — ela pode
   sacrificar estrutura individual (já aconteceu: década inteira vazia
   num palpite porque os outros compensavam) — corrigir manualmente

### Ao adicionar palpites a um arsenal já existente

- [ ] NUNCA otimizar os novos isoladamente — otimizar junto com os já
  existentes (fixos), avaliando sempre o CONJUNTO completo
- [ ] Isso garante que os novos genuinamente complementam os existentes,
  não apenas coexistem

**Erro que evita:** os dois erros estruturais mais caros do projeto —
décadas vazias (V1/V3, e depois H12 pós-otimização) e o banimento
permanente de dezenas normais (ESP mal implementado).

---

## ETAPA 5.5 — REOTIMIZAÇÃO CONJUNTA PERIÓDICA (pendente para C2959→C2960)

**Descoberta de C2959:** construir palpites sequencialmente (travar os já
existentes, otimizar só o mais novo) é sub-ótimo. Testado: reotimizar
TODOS os palpites do arsenal simultaneamente (deixar qualquer um mudar,
não só o mais recente) rendeu +0.186 de ganho sobre 10 palpites já
construídos — maior que o ganho de adicionar mais um palpite isolado
nas últimas rodadas (0.104, 0.086, 0.066).

**Ação pendente, a fazer na próxima sessão, ANTES de gerar qualquer
palpite novo:**
1. Pegar o arsenal atual completo (10 palpites de C2959)
2. Rodar hill-climbing permitindo QUALQUER um dos 10 mudar (não só
   adicionar um 11º travando os outros)
3. Comparar score antes/depois — já confirmado que o ganho é real
4. Só depois de reotimizar os existentes, decidir se vale adicionar
   mais um palpite novo, ou se o arsenal atual já está no melhor
   arranjo possível para o tamanho que tem

**Por que isso vira regra permanente:** a cada bloco de ~5-10 palpites
adicionados sequencialmente, vale parar e reotimizar o conjunto inteiro
antes de continuar — não só empilhar.

---

## ETAPA 6 — DIVERSIDADE ENTRE PALPITES

- [ ] Calcular overlap entre TODOS os pares (nunca só verificar visualmente)
- [ ] Faixa observada como próxima do ótimo: **22-27/50** — confirmada
  tanto empiricamente (Monte Carlo) quanto teoricamente (submodularidade
  + dependência negativa, ver arquivo E)
- [ ] Não forçar overlap artificialmente mais baixo que isso — a teoria
  mostra que não há vantagem adicional em ir além
- [ ] Palpites "híbridos"/"consenso" tendem a ter overlap alto com os
  que os originaram — não contar como diversidade real
- [ ] **Auditoria de redundância explícita:** antes de finalizar o
  arsenal, perguntar de cada palpite "esta é uma hipótese genuinamente
  diferente, ou é uma variação disfarçada de outra já presente?" —
  palpites com lógica de construção diferente mas resultado quase
  idêntico (overlap muito alto) devem ser tratados como 1 hipótese, não 2

---

## ETAPA 7 — PARES COMPLEMENTARES

- [ ] Considerar o complemento exato de um palpite forte como par
- [ ] Garantia matemática: ac(P1) + ac(complemento) = 20 SEMPRE
- [ ] Corrigir ESP no complemento (inversão pura pode reintroduzir
  violação dentro do próprio complemento)
- [ ] Validar estrutura do complemento como qualquer outro palpite

---

## ETAPA 8 — SINAL DE ZERO ACERTOS (P_ZERO) — ⚠️ REBAIXADO PARA OBSERVAÇÃO

Checklist original — os 4 simultâneos:
- [ ] Soma extrema (>1200 ou <750)
- [ ] Repetições ≥6 do sorteio anterior
- [ ] Ciclo avançado (>20 sorteios sem fechar)
- [ ] ≥5 dezenas muito quentes concentradas

**⚠️ REFUTADO PARA SINAIS PARCIAIS — não construir com 2/4 ou 3/4.**
Testado com N=156 casos reais: lógica de reversão de baixas extremas
teve resultado PIOR que baseline (p=0.016). Testadas mais 5 variações
(continuação, frias extremas, exclusão exata, paridade oposta, décadas
vazias como base) — todas neutras ou piores. Zero acertos nunca ocorreu
em nenhum teste (esperado: 1 em 11.372.635).

**A condição completa (4/4 simultâneos) nunca ocorreu no histórico —
é hipótese NÃO TESTADA, construída de peças já refutadas individualmente
em combinações parciais. Isso muda o que fazer se ela ocorrer:**

**Regra corrigida — se 4/4 surgir: TRATAR COMO TESTE, nunca como ação
validada.** Registrar o evento, opcionalmente reservar uma fração
simbólica do orçamento para observar — nunca comprometer o arsenal
principal com base numa hipótese que nunca foi confirmada, mesmo que
"pareça razoável" ela funcionar. Essa é exatamente a armadilha nº2
(falácia do apostador) se tratada como certeza.

---

## ETAPA 9 — REGISTRAR EXPECTATIVA ANTES DO RESULTADO

- [ ] Anotar expectativa realista antes de saber o resultado
- [ ] Não prometer que um método específico "vai ganhar"
- [ ] Separar avaliação do PROCESSO (diversidade, estrutura, cobertura)
  da avaliação do RESULTADO (acertos)

**Erro que evita:** viés de "resulting" — tratar o palpite que teve
sorte como se tivesse método superior.

---

## ETAPA 10 — PÓS-APOSTA

- [ ] Listar todos os palpites numerados, prontos para conferência
- [ ] Confirmar cobertura combinada (deve ser 100/100 desde a correção ESP)
- [ ] Confirmar custo total
- [ ] Guardar a versão final, não o rascunho

---

## O QUE ESTE PROTOCOLO NÃO É

- Não é garantia de acerto — nenhuma etapa muda a probabilidade de
  qualquer dezena específica sair
- Não é regra imutável — dado novo testado com rigor sempre vence
- Não substitui julgamento do momento

---

## AS TRÊS ARMADILHAS ESTATÍSTICAS JÁ MAPEADAS (verificar sempre)

Antes de aceitar qualquer resultado "forte" (p muito baixo), checar se
ele não é uma destas três ilusões — todas já nos enganaram uma vez:

**1. Lei dos Grandes Números Verdadeiros** (olhar em muitos lugares até
achar por acaso) — ex: "L9 parece anômala" só porque, entre 10 décadas
observadas o tempo todo, sempre alguma vai parecer anômala (confirmado:
20.4% das janelas de 30 sorteios mostram isso em ALGUMA década).

**2. Falácia do apostador** (achar que o passado empurra o futuro) —
ex: décadas vazias "devendo" retornar, reversão de padrão extremo —
todas testadas e refutadas (p=0.016 a p=0.98).

**3. Confusão entre definição e descoberta** (a variável testada está
matematicamente amarrada ao resultado pela própria forma como foi
construída, não por comportamento real) — ex: testar "quantas dezenas
nunca vistas aparecem" quando o ciclo já está avançado é tautológico:
com poucas dezenas restantes por ver, MATEMATICAMENTE sobra pouco
espaço para "novas" aparecerem, gerando p=0.0000 que não significa
nada sobre o sorteio, só sobre a aritmética da própria pergunta.

**4. Confusão entre possibilidade retrospectiva e previsibilidade
prospectiva** — achar que, porque um resultado "caberia" dentro de um
palpite (o que é quase sempre matematicamente verdade), isso significa
que havia um caminho de raciocínio válido que deveríamos ter seguido
para prevê-lo. Prova: qualquer palpite de 50 dezenas contém
C(50,20) ≈ 47 trilhões de conjuntos possíveis de 20 — praticamente
qualquer resultado razoável "caberia" nele. Isso não é evidência de
que erramos o raciocínio; é a aritmética inevitável de escolher 50 de
100. A pergunta certa nunca é "isso poderia ter cabido", é "havia
informação disponível ANTES do sorteio que apontasse para esse
resultado específico, entre os 47 trilhões possíveis, e não outro?"

**Regra de verificação:** se um resultado tem p extremo (<0.001) e
"parece bom demais", perguntar: a variável testada poderia, pela sua
própria definição matemática, estar mecanicamente ligada ao resultado,
independente de qualquer comportamento real do sorteio?

---

## CRITÉRIOS DE FALSEABILIDADE — O QUE PROVARIA O FRAMEWORK ERRADO

Uma tese só é científica se especificarmos, ANTES de olhar novos dados,
o que a derrubaria. Isso evita aceitar só confirmações e ignorar
contradições — o viés que mais ameaça um framework depois de muito
tempo sendo validado repetidamente.

**Tese central do projeto:** "Seleção de dezena individual não tem
sinal; só a relação estrutural entre múltiplos palpites (otimização de
conjunto) tem efeito real."

### O que provaria isso errado — critérios específicos, não vagos

**1. Top-20 estável entre janelas independentes.** Já testado 1 vez:
overlap 2/20 (menor que o acaso, 4/20). Falsificaria: repetir esse
teste em 5+ pares de janelas diferentes e encontrar overlap
CONSISTENTEMENTE acima de 4/20, com significância.

**2. Sinal condicional que se replica em dados novos.** DNA replicado
validado 1 vez (N=520/514). Falsificaria mais o framework: encontrar
3+ efeitos condicionais INDEPENDENTES, cada um sobrevivendo correção
para múltiplos testes, e cada um se confirmando quando testado contra
sorteios que ainda nem existiam quando descobertos.

**3. Teste de uniformidade falhando, especificado ANTES de olhar.** Já
rodados ~8 testes qui-quadrado (frequência, décadas, colunas, pares,
dobradas, quadrantes, distância espacial) — todos uniformes.
Falsificaria: escolher uma nova partição dos 100 números ANTES de ver
os dados, testar, e achar não-uniformidade com p<0.01.

**4. Auditoria física do equipamento.** Evidência direta (não
estatística) de viés mecânico real — como os casos históricos de
roleta viciada (Jagger, García-Pelayo). Seria causal, não inferido.

**5. Performance real do arsenal acima do previsto, de forma
sustentada.** Arsenais otimizados preveem média teórica ~13-14 (melhor
de N palpites). Falsificaria (ou revelaria algo a mais): média real
ficar significativamente acima disso por 50+ sorteios seguidos.

### O que NÃO conta como evidência (guarda contra se enganar)

- Um resultado bom isolado (12-14ac) — já é a variância normal
- p<0.05 sem correção para múltiplos testes na mesma sessão
- Um padrão "que parece fazer sentido" sem ter sido testado ANTES de
  ser observado
- Comparar só com o baseline errado (já enganou 3 vezes: L=0, L≥4,
  regime B→M)

### O que uma falseamento REAL significaria, na prática (esclarecimento)

Se o critério 3 (nova partição, p<0.01) ocorresse: isso **não
derrubaria o framework inteiro** — derrubaria só a suposição de
uniformidade daquela partição específica. O passo seguinte correto
seria: (1) verificar se é viés real, p-hacking, ou estrutura genuína
não capturada antes; (2) exigir replicação em dados novos antes de
qualquer ação; (3) só then considerar se isso abre uma nova via de
seleção de dezena — nunca agir sobre uma única observação, mesmo
extrema, sem o mesmo rigor de walk-forward que aplicamos a tudo mais.

---

## MELHORIA CONTÍNUA

1. Testar hipóteses novas sempre em walk-forward antes de confiar —
   nunca validar por N=1
2. Revisitar este protocolo a cada 10-15 sorteios
3. Nunca deixar o protocolo virar engessamento — acomodar hipóteses
   novas e interessantes, não bloqueá-las
4. Cada novo relatório de pesquisa deve ser escaneado por "o que muda
   no protocolo", não só arquivado
5. **Medir o "custo de blind spot" de qualquer regra fixa antes de
   adotá-la** — a lição do erro ESP: calcular em que fração dos sorteios
   históricos a regra causaria perda estrutural garantida
