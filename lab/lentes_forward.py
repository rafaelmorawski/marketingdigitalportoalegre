# -*- coding: utf-8 -*-
"""Teste forward pré-registrado da lente coluna±10 (hipótese pós-hoc: só vale com dados novos).
  python3 lab/lentes_forward.py prever 2989      -> grava os 4 bilhetes top-50 ANTES do sorteio em data/lentes_previsoes.json
  python3 lab/lentes_forward.py conferir 2989 "<20 dezenas>"  -> confere e acumula em data/lentes_forward.csv
Regra de decisão (fixada agora): após 100 sorteios novos, uma lente só conta se z >= 2,91 (Bonferroni, 14 lentes) E replicar na
segunda metade (50+50). Caso contrário: sem sinal."""
import csv, json, os, sys
import numpy as np
from dados import carregar_historico
from aprendizado_online import scores, top50, LENTES

ESCOLHIDAS = ["coluna±10"]   # única hipótese que sobreviveu à correção do desempate (ver relatorios/AUTOPSIA_100_e_prereg_lentes.md)
PREV, LOG = "data/lentes_previsoes.json", "data/lentes_forward.csv"

def prever(conc):
    M = carregar_historico()["D"]; t = len(M)
    S = dict(zip(LENTES, scores(M, None, t)))
    prev = json.load(open(PREV)) if os.path.exists(PREV) else {}
    prev[str(conc)] = {nm: sorted(int(x) for x in top50(S[nm])) for nm in ESCOLHIDAS}
    json.dump(prev, open(PREV, "w")); print("previsões gravadas para o C%d (usando dados até C%d)" % (conc, len(M)))
    for nm, v in prev[str(conc)].items(): print(f"{nm:15s}", " ".join(f"{x:02d}" for x in v))

def conferir(conc, dez):
    r = set(int(x) for x in dez.split()); prev = json.load(open(PREV))[str(conc)]
    novo = not os.path.exists(LOG)
    with open(LOG, "a", newline="") as f:
        w = csv.writer(f)
        if novo: w.writerow(["concurso"] + ESCOLHIDAS)
        lin = [len(r & set(prev[nm])) for nm in ESCOLHIDAS]; w.writerow([conc] + lin)
    print("acertos:", dict(zip(ESCOLHIDAS, lin)), "(esperado 10,00 cada)")
    d = list(csv.DictReader(open(LOG))); n = len(d)
    for nm in ESCOLHIDAS:
        m = np.mean([int(x[nm]) for x in d]); print(f"  {nm:15s} n={n} média {m:.3f} z={(m-10)/(2.01/np.sqrt(n)):+.2f}")

if __name__ == "__main__":
    prever(int(sys.argv[2])) if sys.argv[1] == "prever" else conferir(int(sys.argv[2]), sys.argv[3])
