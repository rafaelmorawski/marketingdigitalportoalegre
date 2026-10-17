# Pré-registro — painel de semáforos (17/10/2026)
Pergunta da Rafael: condições do sorteio (soma, pares, ≥50, décadas vazias, sequências, agrupamento, repetição, tempo de ocorrência) mostram tendência que se repete, e algum "semáforo" aponta uma hipótese útil?

## Indicadores (26), calculados por sorteio
pares, soma, acima50, décadas vazias, colunas vazias, máx. por década, mín. por década, máx. por coluna, consecutivos (i,i+1), maior sequência de consecutivos, vizinhas na linha, vizinhas na coluna, vizinhas nas diagonais, vizinhos-8 (agrupamento), repetidas do anterior, maior buraco, amplitude (maior−menor), desvio-padrão das dezenas, borda, primos, múltiplos de 3, múltiplos de 5, quadrante mínimo, pares inferior−superior, dezenas ≤31, repetidas da década.

## Testes (por indicador)
A) Ljung-Box lags 1–10 (a série repete tendência?) — χ² gl 10.
B) Alerta alto: depois de um sorteio com indicador no decil superior do nulo (simulado, 300 mil), a média do indicador no sorteio seguinte difere do nulo? (z)
C) Alerta baixo: idem, decil inferior.
D) Tempo de ocorrência (12 eventos): depois de m sorteios sem o evento (m = quantil 75% do tempo de espera geométrico), a taxa do evento é maior que a probabilidade-base? (z binomial, "atrasado volta?")
Total: 26×3 + 12 = 90 testes → Bonferroni bilateral p < 0,00056 (|z| > 3,45).

## Semáforo
Verde |z|<1,5; amarelo 1,5–2; vermelho >2 (z do valor atual contra o nulo uniforme). Cada semáforo traz: hipótese associada, sequência atual, tempo desde o último evento e **selo de evidência histórica** (confirmada se passa Bonferroni E replica nas duas metades; senão "não confirmada").

## Resultado (`python3 lab/semaforo.py`, 2.988 sorteios)
**Nenhum dos 90 testes passou (|z| > 3,45).** Maior |z| isolado entre os 64 testes condicionais: 2,61 (vizinhas na diagonal, após valor baixo); esperado pelo acaso entre 64 testes: ~2,4 a 2,8. Menor p de Ljung-Box entre 26 indicadores: 0,040 (pares), contra limiar 0,00056.
Tempo de ocorrência: 12 eventos (década vazia, sequência ≥4, pares ≥13/≤7, acima50 ≥13/≤7, soma extrema, repetidas extremas, colunas vazias). Nenhum evento "atrasado" volta mais do que a probabilidade-base (maior z: +2,04 e −2,22, ambos abaixo do limiar). O tempo de espera é o de um processo sem memória.
Painel do estado atual: `relatorios/SEMAFORO_C2988.md` (atualizado pelo `lab/robo.py` a cada sorteio).
