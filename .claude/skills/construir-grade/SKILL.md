---
name: construir-grade
description: Monta e mede uma grade de jogos da Lotomania (jogos fixos + N novos otimizados) com relatório honesto. Use quando o Rafael pedir grade, grupo novo, mais jogos ou comparação entre grupos para um concurso.
---
1. Pergunte (ou confirme) **orçamento** (R$ 3 por jogo) e **quais grupos ficam fixos** (J é fixo por decisão dele).
2. Rode `python3 lab/construtor.py --fixos data/jogos_C2988.json --grupos J --novos <N> --nome <NOME>` (ou `--nucleo-relogio` para o relógio; `--obj emax|p15|cauda`). Ele usa 3 bancos, controle de 40 aleatórios e imprime custo, E[max], P(≥15), P(≥17), chance de 20 e de 20-ou-0, piso garantido e retorno aproximado.
3. Valide com `python3 lab/validar_dados.py` e `python3 -m unittest discover -s tests`.
4. Responda com tabela e os jogos em bloco de código (dezenas com dois dígitos). Diga sempre: é **cobertura, não previsão**; chance de 20 = N × 1/11.372.636 (ou 2N com o zero); 15 acertos paga ≈ R$ 10; retorno esperado < preço.
5. Chame `auditor-estatistico` se algum ganho parecer maior que +0,2 em E[max] sobre aleatórios (teto conhecido ≈ +0,17 a +0,2).
Lembretes: paridade e restrições não importam; hill-climbing no histórico real só sobreajusta; ganho de otimização cresce com N.
