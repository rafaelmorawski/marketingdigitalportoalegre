# Perguntas 10, 86, 87 e 54 — poder estatístico e garantia mínima (17/10/2026)

## 1. Poder dos nossos detectores (`lab/poder.py`, 200 históricos sintéticos de 2.988 sorteios por célula)
Calibração: sem viés, falsos positivos a p<0,05 = 4,0% (χ² freq), 4,0% (top-50), 3,5% (repetição), 2,5% (vizinha coluna). Nominal 5%.
| Viés injetado | δ (pp) | Detector | Poder p<0,05 | Poder Bonferroni (0,0033) | Ganho de um bilhete que CONHECE o viés |
|---|---|---|---|---|---|
| 10 dezenas fixas | +0,52 | χ² freq | 8,5% | 1,0% | +0,027 acerto |
| | +0,96 | χ² freq | 36,5% | 13,0% | +0,050 |
| | +1,90 | χ² freq | 99,0% | 94,5% | +0,103 |
| | +3,86 | χ² freq | 100% | 100% | +0,211 |
| repetição do anterior | +0,43 | taxa | 76% | 36% | +0,051 |
| | +0,85 | taxa | 100% | 99,5% | +0,109 |
| vizinha na coluna | +0,40 | taxa | 92,5% | 59% | +0,096 |
| | +0,76 | taxa | 100% | 100% | +0,187 |
Leitura: um viés que passa despercebido vale ≤ +0,05 acerto por bilhete (≈ +6% na chance de 15+ e na de 20); os vieses que valem ≥ +0,1 acerto, nossos detectores pegam em ≥ 90% das vezes. Observado no histórico real: repetição +0,07 pp (excluído acima de ~0,4 pp), coluna ±10 +0,25 pp (abaixo do que 2.988 sorteios detectam: inconclusivo e de valor ~+0,06).
Limite do estudo: detectores simples; o painel de ML completo não foi submetido à mesma injeção.

## 2. Garantia mínima de acertos (`lab/garantia.py`, adversário exato por programação inteira)
Pior sorteio possível para cada grupo (qual o menor valor do melhor jogo):
| Grupo | Melhor jogo garantido ≥ |
|---|---|
| J espiral (10) | 9 |
| **K10** | **10** |
| **R10** | **10** |
| 24 jogos do C2988 | 10 |
| aleatórios (10) | 6 a 7 |
| jogo + complemento (2) | 10 |
Limite mínimo de jogos para GARANTIR k+ (contagem, 1/P(≥k)): 15+ → 88 jogos (R$ 264); 17+ → 2.474; 19+ → 341.952; 20 → 11.372.636 (R$ 34 mi). Na prática, designs reais exigem mais que esse limite.
Garantir 10 não paga prêmio algum (a Lotomania paga de 15 acertos e 0); é um indicador de robustez, não de retorno.
