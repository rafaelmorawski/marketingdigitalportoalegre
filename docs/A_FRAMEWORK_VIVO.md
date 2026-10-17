# A — FRAMEWORK VIVO C294X — LOTOMANIA
**Documento nº1 da biblioteca — leia este primeiro, sempre**
**Estado consolidado até C2954 | Histórico validado: 2954 sorteios**

---

## COMO USAR ESTA BIBLIOTECA (ordem de leitura)

- **A (este arquivo):** o que sabemos — leis confirmadas, hipóteses refutadas, método de construção atual
- **B — Protocolo de Construção:** checklist passo a passo para gerar/auditar qualquer arsenal
- **C — Perguntas que Movem o Método:** perguntas-gatilho para destravar avanço quando a sessão travar em "só gerar palpite"
- **D — Aprendizados Críticos:** as duas maiores descobertas do projeto (erro de escopo ESP + otimização de conjunto), com todo o raciocínio e prova
- **E — Biblioteca Científica (resumo):** referência condensada dos 5 relatórios de pesquisa profunda already feitos

---

## O ACHADO CENTRAL — NUNCA ESQUECER

> **Existem duas camadas distintas em qualquer loteria: as LEIS DO SISTEMA
> (nível do espaço de resultados — imutáveis, comprováveis com N grande) e a
> SELEÇÃO DE DEZENA INDIVIDUAL (qual número específico sai — genuinamente
> aleatória). Nenhum critério de seleção de dezena testado supera o acaso.**

Confirmado via walk-forward em N=2888+ sorteios reais, testando dezenas de
métodos (frequência, vácuo, momentum, fase rítmica, harmonia musical,
insistência em linha, reversão de padrão, paridade oposta, décadas vazias,
entropia máxima multi-dimensional, "20 convicção + 30 cobertura"). **Todos
empataram com aleatório ou foram piores.**

O que MOVE o resultado não é escolher melhor as dezenas — é a **relação
estrutural entre múltiplos palpites** (diversidade, otimização de conjunto,
pares complementares, cobertura sem furo).

---

## BLOCO 1 — LEIS DO SISTEMA (imutáveis até prova em contrário)

| Lei | Valor | N | Status |
|---|---|---|---|
| P(20ac) por ticket | 1/11.372.635 | matemática | imutável |
| P(≥15ac) por ticket | 1/88 | matemática | imutável |
| P(≥19ac) por ticket | 1/341.951 | matemática | imutável — idêntico para QUALQUER conjunto de 50 dezenas (teorema, não estimativa) |
| L=0 nunca 3× seguida na mesma linha | lei histórica | 2954 | absoluta até hoje |
| Sorteios com ≥1 década vazia | 67.7% | 2948 | estável |
| Sorteios com 2+ décadas vazias | 18.7% | 2948 | estável |
| Sorteios sem nenhuma década vazia | 32.3% | 2948 | estável |
| Soma média | 988 | 2948 | std=118 |
| Regime B / M / A | 23% / 54% / 23% | 2948 | estável |
| Transição B→M | 59% | histórico | estável |
| Repetição de dezena entre sorteios consecutivos | 20.08% | 2948 | = ao acaso puro |
| Zeros uniformes entre linhas/colunas | Chi²=8.37/6.24, p>0.4 | 2948 | sem viés |
| Pares ESP coocorrem 20% menos que esperado | lift ~0.80x, p<0.05 | 2953 | válido — mas ver Bloco 5 sobre a IMPLEMENTAÇÃO correta |
| ac(P1) + ac(complemento) = 20 | identidade de conjuntos | sempre | garantia matemática, não estatística |
| Diversidade entre palpites (overlap 18-27/50) | triplica ≥15ac | p<0.0001 | alavanca clássica confirmada |
| **Otimização de conjunto (hill-climbing) supera diversidade heurística** | dobra P(≥15ac): ~15%→~29% com 12 palpites | testado N=5 trials | **alavanca mais forte já validada — ver Bloco 5** |

---

## BLOCO 2 — CATÁLOGO COMPLETO DE HIPÓTESES REFUTADAS (não retestar)

