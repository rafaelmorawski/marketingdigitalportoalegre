/-
  Afirmações matemáticas do laboratório Lotomania, verificadas pelo compilador do Lean 4 (só núcleo, sem Mathlib).
  Compilar:  lean lean/Lotomania.lean     (sem erros = todas as provas aceitas)
  Os números concretos usam a fórmula multiplicativa do binomial e `decide +kernel`; os mesmos valores são calculados em Python em lab/.
-/

/-! ## 1. Espelho: acertos de T mais acertos do complemento de T = 20 -/

/-- Contagem dividida por um teste `q`: sorteados que estão em `q` + sorteados que não estão em `q` = sorteados. -/
theorem contagem_dividida {α : Type} (l : List α) (p q : α → Bool) :
    l.countP (fun x => p x && q x) + l.countP (fun x => p x && !q x) = l.countP p := by
  induction l with
  | nil => simp
  | cons a t ih =>
    simp only [List.countP_cons]
    cases hp : p a <;> cases hq : q a <;> simp <;> omega

/-- Se saem 20 dezenas, o jogo T e o seu espelho (complemento) somam exatamente 20 acertos. -/
theorem jogo_mais_espelho_somam_20 {α : Type} (l : List α) (d t : α → Bool)
    (h : l.countP d = 20) :
    l.countP (fun x => d x && t x) + l.countP (fun x => d x && !t x) = 20 := by
  have := contagem_dividida l d t
  omega

/-- Consequência: um jogo e o seu espelho garantem, juntos, pelo menos 10 acertos em algum dos dois. -/
theorem piso_de_10 {α : Type} (l : List α) (d t : α → Bool) (h : l.countP d = 20) :
    10 ≤ l.countP (fun x => d x && t x) ∨ 10 ≤ l.countP (fun x => d x && !t x) := by
  have := jogo_mais_espelho_somam_20 l d t h
  omega

/-- Simetria 20 × 0: o jogo T faz 0 acertos exatamente quando o espelho de T faz 20 (todas as 20 sorteadas). -/
theorem zero_de_T_e_vinte_do_espelho {α : Type} (l : List α) (d t : α → Bool) (h : l.countP d = 20) :
    l.countP (fun x => d x && t x) = 0 ↔ l.countP (fun x => d x && !t x) = 20 := by
  have := jogo_mais_espelho_somam_20 l d t h
  omega

/-! ## 2. Números exatos -/

def fatorial : Nat → Nat
  | 0 => 1
  | n + 1 => (n + 1) * fatorial n

/-- Binomial pela fórmula multiplicativa: n·(n−1)·…·(n−k+1) / k!. -/
def binom (n k : Nat) : Nat := ((List.range k).foldl (fun acc i => acc * (n - i)) 1) / fatorial k

theorem binom_100_20 : binom 100 20 = 535983370403809682970 := by decide +kernel
theorem binom_50_20  : binom 50 20  = 47129212243960 := by decide +kernel

/-- Chance de 20 acertos de um bilhete = C(50,20)/C(100,20). C(100,20)/C(50,20) = 11.372.635,89… : "1 em 11.372.636" é o valor arredondado. -/
theorem um_em_11372636_arredondado :
    11372635 * binom 50 20 < binom 100 20 ∧ binom 100 20 < 11372636 * binom 50 20 ∧
    22745271 * binom 50 20 < 2 * binom 100 20 := by
  decide +kernel

/-- Nº de sorteios com exatamente `h` dos 20 dentro de um bilhete de 50. -/
def comk (h : Nat) : Nat := binom 50 h * binom 50 (20 - h)

/-- Os 15+ somam S; garantir 15+ em QUALQUER sorteio exige ao menos C(100,20)/S jogos: o limite de contagem é 88 jogos. -/
theorem garantir_15_exige_88 :
    let S := comk 15 + comk 16 + comk 17 + comk 18 + comk 19 + comk 20
    87 * S < binom 100 20 ∧ binom 100 20 ≤ 88 * S := by
  decide +kernel

/-- Idem para 19+: 341.952 jogos no mínimo. -/
theorem garantir_19_exige_341952 :
    let S := comk 19 + comk 20
    341951 * S < binom 100 20 ∧ binom 100 20 ≤ 341952 * S := by
  decide +kernel

/-- A chance de 0 acertos é a mesma de 20 (mesma contagem C(50,20) de sorteios): simetria dos binomiais. -/
theorem zero_igual_vinte : comk 0 = comk 20 := by decide +kernel

#print axioms piso_de_10
#print axioms zero_de_T_e_vinte_do_espelho
#print axioms um_em_11372636_arredondado
#print axioms garantir_15_exige_88
#print axioms garantir_19_exige_341952
