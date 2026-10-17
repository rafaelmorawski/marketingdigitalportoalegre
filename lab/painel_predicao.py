#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PAINEL DE TESTE DE PREDIÇÃO — LOTOMANIA
=======================================
Pergunta que o painel responde, a cada resultado novo:
    "Algum modelo de ML consegue prever quais dezenas saem, em sorteios que
     nunca viu?"

Como funciona
  - Lê o histórico (CSV exportado da planilha da Caixa: concurso, data e as
    20 dezenas nas colunas 3 a 22) e, opcionalmente, sorteios novos passados
    com --extra "07 12 20 ... 99" (20 dezenas, pode repetir a opção).
  - Monta 28 variáveis por (sorteio, dezena), SÓ com informação anterior ao
    sorteio: presença nos últimos 10 sorteios, frequência em janelas de
    5/10/20/50/100/300, frequência total, tempo sem sair, se já saiu no ciclo
    atual, posição no ciclo, número/década/paridade/resto por 5 e por 10,
    soma e pares do último sorteio, repetidas entre os dois últimos.
  - Treina em tudo que vem ANTES dos últimos --test-draws sorteios e testa nos
    últimos --test-draws (sorteios que o modelo nunca viu).
  - Modelos: gradiente boosting, regressão logística e um CONTROLE (o mesmo
    gradiente boosting treinado com rótulos embaralhados, que mostra quanto o
    ruído sozinho rende).
  - Métricas: AUC (acaso = 0,5000), log-loss contra a taxa-base e, por sorteio,
    os acertos do top-50 (esperado 10,000) e do top-20 (esperado 4,000), com z.

Como ler
  - Sem sinal: AUC ~0,500, top-50 ~10,00 e |z| pequeno, igual ao controle.
  - Só considere um desvio se: |z| do top-50 passar de ~2,6 (correção para
    vários modelos/rodadas), AUC ficar acima do controle de forma consistente
    e o desvio se REPETIR em dados novos. Um único z alto, rodando a cada
    resultado, é esperado por acaso de tempos em tempos.
  - Cada rodada acrescenta uma linha ao arquivo de log (--log).

Uso
  python3 painel_predicao.py --csv Lotomania.csv
  python3 painel_predicao.py --csv Lotomania.csv --extra "07 12 20 29 31 32 39 43 44 48 50 52 60 61 69 84 85 90 91 99"

