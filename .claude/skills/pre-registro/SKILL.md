---
name: pre-registro
description: Registra uma hipótese da Lotomania ANTES de ver o resultado (bilhete previsto, estatística, regra de decisão). Use para testes forward.
---
1. Escreva hipótese, estatística, janela, nº de testes e limiar em `relatorios/PREREG_<tema>.md` antes de rodar.
2. Para previsões forward use `python3 lab/lentes_forward.py prever <concurso>` (grava `data/lentes_previsoes.json` com os dados até o último concurso conhecido) e, depois do sorteio, `conferir` (o `lab/robo.py` já faz isso).
3. Regra de decisão fixada antes: após 100 sorteios novos, só conta se z ≥ limiar de Bonferroni E replicar nas duas metades (50+50). Senão: sem sinal.
