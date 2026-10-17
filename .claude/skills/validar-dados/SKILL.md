---
name: validar-dados
description: Confere a integridade do histórico da Lotomania (contiguidade, dezenas válidas, datas, planilha × API × ordem de saída) e atualiza dados novos. Use ao receber planilha nova, antes de qualquer análise grande, e quando um número de referência não bater.
---
1. `python3 lab/validar_dados.py` (sai com erro se houver divergência).
2. Planilha xlsx da Caixa: `python3 lab/ler_xlsx.py <xlsx> /tmp/x.csv`, converter para latin-1 em `data/Lotomania.csv` (o loader lê latin-1) e rodar a validação de novo. O leitor do `ler_xlsx.py` tolera células numéricas inválidas ('-').
3. API da Caixa: o endpoint "último resultado" atrasa; consulte o número do concurso diretamente (`.../lotomania/<n>`). Concurso não publicado responde HTTP 500/404.
4. Ordem de saída das bolas: `python3 lab/baixar_ordem.py <último> data/historico_ordem.csv`.
5. Antes de commitar: `python3 -m unittest discover -s tests`.
