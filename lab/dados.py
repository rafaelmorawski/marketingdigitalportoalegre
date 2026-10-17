import csv
import numpy as np

def carregar(caminho="data/historico.csv"):
    """Retorna (concursos, datas, M) com M de forma (n,100) em 0/1."""
    cs, ds, linhas = [], [], []
    with open(caminho) as f:
        for r in csv.DictReader(f):
            cs.append(int(r["concurso"])); ds.append(r["data"])
            v = np.zeros(100, dtype=np.int8)
            for i in range(1, 21):
                v[int(r[f"B{i}"])] = 1
            linhas.append(v)
    return np.array(cs), ds, np.array(linhas)
