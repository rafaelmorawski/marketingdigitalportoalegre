# "Na maioria das vezes repete 8 a 9 dezenas do sorteio anterior" (17/10/2026) — `lab/repetidas_janela.py`
- Do sorteio imediatamente anterior (k=1): média 4,01 (esperado 4,00); 8 ou 9 repetidas em apenas 2,1% dos sorteios (esperado 1,7%); 3 a 5 repetidas em 64,2%.
- A faixa 8–9 aparece quando se olha as dezenas já saídas em mais de um sorteio anterior: k=2 média 7,17 (8–9 em 30,3%, esperado 31,4%); **k=3 média 9,73 (8–9 em 31,8%, esperado 31,5%)**; k=4 média 11,78.
- Todas as distribuições batem com a esperada (χ² p entre 0,24 e 0,99). A "maioria" de 8–9 é consequência aritmética: união de 2–3 sorteios de 20 dezenas cobre 7,2–9,8 dezenas de qualquer sorteio novo.
