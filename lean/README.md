# Provas em Lean 4 (afirmações matemáticas do laboratório)
`lean lean/Lotomania.lean` — sem erros = todas as provas aceitas pelo compilador. Lean 4.35.0 (núcleo, sem Mathlib); instalar com `elan` (https://github.com/leanprover/elan).
Provado: (1) jogo + espelho somam 20 acertos, logo garantem ≥10; (2) 0 acertos de T ⇔ 20 acertos do espelho; (3) 1 em 11.372.636 é o arredondamento de C(100,20)/C(50,20) = 11.372.635,89…; (4) garantir 15+ exige ≥88 jogos e 19+ ≥341.952 (limite de contagem); (5) C(50,0)·C(50,20) = C(50,20)·C(50,0).
Não provado em Lean (só testado em Python/simulação): tudo sobre o histórico, hill-climbing, pisos garantidos de grades específicas (programação inteira em `lab/garantia.py`).
