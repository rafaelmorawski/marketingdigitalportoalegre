# ADENDO PARA E_BIBLIOTECA_CIENTIFICA.md — NOVA SEÇÃO 7
**Inserir ao final do arquivo E existente, mantendo a numeração sequencial**

---

## 7. COMPUTAÇÃO EVOLUTIVA E DESIGN COMBINATÓRIO APLICADOS (sessão C2967-C2970)

**Contexto:** questionamento legítimo de que limitar o ferramental a
Hill-Climbing seria limitação técnica, já que Algoritmos Genéticos,
Têmpera Simulada e Design Combinatório (Set Cover) são abordagens
válidas da matemática discreta. Testado empiricamente, não só
teoricamente.

### 7.1 Algoritmo Genético vs Hill-Climbing — testado com orçamento igual

**Metodologia:** mesmo problema (edge sobre arsenal de 6 palpites),
mesmo orçamento computacional (60.000 avaliações de fitness para
ambos), comparação direta.

**Resultado:**
- Hill-Climbing: score final = 12.9812
- Algoritmo Genético (população 30, crossover, mutação, seleção por
  elite): score final = 12.9772
- Diferença: -0.0040 (GA levemente pior, dentro do ruído)

**Interpretação:** GA e Têmpera Simulada são genuinamente superiores
a Hill-Climbing em paisagens de otimização com múltiplos máximos
locais separados por "vales" profundos. A função objetivo aqui
(E[máximo entre N palpites]) parece ser relativamente suave nesse
espaço de busca — trocar 1 dezena por vez quase sempre encontra
caminho de melhoria incremental sem ficar preso, dado que o espaço
combinatório de 50-de-100 é enorme e bem conectado. Isso explica por
que Hill-Climbing com reinício aleatório já performa no mesmo patamar
do GA aqui, mesmo sem os mecanismos extras de escape de máximo local.

**Não descartar GA permanentemente** — testado em 1 configuração
específica. Vale retestar em arsenais maiores ou com funções objetivo
diferentes (ex: P(≥17) direto, que pode ter paisagem mais irregular).

### 7.2 Set Cover Guloso — cobertura determinística, não probabilística

**Diferença fundamental de tudo mais testado:** Hill-Climbing otimiza
uma EXPECTATIVA MÉDIA contra milhares de sorteios simulados —
probabilístico. Set Cover resolve GARANTIA COMBINATÓRIA — determinístico.

**Metodologia:** algoritmo guloso clássico (aproximação garantida
(1-1/e) ≈ 63% do ótimo — Feige 1998) para maximizar pares de dezenas
NOVOS cobertos, dado um arsenal já existente.

**Resultado real (arsenal de 6 palpites, C2968):**
- Pares totais possíveis: 4.950
- Pares já cobertos antes do Set Cover: 4.471 (90.3%)
- Pares novos cobertos pelo palpite Set Cover: 271 de 479 que faltavam
- Cobertura final: 4.742/4.950 (95.8%)

**O que isso garante, formalmente:** se dois números específicos,
dentre os 271 pares agora cobertos, saírem juntos no resultado real,
o arsenal terá pelo menos essas duas dezenas juntas em algum palpite
— não é chance, é certeza combinatória. Isso não aumenta a
probabilidade de qualquer par sair (permanece aleatório), mas
garante que, SE sair, a estrutura não fica cega para ele.

**Desempenho real observado (C2968):** o palpite Set Cover fez 9
acertos — mediano, não se destacou nem prejudicou. A garantia
combinatória não se traduziu em vantagem prática nesse resultado
específico, mas o valor do método é estrutural (blindagem), não de
picos de acerto.

### 7.3 Armadilha estatística pega em tempo real — adenda às 4 já catalogadas

**Contexto:** testando se a soma tem "regressão à média proporcional"
após desvios extremos (diferente de correlação simples já testada).

**O que pareceu, inicialmente:** correlação de -0.7175 entre desvio
atual e mudança no próximo sorteio, p=0.0000 — parecia descoberta
forte.

**O que era de verdade:** artefato matemático puro. A variável
"mudança" foi definida como `soma_próxima - soma_atual`, que CONTÉM
`-soma_atual` na própria fórmula. Isso garante correlação negativa
com o desvio atual mesmo em dados 100% aleatórios, por pura álgebra.
Confirmado rodando o mesmo teste em dados sintéticos: -0.707,
praticamente idêntico ao valor "real" encontrado.

**Correlação teórica exata esperada só pela definição:** -1/√2 ≈
-0.7071 — bate quase exatamente com o -0.7175 observado.

**Isso é a 5ª armadilha catalogada** (arquivo B já tinha 4): quando
uma variável derivada CONTÉM outra variável testada dentro da própria
fórmula (com sinal), a correlação entre elas é mecanicamente
garantida, independente de qualquer comportamento real do sistema.
Regra de verificação: antes de aceitar qualquer resultado "forte
demais" sobre uma variável derivada, checar se a fórmula de derivação
contém a variável de comparação embutida algebricamente.

---

## SÍNTESE ATUALIZADA — O QUE MUDA NO PROTOCOLO

1. **GA testado e não superou Hill-Climbing** nesta configuração —
   continuar usando Hill-Climbing como método padrão, sem descartar
   GA para configurações futuras diferentes.
2. **Set Cover guloso adotado como método complementar formal** — usar
   quando o objetivo é blindagem de pares específicos, não só
   maximizar expectativa média. Adicionar como Etapa opcional no
   protocolo de construção (arquivo B).
3. **5ª armadilha estatística catalogada** — variável derivada
   contendo a variável de comparação embutida algebricamente sempre
   correlaciona espuriamente. Adicionar ao Bloco de Armadilhas do
   arquivo B.