| Hipótese testada | Resultado | Significância |
|---|---|---|
| Frequência alta (baseline) vs baixa (inverso) | empate | p=0.56 |
| Palpite fixo nunca atualizado | empate | p=0.76 |
| Musical (fase rítmica + harmonia) | PIOR | p<0.0001 |
| Momentum década (20 vs 30 sorteios) | PIOR | p<0.0001 |
| Aleatório puro vs qualquer critério | empata ou vence | p=0.65 |
| Insistir numa linha até ela zerar | empate | p=0.82 |
| Simetria "5 por linha" forçada vs distribuição natural | empate (direção negativa não sig.) | p=0.078 |
| Reversão de padrão extremo (baixas→altas) | PIOR — falácia do apostador | p=0.016 |
| Continuação de padrão (oposto da reversão) | empate | não sig. |
| Décadas vazias do sorteio anterior como base do próximo | empate/levemente pior | não sig. |
| Máxima entropia multi-dimensional (décadas+paridade+finais+soma) | empate | p=0.63 |
| "20 de convicção + 30 de cobertura" (mesmo com cobertura estrutural) | empate | p=0.79 |
| "Top 20 dezenas" por qualquer critério — teste de estabilidade entre janelas | overlap entre janelas independentes ≤ acaso puro | prova definitiva: não existe top-20 real |
| P_ZERO com sinais parciais (2/4) — reversão de baixas extremas | PIOR que baseline | p=0.016, N=156 |
| P_ZERO — 5 variações adicionais (continuação, frias extremas, exclusão exata, paridade oposta) | todas neutras | não sig. |

**Padrão geral:** qualquer hipótese que assuma "memória" do sorteio
anterior influenciando o próximo falha, porque sorteios são i.i.d.
(confirmado cientificamente — ver arquivo E).

### O único caso de efeito condicional real (não geral) já encontrado

**"DNA replicado"** (carregar dezenas ativas dos 2 últimos sorteios): empata
no agregado (p=0.27), MAS tem condição real:
- Se ≥6 repetições entre os 2 sorteios anteriores: +1.28ac vs baseline (N=520)
- Se 3-5 repetições: neutro
- Se ≤2 repetições: **-1.37ac vs baseline** (N=514) — evitar nessa faixa

---

## BLOCO 3 — MÉTODO DE CONSTRUÇÃO ATUAL (substituiu o método v3 anterior)

### O que MUDOU desde a v3

A v3 recomendava "5 por década + diversidade heurística (overlap 18-27)"
como método de construção. **Isso foi superado por otimização de conjunto
real (hill-climbing)**, que produz ganho mensurável adicional — ver Bloco
5 e arquivo D para prova completa.

### Receita de construção atual (a mais forte já validada)

1. **Universo completo disponível** (100 dezenas) — NUNCA banir 11, 67, 89
   permanentemente (erro de escopo corrigido, ver Bloco 5)
2. Validade de CADA palpite individual: 50 dezenas exatas, nenhuma década
   vazia, nenhuma com L=1, nunca os dois números de um par ESP juntos
   NESSE palpite específico
3. Gerar arsenal inicial (aleatório válido) e otimizar via hill-climbing:
   trocar 1 dezena por vez, mantendo só trocas que aumentam E[máximo de
   acertos entre todos os palpites] contra milhares de sorteios simulados
4. Auditar estrutura de CADA palpite após a otimização — ela pode
   encontrar "atalhos" que violam boas práticas individuais (já
   aconteceu: um palpite ficou com década inteira vazia porque os outros
   compensavam) — sempre corrigir manualmente se necessário
5. Overlap resultante esperado: ~22-27/50 entre pares — não forçar mais
   baixo que isso; a teoria (submodularidade + dependência negativa)
   confirma que esse é aproximadamente o ponto ótimo, não um mínimo a
   perseguir

### Tamanho de arsenal recomendado

Ganho real e mensurável até ~12-15 palpites (com otimização genuína,
diferente da heurística antiga que saturava em 10-11). Depois de 12, o
ganho marginal cai de ~2-2.7pp/palpite para ~0.5pp/palpite — mas ainda
positivo até ~15.

### O teto absoluto — nunca prometer além disso

Para 13-17ac: ganho real e mensurável via otimização.
Para 19-20ac: **nenhuma técnica de construção muda a probabilidade** —
é teorema, não limitação de busca. P(≥19ac) = 1/341.951 para QUALQUER
conjunto de 50 dezenas, sempre. O que muda com mais palpites é só a
chance de que ALGUM dos N acerte esse extremo (10 palpites → 1/34.196).

---

## BLOCO 4 — SINAIS ESTRUTURAIS: REVISADO (⚠️ CORREÇÃO IMPORTANTE)

**⚠️ REFUTADO EM C2956 — "L=0 retorna 90-91%" e "L≥4 descomprime 87-90%"
NUNCA foram sinais reais.** Testado com walk-forward completo (N=2746 e
N=3224 casos reais) contra o baseline correto (taxa de qualquer década
ter presença/ausência, independente do estado anterior):

- L=0 retorna: observado 91.2% vs baseline 90.7% — diferença não
  significativa (p=0.37)
- L≥4 descomprime: observado 88.3% vs baseline 89.1% — diferença não
  significativa (p=0.17)

**Causa raiz, matemática pura sem precisar de histórico:** P(uma década
específica ter presença ≥1 em qualquer sorteio, sempre) = 90.5% via
hipergeométrica. P(<4) = 89.0%. Esses valores batem quase exatamente com
os "sinais" — porque são a MESMA coisa. Não existe retorno nem
descompressão condicionada ao estado anterior; é a probabilidade basal
de qualquer década, sempre, por décadas terem 10 números cada de um
universo de 100 com 20 sorteados.