Requisitos: numpy, scikit-learn.
Resultado de referência (C300–C1999 treino, C2000–C2986 teste): AUC 0,4992
(boosting) e 0,4988 (logística); top-50 = 9,990 e 9,997; controle 0,4986 / 9,970.
"""
import argparse
import csv
import datetime
import os
import sys

import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss, roc_auc_score
from sklearn.preprocessing import StandardScaler

JANELAS = (5, 10, 20, 50, 100, 300)


def carregar(caminho, extras, extras_file=None):
    """Planilha da Caixa + sorteios novos (de --extras-file, só os que a planilha ainda não tem, e de --extra)."""
    with open(caminho, encoding="latin1", newline="") as f:
        linhas = [r for r in csv.reader(f)][1:]
    linhas = [r for r in linhas if r and r[0].strip().isdigit()]
    linhas.sort(key=lambda r: int(r[0]))
    sorteios = [[int(v) for v in r[2:22]] for r in linhas]
    ultimo = int(linhas[-1][0])
    novos = []
    if extras_file and os.path.exists(extras_file):
        with open(extras_file, encoding="utf-8", newline="") as f:
            for r in list(csv.reader(f))[1:]:
                if r and r[0].strip().isdigit() and int(r[0]) > ultimo:
                    novos.append((int(r[0]), r[2]))
        novos.sort()
    lista = [e for _, e in novos] + list(extras)
    for e in lista:
        nums = [int(x) for x in e.replace(",", " ").split()]
        if len(nums) != 20 or len(set(nums)) != 20 or min(nums) < 0 or max(nums) > 99:
            sys.exit("sorteio extra precisa de 20 dezenas distintas entre 00 e 99")
        sorteios.append(nums)
        ultimo += 1
    N = len(sorteios)
    D = np.zeros((N, 100), dtype=np.int8)
    for i, s_ in enumerate(sorteios):
        D[i, s_] = 1
    return D, ultimo


def preparar(D):
    N = len(D)
    cum = np.vstack([np.zeros((1, 100), dtype=int), np.cumsum(D, 0)])
    visto = np.zeros(100, dtype=bool)
    ciclo_visto, ciclo_pos = [None] * N, np.zeros(N)
    inicio = 0
    for t in range(N):
        ciclo_visto[t] = visto.copy()
        ciclo_pos[t] = t - inicio
        visto |= D[t].astype(bool)
        if visto.all():
            visto[:] = False
            inicio = t + 1
    gap = np.zeros((N, 100))
    ultima = np.full(100, -1)
    for t in range(N):
        gap[t] = t - ultima
        ultima[D[t] == 1] = t
    return cum, ciclo_visto, ciclo_pos, gap


def variaveis(t, D, cum, ciclo_visto, ciclo_pos, gap):
    nums = np.arange(100)
    cols = [D[t - k].astype(float) for k in range(1, 11)]
    cols += [(cum[t] - cum[t - w]) / w for w in JANELAS]
    ult = D[t - 1]
    cols += [
        cum[t] / t,
        gap[t],
        ciclo_visto[t].astype(float),
        np.full(100, ciclo_pos[t]),
        nums.astype(float),
        (nums // 10).astype(float),
        (nums % 2).astype(float),
        (nums % 5).astype(float),
        (nums % 10).astype(float),
        np.full(100, (nums * ult).sum() / 100.0),
        np.full(100, float(ult[0::2].sum())),
        np.full(100, float((D[t - 1] & D[t - 2]).sum())),
    ]
    return np.stack(cols, 1)


def avaliar(nome, p, y, y_treino):
    P, Y = p.reshape(-1, 100), y.reshape(-1, 100)
    top50, top20 = [], []
    for i in range(len(P)):
        o = np.argsort(-P[i], kind="stable")
        top50.append(Y[i][o[:50]].sum())
        top20.append(Y[i][o[:20]].sum())
    n = len(P)
    z50 = (np.mean(top50) - 10.0) / (2.006 / np.sqrt(n))
    z20 = (np.mean(top20) - 4.0) / (1.6 / np.sqrt(n))
    auc = roc_auc_score(y, p)
    base = np.full(len(y), y_treino.mean())
    print(f"  {nome:34s} AUC={auc:.4f} | log-loss {log_loss(y, p):.5f} (taxa-base {log_loss(y, base):.5f}) | "
          f"top-50 {np.mean(top50):.3f} (z={z50:+.2f}) | top-20 {np.mean(top20):.3f} (z={z20:+.2f}) | melhor sorteio {max(top50)}")
    return auc, z50


def main():
    ap = argparse.ArgumentParser(description="Painel de teste de predição da Lotomania")
    ap.add_argument("--csv", required=True)
    ap.add_argument("--extra", action="append", default=[], help="20 dezenas de um sorteio novo (repetível)")
    ap.add_argument("--extras-file", default=None,
                    help="CSV com colunas concurso,data,dezenas (ex.: data/extras.csv); entram os concursos que a planilha ainda não tem")
    ap.add_argument("--test-draws", type=int, default=987, help="quantos sorteios finais ficam só para teste")
    ap.add_argument("--inicio", type=int, default=300, help="primeiro sorteio usado (janelas precisam de histórico)")
    ap.add_argument("--log", default="painel_log.csv")
    a = ap.parse_args()

    D, ultimo = carregar(a.csv, a.extra, a.extras_file)
    N = len(D)
    t1 = N - a.test_draws
    if t1 <= a.inicio + 200:
        sys.exit("histórico insuficiente para esse tamanho de teste")
    pre = preparar(D)
    Xtr = np.concatenate([variaveis(t, D, *pre) for t in range(a.inicio, t1)])
    ytr = np.concatenate([D[t] for t in range(a.inicio, t1)])
    Xte = np.concatenate([variaveis(t, D, *pre) for t in range(t1, N)])
    yte = np.concatenate([D[t] for t in range(t1, N)])
    print(f"Histórico: {N} sorteios (até C{ultimo}) | treino: sorteios {a.inicio}–{t1 - 1} "
          f"({len(ytr):,} linhas, {Xtr.shape[1]} variáveis) | teste nunca visto: {t1}–{N - 1} ({len(yte):,} linhas)")

    gb = HistGradientBoostingClassifier(max_iter=250, learning_rate=0.05, max_depth=6,
                                        min_samples_leaf=200, random_state=0).fit(Xtr, ytr)
    auc_gb, z_gb = avaliar("gradiente boosting", gb.predict_proba(Xte)[:, 1], yte, ytr)
    sc = StandardScaler().fit(Xtr)
    lr = LogisticRegression(max_iter=300, C=0.5).fit(sc.transform(Xtr), ytr)
    auc_lr, z_lr = avaliar("regressão logística", lr.predict_proba(sc.transform(Xte))[:, 1], yte, ytr)
    emb = ytr.copy()
    np.random.default_rng(1).shuffle(emb)
    ct = HistGradientBoostingClassifier(max_iter=250, learning_rate=0.05, max_depth=6,
                                        min_samples_leaf=200, random_state=0).fit(Xtr, emb)
    auc_ct, z_ct = avaliar("CONTROLE (rótulos embaralhados)", ct.predict_proba(Xte)[:, 1], yte, ytr)

    veredito = ("SEM SINAL: indistinguível do acaso e do controle."
                if max(abs(z_gb), abs(z_lr)) < 2.6 and max(auc_gb, auc_lr) < 0.5 + 3 * 0.0025
                else "DESVIO: replicar em dados novos antes de qualquer ação (z alto isolado é esperado por acaso).")
    print("\nVEREDITO:", veredito)
    novo = not os.path.exists(a.log)
    with open(a.log, "a", newline="") as f:
        w = csv.writer(f)
        if novo:
            w.writerow(["data", "ultimo_concurso", "sorteios", "auc_boosting", "z_top50_boosting",
                        "auc_logistica", "z_top50_logistica", "auc_controle", "z_top50_controle"])
        w.writerow([datetime.datetime.now().isoformat(timespec="seconds"), ultimo, N,
                    f"{auc_gb:.4f}", f"{z_gb:+.2f}", f"{auc_lr:.4f}", f"{z_lr:+.2f}", f"{auc_ct:.4f}", f"{z_ct:+.2f}"])
    print(f"Linha registrada em {a.log}")


if __name__ == "__main__":
    main()
