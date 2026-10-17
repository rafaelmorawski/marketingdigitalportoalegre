# O prêmio de 0 acertos (17/10/2026) — `lab/zero_acertos.py`

## Matemática
- 0 acertos de um bilhete T = o sorteio cai inteiro no complemento de T = 20 acertos do espelho de T. P = 1 em 11.372.636, igual aos 20. Um jogo já "joga" nos dois lados; não existe um método diferente para o zero.
- Um grupo de N jogos tem 2N conjuntos efetivos (jogos e espelhos). Chance de ser pago por 20 ou 0 (união, correção de 2ª ordem): J 1 em 568.634; **K10 1 em 568.632**; R10 1 em 568.632; 24 jogos 1 em 238.141 (teto 1 em 236.930; perda 0,5% pelas grandes sobreposições, ex.: Z1 e U1 compartilham 40).
- Sobreposição a entre dois jogos: o sorteio ⊂ G_j ∩ espelho(G_k) exige |G_j∖G_k| = 50−a ≥ 20. Nunca se evitam todas as colisões (exigiria a < 20 e 50−a < 20), mas valem ~1e-9 do prêmio.
- Jogo + espelho: se o sorteio ⊂ T, T faz 20 E o espelho faz 0 (dois prêmios).

## Dados da Caixa (últimos 300 concursos, ≈1,72 mi de bilhetes por concurso)
- Ganhadores esperados de cada tipo, se as apostas fossem uniformes: 0,151. Observado: 20 acertos 0,147; 0 acertos 0,167; razão 1,14. Histórico todo: 970 ganhadores de 0 e 958 de 20. As apostas humanas são quase uniformes nesses extremos.
- Concursos com ao menos 1 ganhador de 0 acertos: 15,3%; de 20 acertos: 12,3%.
- Prêmio médio por ganhador de 0 acertos: R$ 131.251 (mediana R$ 126.327).
- Valor: R$ 0,0115 por bilhete por concurso (1% do preço). Com 24 jogos, R$ 0,28 sobre R$ 72.
- A estrutura do sorteio NÃO prevê o nº de ganhadores de 0 (correlação fora da amostra −0,005), ao contrário das faixas 15–18 (+0,25 a +0,41).
