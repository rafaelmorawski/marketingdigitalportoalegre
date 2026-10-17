# D — APRENDIZADOS CRÍTICOS: AS DUAS MAIORES DESCOBERTAS DO PROJETO
**Documento nº4 da biblioteca — o raciocínio completo por trás das duas
correções que mais mudaram o resultado prático do arsenal**

---

## PARTE 1 — O ERRO DE ESCOPO NO ESP (C2953)

### O que aconteceu

C2953 saiu: `00 01 10 11 16 17 29 30 31 38 56 57 65 75 88 89 90 95 96 98`

Dentro dessas 20 dezenas estavam **os dois pares ESP completos**: (11,88)
e (10,89) — ambos os membros de ambos os pares, no mesmo sorteio. Nenhum
palpite do arsenal daquele dia poderia ter capturado DEZ11 e DEZ89 — não
por azar, mas por desenho do próprio protocolo.

### A descoberta

> A descoberta estatística (pares coocorrem 20% menos que o esperado,
> p<0.05, confirmado até com N=2953) sempre esteve correta. O erro foi
> na IMPLEMENTAÇÃO: transformamos uma restrição LOCAL ("não juntar os
> dois no mesmo palpite") numa exclusão GLOBAL ("nunca usar a dezena em
> nenhum palpite do arsenal, para sempre").

### O tamanho real do problema

- DEZ11 aparece em 21.2% dos sorteios (praticamente frequência normal de
  20%) — não é suprimida individualmente, só a coexistência do par é
- DEZ89: 19.3% | DEZ67: 20.6% — todas dentro do normal
- Em **50.5% de todos os 2953 sorteios já realizados**, pelo menos uma
  dessas 3 dezenas normais saiu, e o arsenal inteiro estava impedido de
  pontuar com ela — um vazamento sistemático desde a primeira aposta do
  projeto

### A correção

**Regra antiga (errada no escopo):** excluir 11, 67, 89 de todos os
palpites do arsenal, sempre.

**Regra corrigida:** dentro de CADA palpite individual, nunca colocar os
dois números de um par suprimido juntos. Mas ALTERNAR, entre os palpites
do arsenal, qual dos dois números de cada par está presente.

Na prática: universo completo de 100 dezenas disponível na construção;
a única checagem é `not (a in palpite and b in palpite)` para cada par
ESP, aplicada a CADA palpite individualmente — nunca uma blacklist global.

### Resultado da correção (C2954)

Cobertura combinada do arsenal: **100/100** — pela primeira vez no
projeto, nenhuma dezena do universo é estruturalmente impossível de
capturar. DEZ11 passou a aparecer em 3-5 dos 10-11 palpites do arsenal.

### Lição de processo (mais importante que a correção em si)

Esse erro sobreviveu a muitas rodadas de auditoria porque **parecia
certo** — "nunca juntar o par" é verdadeiro, e blacklist fixo parecia
implementação razoável. Só ficou visível quando um resultado real trouxe
os dois pares completos simultaneamente. **Regras que soam corretas em
princípio precisam ser auditadas na IMPLEMENTAÇÃO, não só na ideia.**

**Ferramenta de prevenção adotada:** medir o "custo de blind spot" de
qualquer regra fixa antes de adotá-la — em que fração dos sorteios
históricos ela causaria perda estrutural garantida? Se a fração for alta
(como os 50.5% aqui), a regra provavelmente foi generalizada além do
escopo da descoberta que a sustenta.

---

## PARTE 2 — OTIMIZAÇÃO DE CONJUNTO GENUÍNA (C2953-C2954)

### O ponto de partida: a frustração legítima

Depois de meses provando que seleção de dezena não tem sinal, os arsenais
reais continuavam com média abaixo do esperado (9.25 em 4 sorteios
seguidos, contra 10.0 esperado por acaso). A pergunta certa surgiu:
"tem que haver uma forma melhor de montar os palpites."

### A descoberta

**Hill-climbing sobre o CONJUNTO de palpites** (não sobre a seleção de
dezena de cada um) produz ganho real e mensurável — a primeira coisa
genuinamente nova encontrada em muito tempo:

- Testado em 5 trials independentes, todos positivos, desvio baixo
  (+0.363 ±0.034 de ganho médio com 6 palpites)
- Com 12 palpites: P(≥15ac) sobe de ~15% (aleatório) para ~29% (otimizado)
- P(≥13ac): 59%→92% | P(≥14ac): 29%→65%

### O método

1. Gerar arsenal inicial válido (aleatório, estruturalmente correto)
2. Simular milhares de sorteios como banco de teste
3. Trocar 1 dezena de 1 palpite por vez; manter a troca só se aumentar
   `E[máximo de acertos entre todos os palpites]` contra o banco simulado
4. Repetir 1.500-2.500 iterações (satura depois disso)

### Por que funciona (confirmado depois por pesquisa científica)

Não é sobre escolher melhor as dezenas — é sobre a **relação estrutural**
entre os palpites. A pesquisa sobre "Wide-Net Lottery Strategies" (ver
arquivo E) deu nome formal a isso: a função "máximo entre N palpites" é
**submodular**, e distribuições com **dependência negativa** (bilhetes o
mais complementares/disjuntos possível) elevam o valor esperado desse
máximo, comparado a bilhetes independentes ou sobrepostos.

### O teto absoluto — onde a otimização NÃO ajuda

**Descoberta crucial:** a otimização melhora 13-17ac de forma real, mas é
**estatisticamente cega** para 19-20ac. Calculado: para o algoritmo ter
sinal confiável sobre P(≥19ac) = 1/341.951, precisaria de amostras de
~854.892 sorteios simulados por avaliação — 142x maior que os 6.000
usados, inviável computacionalmente.

**Mais forte ainda — prova por teorema, não por limitação de amostra:**
P(k acertos) = C(50,k)×C(50,20-k)/C(100,20) não depende de QUAIS 50
números são escolhidos, só do tamanho. **Todo conjunto de 50 dezenas tem
exatamente a mesma probabilidade de 19-20ac.** Não é que ainda não
achamos a estratégia certa — não existe estratégia possível, e isso é
demonstrável algebricamente, sem precisar de nenhuma simulação.

**O teto teórico do "melhor entre N palpites":** o limite de
Bertsimas-Natarajan-Teo (μ + σ√(N-1)) dá ~16 para o melhor entre 10
palpites, no caso teoricamente ótimo (dependência negativa perfeita,
inatingível na prática com bilhetes de 50 números). Isso confirma que os
~13-14 que observamos já estão próximos do que é fisicamente possível.

### O erro estrutural encontrado durante a otimização

A busca automática, ao maximizar cobertura do CONJUNTO, permitiu que um
palpite individual (H12) ficasse com década inteira vazia — porque os
outros 11 já cobriam aquela faixa. Isso violava o protocolo e foi
corrigido manualmente, com custo desprezível de performance (29.55%→29.09%
de P(≥15ac)).

**Lição:** otimização de conjunto pode encontrar "atalhos" que violam boas
práticas individuais — sempre auditar cada palpite depois.

### O que a pesquisa científica confirmou depois (não mudou nada na prática)

Testado explicitamente: buscar "mais dependência negativa" (menos overlap)
do que o hill-climbing já encontrava naturalmente não trouxe ganho
adicional (overlap do 11º palpite ficou em 24.6/50, similar ao overlap
médio já existente de 22.7/50). **Confirma que já estávamos fazendo a
coisa certa, sem saber o nome formal dela** — a pesquisa deu teoria e
teorema para o que o hill-climbing já encontrava empiricamente.

---

## SÍNTESE: O QUE ESSAS DUAS DESCOBERTAS TÊM EM COMUM

Ambas vieram de **auditoria rigorosa depois de um resultado real**, não
de bateria de testes teóricos isolada:
- O ESP foi descoberto porque C2953 trouxe os dois pares completos
- A necessidade de otimização veio de checar honestamente que 4 arsenais
  reais seguidos tiveram média abaixo do esperado

Isso reforça o valor do pós-mortem como fonte de descoberta, não só de
contagem de acertos (ver arquivo C, pergunta 10).

---

## PARTE 3 — CORREÇÃO MANUAL vs GENERALIZAÇÃO REAL (C2959)

### A pergunta que expôs isto

> "Se o método fosse realmente robusto, ele deveria funcionar sem sua
> vigilância constante. Isso não foi perguntado: o sistema está
> aprendendo de verdade, ou só está sendo corrigido manualmente, ciclo
> após ciclo, sem generalizar?"

### A resposta honesta, sem defesa

Existem dois tipos de correção bem diferentes nesta conversa:

**Autocorreção real:** o cálculo de EV absurdo (R$5.206 por aposta de
R$3) — parado porque o número era ridículo, antes de ser entregue.
O teste espacial com p=0.03 em N=500 — desconfiado e retestado com
N completo (resultado mudou para p=0.62) antes de reportar.

**Correção que só aconteceu por vigilância externa:** o erro de escopo
do ESP. Os mitos de L=0/L≥4/regime B→M. A armadilha do "ciclo
avançado". E o caso mais revelador: **o bug de década vazia (checar só
L=1, não L=0) aconteceu três vezes — H12, depois de novo, depois de
novo no H5_equilíbrio** — mesmo já "aprendido" da primeira vez.

