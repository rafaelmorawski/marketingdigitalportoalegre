# Laboratório Lotomania

Pacote para levar ao Claude Code: histórico, os 24 jogos do C2988 com a razão de cada grupo, a biblioteca (A a I) e os scripts de conferência, auditoria e teste de predição. **Leia o `CLAUDE.md` primeiro** (missão, o que já sabemos, protocolo de rigor, fluxo).

## Instalação
    pip install -r requirements.txt

## Quando sair o resultado de um concurso (automático)
    python3 lab/robo.py      # busca na API da Caixa e roda o fluxo todo
    python3 -m unittest discover -s tests    # testes de regressão

## Manual
    python3 lab/conferir.py --concurso 2988 --dezenas "<20 dezenas>" --data 17/10/2026
    python3 lab/painel_predicao.py --csv data/Lotomania.csv --extras-file data/extras.csv --log data/painel_log.csv

## Ferramentas (em Python)
    from lab.ferramentas import avaliar_grade, comparar_com_aleatorios, chances_exatas, auditoria
    # jogos: lista de listas com 50 dezenas (0 a 99)

## Importante
Tudo aqui mede **cobertura em sorteios simulados uniformes** e estatística do histórico. Nada prevê o sorteio: a chance de 20 acertos é 1 em 11.372.636 por bilhete. Se algum teste mostrar desvio, replique em dados novos antes de qualquer conclusão.
