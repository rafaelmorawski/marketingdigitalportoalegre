# Autópsia dos últimos 100 sorteios e pré-registro (17/10/2026) — versão corrigida

## Erro encontrado e corrigido
A primeira versão do `aprendizado_online.py` desempatava o top-50 pelo número da dezena. Nas lentes binárias (ciclo, repetida, coluna±10) o bilhete virava "poucas dezenas da lente + as de número mais baixo". Os últimos 100 sorteios tiveram 10,41 dezenas em 00–49 (esperado 10,00; z +1,84), e isso fabricou z ≈ +2 em várias lentes. Corrigido: desempate aleatório.

## Resultado corrigido (aprendizado C1001–C2888, teste C2889–C2988)
- Aprendiz (hedge sobre 14 lentes): 10,053 (z +1,16) no aprendizado; 10,360 (z +1,79) no teste. Nulo 10,000.
- Persistência do desempenho das lentes entre sorteios consecutivos: −0,005 (limite 2σ ±0,045).
- Melhor lente a posteriori em cada sorteio: 13,44 acertos; a mesma lente no sorteio seguinte: 10,28 (viés de seleção).
- Dezena errada em t sai em t+1 com 0,2019 (demais 0,1998; uniforme 0,2000).
- Lentes com z isolado alto: coluna±10 (+2,47 aprendizado, +2,29 teste) e freq50 (−0,79 aprendizado, +2,69 teste). Limiar Bonferroni para 14 lentes: 2,91. Nenhuma passa; freq50 não replica entre fases.

## Teste direto do mecanismo da coluna (chance de a dezena sair, dado que tem vizinha ±10 sorteada no sorteio anterior)
| Recorte | com vizinha | base | p |
|---|---|---|---|
| C1–C1000 (nunca visto pelo aprendiz) | 0,2027 | 0,2000 | 0,23 |
| C1001–C2988 | 0,2024 | 0,2000 | 0,13 |
| tudo | 0,2025 | 0,2000 | 0,051 |
Controle (vizinha na linha ±1): 0,2008, p = 0,53.
Efeito, se real: +0,25 ponto percentual por dezena (≈ +0,08 acerto por bilhete). Para confirmar em tempo real seriam necessários milhares de sorteios.

## Pré-registro
Apenas a lente coluna±10 é registrada antes de cada sorteio (`lab/lentes_forward.py`), por custo zero. Não muda a grade.
