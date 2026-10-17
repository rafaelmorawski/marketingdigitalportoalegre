# -*- coding: utf-8 -*-
"""Carrega o histórico da Lotomania (planilha da Caixa em CSV + sorteios novos em data/extras.csv)."""
import csv
import os

import numpy as np

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def caminho(*partes):
    return os.path.join(RAIZ, *partes)


def _ler_csv_caixa(path):
    with open(path, encoding="latin1", newline="") as f:
        linhas = [r for r in csv.reader(f)][1:]
    saida = []
    for r in linhas:
        if r and r[0].strip().isdigit():
            saida.append((int(r[0]), r[1], [int(v) for v in r[2:22]]))
    return saida


def _ler_extras(path):
    if not path or not os.path.exists(path):
        return []
    saida = []
    with open(path, encoding="utf-8", newline="") as f:
        for r in list(csv.reader(f))[1:]:
            if r and r[0].strip().isdigit():
                nums = [int(x) for x in r[2].replace(",", " ").split()]
                if len(nums) != 20 or len(set(nums)) != 20 or min(nums) < 0 or max(nums) > 99:
                    raise ValueError(f"extras.csv: sorteio {r[0]} inválido (20 dezenas distintas entre 00 e 99)")
                saida.append((int(r[0]), r[1], nums))
    return saida


def carregar_historico(csv_path=None, extras_path=None):
    """Retorna dict com concursos, datas, dezenas (lista de listas) e D (N x 100, int8)."""
    csv_path = csv_path or caminho("data", "Lotomania.csv")
    extras_path = caminho("data", "extras.csv") if extras_path is None else extras_path
    base = _ler_csv_caixa(csv_path)
    ja = {c for c, _, _ in base}
    todos = base + [e for e in _ler_extras(extras_path) if e[0] not in ja]
    todos.sort(key=lambda x: x[0])
    D = np.zeros((len(todos), 100), dtype=np.int8)
    for i, (_, _, nums) in enumerate(todos):
        D[i, nums] = 1
    return {"concursos": [c for c, _, _ in todos], "datas": [d for _, d, _ in todos],
            "dezenas": [n for _, _, n in todos], "D": D}


def estado_ciclo(D, concursos, inicio=2978):
    """Dezenas que ainda não saíram no ciclo iniciado no concurso `inicio` (reinicia ao completar 100)."""
    visto = np.zeros(100, dtype=bool)
    pos = 0
    for c, linha in zip(concursos, D):
        if c < inicio:
            continue
        visto |= linha.astype(bool)
        pos += 1
        if visto.all():
            visto[:] = False
            pos = 0
    faltam = [int(n) for n in np.flatnonzero(~visto)]
    return {"faltam": faltam, "posicao": pos, "completo": len(faltam) == 100 or len(faltam) == 0}
