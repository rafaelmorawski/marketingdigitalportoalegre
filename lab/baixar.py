"""Baixa o histórico da Lotomania da API pública da Caixa para data/historico.csv."""
import csv, json, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

URL = "https://servicebus2.caixa.gov.br/portaldeloterias/api/lotomania/{}"

def um(n, tent=5):
    for t in range(tent):
        try:
            with urllib.request.urlopen(URL.format(n), timeout=30) as r:
                d = json.load(r)
            if d.get("numero") != n:
                return None
            return n, d["dataApuracao"], sorted(int(x) for x in d["listaDezenas"])
        except Exception:
            time.sleep(1.5 * (t + 1))
    raise RuntimeError(f"falhou {n}")

def main(ate, saida):
    with ThreadPoolExecutor(8) as ex:
        res = [r for r in ex.map(um, range(1, ate + 1)) if r]
    with open(saida, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["concurso", "data"] + [f"B{i}" for i in range(1, 21)])
        for n, d, dz in sorted(res):
            w.writerow([n, d] + dz)
    print(len(res), "concursos gravados em", saida)

if __name__ == "__main__":
    main(int(sys.argv[1]), sys.argv[2])
