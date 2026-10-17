---
name: novo-resultado
description: Quando sair o resultado de um concurso da Lotomania. Confere os jogos por grupo, atualiza ledger e ciclo, roda o painel de predição e o pré-registro, e responde ao Rafael com tabela por grupo. Use ao receber 20 dezenas ou quando ele disser que o sorteio saiu.
---
1. Rode `python3 lab/robo.py` (busca na API da Caixa; consulta o concurso seguinte ao do ledger, pois o endpoint "último" atrasa). Sem API: `python3 lab/robo.py --concurso <n> --dezenas "<20>" --data dd/mm/aaaa`.
2. Se o Rafael enviar nova planilha xlsx da Caixa: `python3 lab/ler_xlsx.py <xlsx> /tmp/x.csv`, converta para latin-1 em `data/Lotomania.csv` e confira contra a API (já bateu 2.987/2.987).
3. Responda em português com: tabela por grupo (melhor, média), ciclo (faltantes antes/depois, repetidas), veredito do painel, e a lente forward. **Sem inventar tendência** a partir de um sorteio. A cada ~20 sorteios, resuma o ledger por grupo (esperado: média 10,0; ~170 sorteios para distinguir grupos).
4. Commit e push na branch designada. Não abrir PR sem pedido.