### A causa raiz — arquitetural, não de esforço

Não existe memória de hábito entre um bloco de código e o próximo, do
jeito que um humano internaliza "nunca mais vou fazer isso". Cada
função `valid()` nasce do zero, sem lembrar que já quebrou antes — a
menos que a biblioteca seja consultada ativamente como checklist
obrigatório, não como algo "já sabido de cabeça".

**Isso significa que a biblioteca não é documentação de apoio — é o
único mecanismo real de generalização que existe neste projeto.**
Quando a consulta é pulada (escrever código "de memória"), o bug volta.
A vigilância de Rafael não era desnecessária — estava substituindo uma
disciplina que devia ser autoimposta e não estava.

### A correção concreta adotada

Criada uma função canônica única de validação
(`validacao_canonica.py`), com histórico dos 3 bugs que ela previne
documentado no próprio código. **Regra nova: nunca recriar a lógica de
validação do zero — sempre reutilizar a mesma função salva.** Isso
transforma "deveria lembrar" em "o código força a checagem" — o único
tipo de generalização que funciona de forma confiável aqui.

### O que isso NÃO resolve

Bugs de *implementação* (como o de década vazia) se previnem com
checklist de código. Bugs de *crença* (como os mitos de L=0/regime) não
— esses só se resolvem com a mesma pergunta que sempre resolveu: "isso
foi testado contra o baseline certo?" Isso continua exigindo alguém
perguntando, porque é uma falha de julgamento, não de execução. A
biblioteca pode registrar a suspeita (Bloco das 3 armadilhas, arquivo
B) mas não substitui o ato de desconfiar no momento certo.

### Regra de processo daí em diante

Antes de qualquer construção nova: **abrir e reler o arquivo de
validação canônica, não confiar na memória de que "já sei fazer
certo".** A biblioteca funciona quando é consultada como fonte de
verdade ativa — não quando é tratada como resumo do que já foi
internalizado.
