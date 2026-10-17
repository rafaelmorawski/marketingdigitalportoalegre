---
name: risco-orcamento
description: Calcula retorno esperado, probabilidade de perda, tempo até ver um 19 ou 20 e trajetórias de N concursos para um orçamento. Use antes de fechar uma aposta ou quando o Rafael perguntar sobre quanto gastar, risco ou tempo.
---
1. `python3 lab/risco.py --jogos <N> --jackpot <milhões> --concursos <C>` (jackpot = prêmio estimado do próximo concurso).
2. Apresente: retorno esperado por bilhete (≈ R$ 0,61 + R$ 0,089 por milhão de prêmio; supõe ganhador único), perda esperada, percentis do resultado líquido, P(terminar no lucro) e tempo até 50% de chance de 19+ e de 20.
3. **Regra de cuidado (CLAUDE.md seção 1):** lembre, sem sermão, que o gasto deve caber num limite que ele aceite perder; se parecer pressionado financeiramente, ofereça ajuda para pensar outros caminhos. Nunca alimente a esperança de ganho.
4. Aproximação conhecida: jogos tratados como independentes; prêmios por faixa são médias dos últimos 300 concursos; imposto e divisão do prêmio ignorados.
