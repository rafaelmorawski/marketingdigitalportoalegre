# C — PERGUNTAS QUE MOVEM O MÉTODO
**Documento nº3 da biblioteca — perguntas-gatilho para destravar avanço real**

---

## COMO USAR ESTE DOCUMENTO

Não é uma lista de tarefas — é um catálogo de **perguntas-gatilho**. Quando
a sessão estiver presa em "gerar mais um palpite" sem produzir aprendizado
novo, voltar a uma destas 10 perguntas costuma destravar avanço real de
método, não só mais um ticket de 50 dezenas.

A ordem (princípios → teste de vantagem → auditoria → limites matemáticos
→ fechamento) reflete a sequência que historicamente gerou mais valor —
não é rígida.

---

## BLOCO 1 — ESTABELECER PRINCÍPIOS DE BASE

### 1. "Podemos parar de fazer bloqueios que fazem perder?"
Transforma filtros de exclusão automática em pesos/guias. Vivido com
H1_ESTRUTURAL_PURO (exclusão zerou 3 décadas) e, de forma mais cara, com
o banimento permanente de 11/67/89 no ESP (ver arquivo D).
**Reaplicar quando:** uma regra "nunca incluir X" aparecer — perguntar se
é lei confirmada ou suposição não testada, e se o ESCOPO da restrição
bate com o escopo da descoberta que a origina.

### 2. "Separar a qualidade da decisão da qualidade do resultado"
Impede confundir "H6 fez 15ac" com "H6 é o método certo". Formalizado na
Etapa 9 do protocolo depois que H6 caiu de 15ac para 4ac no sorteio
seguinte.
**Reaplicar:** todo pós-mortem, antes de declarar qualquer palpite
"vencedor" como método superior.

---

## BLOCO 2 — TESTAR SE EXISTE VANTAGEM REAL

### 3. "Buscar insistir num resultado até ele aparecer não pode nos dar vantagem?"
**RESPOSTA OBTIDA (walk-forward N=2889):** testado formalmente — excluir
a linha de maior jejum até ela zerar. Resultado: empate com baseline
(p=0.82). Confirma empiricamente o teorema de parada opcional (martingale)
que já tínhamos só na teoria.

### 4. "Se fizermos N combinações, teríamos mais chance combinatória?"
Testado com Monte Carlo real (não só cálculo teórico): com arsenal
heurístico, saturação em 10-11 palpites. Com otimização de conjunto
genuína (hill-climbing), o ganho real se estende até ~12-15, com queda
brusca depois disso.
**Como reaplicar:** sempre simular contra o histórico real ou contra
sorteios simulados — nunca só calcular probabilidade teórica isolada.

### 5. "Isso pode trazer vantagem se os N palpites forem variantes do mesmo estado?"
Testa se "variar dentro do mesmo pool" é diversidade real ou ilusão. Já
vivido com HIBRIDO (redundante com 5 dos 7 palpites que o originaram) e
com testes de "núcleo fixo" (30 fixo + 20 rotativo reduziu P(≥15ac) de
4.83% para 3.51%).
**Regra validada:** overlap ótimo entre pares é ~22-27/50 — confirmado
tanto empiricamente quanto pela teoria de submodularidade e dependência
negativa (ver arquivo E).

---

## BLOCO 3 — AUDITAR OS PRÓPRIOS PALPITES GERADOS

### 6. "Por que não tem [dezena X] em nenhum palpite?"
Revela viés de exclusão sistemático não intencional. Usado para descobrir
buracos reais e, no caso mais caro, para expor que 11/67/89 estavam
ausentes de TODO o arsenal por design (não por azar) — a maior correção
já feita no projeto.
**Reaplicar:** sempre que um arsenal for fechado, antes de apostar, rodar
a contagem de cobertura por dezena.

### 7. "Isso foi convicção da hipótese ou só simetria estética?"
**RESPOSTA OBTIDA (walk-forward N=2889):** testado — distribuição forçada
de exatamente 5 dezenas por linha vs distribuição natural (top-50 livre).
Resultado: empate, com direção levemente negativa não significativa
(p=0.078). A simetria de "5 por linha" era estética, não hipótese — vale
como restrição estrutural (evita décadas vazias/lotadas), nunca como
critério de vantagem.

### 8. "Nenhuma dezena pode ficar 100% fixa entre os palpites — auditar explicitamente"
Erro estrutural mais recorrente do projeto. Vivido múltiplas vezes: V1/V3
com décadas inteiras vazias, H4 com 10 dezenas em L4+L7 simultaneamente,
e H12 (pós-otimização automática) com L6 inteira vazia porque os outros
palpites compensavam.
**Checklist formal:** nunca >8 dezenas por linha, nunca L=1, sempre
auditar CADA palpite individualmente após qualquer otimização automática
— ela pode encontrar atalhos que violam boas práticas individuais.

---

## BLOCO 4 — FORMALIZAR LIMITES MATEMÁTICOS DO JOGO ESPECÍFICO

