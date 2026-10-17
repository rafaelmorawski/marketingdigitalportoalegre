---
name: formalizar-lean
description: Escreve e VERIFICA no Lean 4 uma afirmação matemática do projeto Lotomania (simetria do espelho, contagens, limites de cobertura). Use quando o Rafael pedir "provar", "formalizar" ou "verificar no Lean" uma afirmação exata. Não serve para afirmações sobre o histórico ou simulações.
---
1. **Só formalize o que é matemática exata** (combinatória, simetrias, limites de contagem). Resultados do histórico, hill-climbing e simulações ficam em Python; não existe prova em Lean deles.
2. Escreva o enunciado em `lean/Lotomania.lean` (Lean 4 núcleo, sem Mathlib; ver o arquivo para o estilo). Padrão de afirmação intermediária: `have h : <Prop> := by ...`; `have` esconde o corpo da prova, `let` mantém a definição.
3. Compile: `export PATH="$HOME/.elan/bin:$PATH"; lean lean/Lotomania.lean`. **Só diga "provado" se o código de saída for 0 e não houver `sorry`.** Rode `#print axioms <teorema>`: esperado só `propext`, `Classical.choice`, `Quot.sound` (ou nenhum).
4. Contas grandes: `decide +kernel` com `binom` pela fórmula multiplicativa (o `Nat.choose` recursivo é exponencial). Se o Lean recusar um número, **o enunciado estava errado** (aconteceu com 1 em 11.372.636: o valor exato é 11.372.635,89…).
5. Instalação: `elan` (https://github.com/leanprover/elan) + `lean-toolchain` em `lean/`. O teste `ProvasLean` em `tests/` compila o arquivo se o Lean existir.
6. Relate ao Rafael o que foi provado, com o enunciado em português, e o que NÃO é coberto. Não use esta skill para dar aparência de rigor a um resultado empírico.
