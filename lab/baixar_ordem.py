"""Baixa a ORDEM de saída das bolas (dezenasSorteadasOrdemSorteio) de todos os concursos -> data/historico_ordem.csv."""
import csv, json, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
URL = "https://servicebus2.caixa.gov.br/portaldeloterias/api/lotomania/{}"

def um(n):
    for t in range(5):
        try:
            with urllib.request.urlopen(URL.format(n), timeout=30) as r: d = json.load(r)
            return n, d["dataApuracao"], [int(x) for x in d["dezenasSorteadasOrdemSorteio"]]
        except Exception: time.sleep(1.5 * (t + 1))
    raise RuntimeError(n)

if __name__ == "__main__":
    ate, saida = int(sys.argv[1]), sys.argv[2]
    with ThreadPoolExecutor(8) as ex: res = list(ex.map(um, range(1, ate + 1)))
    with open(saida, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["concurso", "data"] + [f"O{i}" for i in range(1, 21)])
        for n, d, o in res: w.writerow([n, d] + o)
    print(len(res), "concursos com ordem gravados")
