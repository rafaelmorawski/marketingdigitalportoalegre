# G — HIPÓTESES DE CICLO (FALTANTES vs JÁ APARECERAM)
**Documento de acompanhamento — testar sistematicamente a cada sorteio**
**Recriado após reset de ambiente — histórico consolidado até C2973**

---

## O QUE ESTAMOS TESTANDO

Uma família de hipóteses de CONTEÚDO (não de estrutura/E[max]) sobre a
relação entre dezenas que faltam aparecer no ciclo atual e dezenas que
já apareceram. Diferente de hill-climbing (que otimiza cobertura de
conjunto sem opinião sobre qual dezena é melhor), esta família aposta
em uma composição específica de conteúdo.

**Testado formalmente e SEM sinal comprovado:**
- Resíduos do ciclo isolado: p=0.914, N=2864
- Família completa (P1,P6,P7,P8) em 1848 pontos históricos: todos p>0.27
- Misto ciclo+temperatura: N=1198, p=0.537

Isso significa: os resultados desta família devem ser lidos como
DIVERSIDADE ESTRUTURAL válida, não como vantagem preditiva.

---

## TABELA DE ACOMPANHAMENTO — NOVAS vs REPETIDAS POR SORTEIO

| Sorteio | Novas | Repetidas | Faltavam antes | Posição no ciclo |
|---|---|---|---|---|
| C2968 | 10 | 10 | 39 | 5º |
| C2969 | 7 | 13 | 32 | 6º |
| C2970 | 10 | 10 | 32 | 7º |
| C2971 | 6 | 14 | 22 | 8º |
| C2972 | 4 | 16 | 16 | 9º |
| C2973 | 3 | 17 | 12 | 10º |
| C2974 | 1 | 19 | 4 | 11º |
| C2975 | 3 | 17 | 1 | 12º |

**8 pontos agora. Ciclo quase fechado — só falta a dezena 54.**

---

## HISTÓRICO DE DESEMPENHO POR RODADA

| Sorteio | N palpites | Melhor real | Palpite vencedor |
|---|---|---|---|
| C2965 | 19 | 14 | P6, FinalDecada |
| C2966 | 23 | 14 | P7 |
| C2967 | várias hipóteses | 16 | Blindagem (adversarial, sorte alta variância) |
| C2968 | 22 | 13 | vários empatados |
| C2969 | 5 | 12 | P3_HillClimb |
| C2970 | 8 | 14 | P6_2porDecada |
| C2971 | 9 | 12 | P1_Faltantes |
| C2972 | 14 | 12 | P6, P7 (empate) |
| **C2973** | **11** | **15** | **P2 (1 por década)** |
| C2974 | 3 | 13 | P3_SetCover (guloso) |
| C2975 | 7 | 14 | P4_PerdidasC2974 |

---

## RESULTADO REAL C2973 — desempenho dos 11 palpites

| Palpite | Acertos |
|---|---|
| **P2 (1 por década)** | **15** (melhor da sessão em várias rodadas) |
| P6 (Faltantes+34 novo) | 12 |
| P3, P7 | 11 |
| P4, P10 (Edge Omitidas) | 10 |
| P1, P11 (Foco Já Sorteadas) | 9 |
| P5, P8 | 8 |
| P9 (Objetivo P≥15 direto) | 5 (pior — ironia: construído pra bater 15+, foi quem menos bateu) |

**Lição de processo:** otimizar um palpite especificamente pra um
objetivo (P≥15) não garante que ELE será o vencedor naquele sorteio
específico — reforça que o valor está no CONJUNTO, não em prever
qual peça vai se destacar.

---

## CICLO FECHANDO — só falta 1 dezena: o 54

Estado atual (após C2975): 99 já apareceram, **falta apenas 54**.
Quando sair, o ciclo (iniciado em C2964) fecha após 12 sorteios e
reinicia do zero — todas as 100 voltam a ser "faltantes".

---

## MÉTODOS NOVOS TESTADOS HOJE (segunda metade da sessão)

### 8. Programação Linear Inteira (ILP) — Set Cover EXATO
Diferente do guloso (aproximação garantida 63% do ótimo), resolver
via solver (PuLP/CBC) encontra o ÓTIMO GLOBAL matematicamente
comprovado. Funciona bem quando o problema já está REDUZIDO (poucos
pares restantes, ex: 831) — resolveu em ~90s, Status=Optimal.
**Não escala bem para o problema completo do zero** (4950 pares):
timeout em 150s sem convergir. Usar ILP como refinamento sobre
arsenal já existente, não como primeira construção.

**Resultado prático:** os 2 palpites construídos via ILP numa rodada
ficaram na média-baixa (9 e 8) no resultado real — garantia de
cobertura de pares não se traduziu em destaque individual, mesmo
sendo matematicamente ótima. Confirma o padrão já visto com Set
Cover guloso.

### 9. "Apoio derivado" (híbrido de dezenas comuns entre 2 palpites) — CUIDADO
Construir um palpite priorizando as dezenas que 2 outros palpites já
compartilham (ex: 12 ou 23 comuns entre P1 e P3) parece reforçar
convicção, mas **testado hoje causou problema real**: com 4 palpites
dessa família (2 originais + 2 apoios derivados), 17 dezenas ficaram
presentes em TODOS os 4 simultaneamente (concentração excessiva), e
10 dezenas ficaram de fora de todos (furo real). E[max] caiu pra
11.85, abaixo do que hill-climbing puro já alcançava (13+).

**Correção aplicada:** um 5º palpite via hill-climbing puro,
priorizando especificamente as 10 do furo, corrigiu tudo — E[max]
subiu pra 12.38 (+0.53, maior ganho do dia) e cobertura voltou a
100/100. **Lição: "apoio derivado" tem valor conceitual, mas precisa
sempre de auditoria de overlap/cobertura depois — não usar mais de
2 palpites dessa família sem checar concentração.**

### 10. Aposta Espelho (recurso oficial do volante Lotomania)
O volante físico tem opção "Aposta Espelho" que o PRÓPRIO SISTEMA da
Caixa gera automaticamente (as outras 50 dezenas não marcadas). Não
precisa construir manualmente — só marcar a opção no bilhete. Confirma
na prática o que já sabíamos: ac(P)+ac(espelho)=20 sempre, por
identidade de conjuntos.

---

## PRÓXIMOS PASSOS QUANDO C2976 SAIR

1. Registrar resultado real, atualizar tabela novas/repetidas
2. Verificar se o 54 saiu — se sim, CICLO FECHOU, reiniciar contagem
   de faltantes do zero (todas as 100 voltam a ser "faltantes")
3. Testar os 5 palpites atuais (P1, P2_Hibrido, P3, ApoioTotal, P5)
4. Auditar overlap/concentração de QUALQUER arsenal com "apoio
   derivado" antes de finalizar — lição de hoje
5. Preferir ILP só como refinamento sobre arsenal já reduzido, não
   construção do zero (timeout em problema completo)

---