### 9. "Qual o piso mínimo garantido de acertos, matematicamente?"
**Já calculado para a Lotomania:**
- P(20ac) = 1/11.372.635 por ticket
- P(≥15ac) = 1/88 por ticket
- P(≥19ac) = 1/341.951 por ticket — **idêntico para QUALQUER conjunto de
  50 dezenas** (teorema de simetria da distribuição hipergeométrica, não
  estimativa sujeita a mais dados)
- Garantia do complemento: ac(P1) + ac(complemento) = 20 SEMPRE
- Teto teórico do "melhor entre N palpites" (Bertsimas-Natarajan-Teo):
  para 10 palpites, ~16 acertos no melhor caso teórico absoluto —
  inatingível na prática com bilhetes de 50 números, mas confirma que
  ~13-14 (o que observamos) já está próximo do que é fisicamente possível
- Não existe piso mínimo garantido >0 acertos com um único ticket

**Diferença de outros jogos:** universo menor (ex: Mega-Sena, 60 números,
6 sorteados) muda completamente a distribuição — recalcular do zero,
nunca herdar números.

---

## BLOCO 5 — FECHAR CADA SESSÃO BEM

### 10. "O que eu não pensei nem solicitei que você pode adicionar à biblioteca?"
Força auto-auditoria proativa. Foi assim que chegamos aos 5 relatórios de
pesquisa científica (arquivo E), à descoberta condicional do "DNA
replicado", e à descoberta do erro de escopo ESP (auditando um resultado
real, não uma bateria de testes teórica).
**Reaplicar:** ao final de qualquer sessão longa, antes de encerrar.

---

## NOTA SOBRE ORIGEM CRUZADA

Este documento nasceu de uma reflexão feita em paralelo sobre um jogo
diferente (Lotofácil). A transferência funcionou porque as perguntas são
sobre *processo de raciocínio*, não sobre números específicos — prova de
que a disciplina construída aqui é portátil entre domínios, mesmo quando
os dados não são. O mesmo vale para o documento de onboarding da Mega-Sena
(fora desta biblioteca numerada, por ser de outro projeto).

---

## BLOCO 6 — PRINCÍPIOS ADICIONAIS TRANSFERIDOS DO LOTOFÁCIL (com correção)

Um segundo documento de reflexão cruzada trouxe mais princípios úteis,
com uma ressalva importante que precisou ser corrigida antes de aceitar.

### 11. "Existe um teste de referência mínimo antes de tentar melhorar?"
Antes de qualquer tentativa de "melhorar" um método, calcular o palpite
de maior frequência histórica contra todo o histórico real, para saber
o piso que qualquer estratégia nova precisa superar. Já é nossa prática
padrão — reforça, não muda nada.

### 12. "Alguma dezena está perto de 100% de presença no arsenal do dia,
sem isso ter sido decisão consciente?"
Auditoria simples e valiosa: contar a frequência de CADA dezena no
conjunto total de palpites fechados. Se alguma se aproxima de 100%
sem ter sido escolha deliberada, é vício de repetição — vale testar
deliberadamente a ausência dela em pelo menos 1 palpite.

### 13. "Ao corrigir um vício, criei outro sem perceber?"
Depois de aplicar qualquer regra corretiva nova ("evitar dezenas
super-representadas", por exemplo), checar explicitamente: quais
dezenas de alto mérito real ficaram de fora por causa da correção?
Regra nova nunca deve substituir a checagem de efeito colateral.

### 14. "A diversidade do arsenal é real ou só de roupagem?"
Já é nossa Etapa 6 — mas vale reforçar a formulação: múltiplos palpites
com estrutura superficialmente diferente (soma diferente, distribuição
por zona diferente) podem compartilhar um núcleo real de dezenas quase
idêntico. Overlap real entre TODOS os pares é o que importa, nunca a
aparência estrutural isolada.

### ⚠️ PRINCÍPIO REJEITADO — "Estrutura condicional ao último resultado"

O documento original recomendava: em vez de usar a média geral do
histórico para decidir a estrutura de um palpite (soma esperada,
distribuição por década), calcular a distribuição condicional — o que
historicamente vem DEPOIS de um resultado com a MESMA estrutura que o
último resultado real teve.

**Isso já foi testado especificamente para Lotomania e refutado, duas
vezes, com dados reais (arquivo A, Bloco 4):**
- "Regime B→M": P(próximo=M | atual=B) = 58.8% = P(próximo=M) sem
  condicionar em nada, p=0.98 — idêntico
- "L=0 retorna": 91.2% condicional vs 90.7% incondicional, p=0.37 —
  idêntico

**Não adotar este princípio como veio.** Pode ser válido para Lotofácil
(parâmetros diferentes, não verificado aqui) — mas para Lotomania,
"o que o último resultado sugere para o próximo" já foi testado
diretamente e não tem sinal. Décadas e regime não têm memória neste
jogo. Se a mesma ideia reaparecer disfarçada com outro nome, checar
contra este bloco antes de retestar do zero.