**Por que isso sobreviveu tanto tempo sem ser pego:** os números
"pareciam" bater (90-91%, 87-90%), e nunca foram testados contra o
baseline CERTO (qualquer década, qualquer sorteio) — só usados como se
fossem verdade desde o início do projeto. Isso é o mesmo padrão do erro
ESP: uma regra que soa correta nunca foi auditada na implementação.

**Uso corrigido:** décadas devem continuar tendo presença mínima em
QUALQUER palpite (isso é regra estrutural válida, sempre — nunca década
vazia). Mas NÃO existe justificativa para dar peso extra a uma década
específica achando que ela "vai retornar mais" só por ter zerado no
sorteio anterior — isso ela faria de qualquer forma, sempre, com ou sem
ter zerado antes.

| Sinal (revisado) | Status |
|---|---|
| L=0 no sorteio anterior → presença no próximo | ❌ REFUTADO — é baseline (90.5%), não efeito real |
| L≥4 no sorteio anterior → <4 no próximo | ❌ REFUTADO — é baseline (89.0%), não efeito real |
| Regime B→M 59% | Ainda válido — não testado com esse erro específico |
| 2 eventos extremos seguidos NÃO aumentam pressão de correção | Ainda válido, testado corretamente (p=0.38) |

---

## BLOCO 5 — A CORREÇÃO MAIS CARA DO PROJETO: ERRO DE ESCOPO NO ESP

**Resumo (detalhe completo no arquivo D):** a regra estatística "pares
(11,88), (32,67), (10,89) coocorrem 20% menos" está correta e validada.
Mas a implementação antiga (banir 11, 67, 89 de TODOS os palpites, para
sempre) generalizou incorretamente uma restrição LOCAL (não juntar os
dois no mesmo palpite) para uma exclusão GLOBAL (nunca usar a dezena em
lugar nenhum).

**Custo medido:** 50.5% de todos os 2953 sorteios já realizados tinham
pelo menos uma dessas 3 dezenas normais (frequência ~20%, nada suprimida
individualmente), e o arsenal inteiro — não importa quantos palpites —
estava impedido de pontuar com ela.

**Correção ativa desde C2954:** universo completo disponível (100
dezenas), restrição ESP aplicada apenas DENTRO de cada palpite
individual. Cobertura combinada do arsenal agora chega a 100/100.

---

## BLOCO 6 — HISTÓRICO DE PERFORMANCE (resultados reais, não simulados)

| Sorteio | Melhor resultado | Lição principal |
|---|---|---|
| C2945-2947 | 14-15ac | Zeros aleatórios, complemento > sinal específico |
| C2948 | 13ac | Palpite vencedor anterior (H6, 15ac) caiu para 4ac — nenhuma hipótese se sustenta |
| C2949 | 13ac (P_COMPENSA) | Leitura oposta (compensação) bateu leitura de continuação (antifria) |
| C2950 | 13ac (H4_MORNAS) | — |
| C2951 | 13ac | **3 décadas zeraram simultaneamente** — resultado raro, ninguém passou de 15 |
| C2952 | 13ac | Média do arsenal abaixo do esperado (8.83 vs 10.0) |
| C2953 | 13ac | **Descoberta do erro de escopo ESP** — DEZ11 e DEZ89 saíram juntas, arsenal inteiro cego para elas por design |
| C2954 | arsenal com ESP corrigido + otimização genuína pela 1ª vez juntos | aguardando resultado |

**Meta-lição:** em nenhum desses sorteios reais qualquer palpite passou
de 15ac. Isso é consistente com a matemática (P(≥15ac)=1/88 por ticket).
Não é falha de método — é a distribuição de probabilidade se manifestando
normalmente.

---

## BLOCO 7 — ESTADO ATUAL (atualizar a cada concurso)

**Último sorteio processado:** C2953
**Resultado:** 00 01 10 11 16 17 29 30 31 38 56 57 65 75 88 89 90 95 96 98
**Achado do dia:** os dois pares ESP completos (11+88, 10+89) saíram juntos
— evento que expôs o erro de escopo do Bloco 5.

**Arsenal ativo para C2954:** 11 palpites, ESP corrigido, otimização de
conjunto real, cobertura 100/100. Ganho teórico: dobra P(≥15ac) vs
arsenal aleatório do mesmo tamanho.

**Pendências de walk-forward:**
- Testar a condição completa dos 4 sinais de P_ZERO quando ocorrer pela
  primeira vez no histórico (nunca vista ainda)
- Avaliar se otimização pura vs otimização+peso de frequência histórica
  faz diferença (hipótese aberta, correlação atual r=-0.136 — quase nula)
