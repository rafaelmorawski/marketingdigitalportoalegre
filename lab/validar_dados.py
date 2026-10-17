# -*- coding: utf-8 -*-
"""Integridade dos dados: concursos contíguos, 20 dezenas distintas em 00–99, datas crescentes, planilha × historico.csv × ordem."""
import csv, os, sys
from datetime import datetime
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(RAIZ, "lab"))
from dados import carregar_historico

def verificar():
    erros, avisos = [], []
    h = carregar_historico(); cs, ds, dz = h["concursos"], h["datas"], h["dezenas"]
    if cs != list(range(cs[0], cs[0] + len(cs))): erros.append("concursos não contíguos")
    for c, d in zip(cs, dz):
        if len(set(d)) != 20 or min(d) < 0 or max(d) > 99: erros.append(f"C{c}: dezenas inválidas")
    dt = [datetime.strptime(x, "%d/%m/%Y") for x in ds]
    if any(b < a for a, b in zip(dt, dt[1:])): erros.append("datas fora de ordem")
    if len({tuple(sorted(d)) for d in dz}) != len(dz): erros.append("sorteios idênticos encontrados")
    ref = os.path.join(RAIZ, "data", "historico.csv")
    if os.path.exists(ref):
        api = {int(r["concurso"]): sorted(int(r[f"B{i}"]) for i in range(1, 21)) for r in csv.DictReader(open(ref))}
        dif = [c for c, d in zip(cs, dz) if c in api and sorted(d) != api[c]]
        if dif: erros.append(f"{len(dif)} concursos divergem da API (ex.: C{dif[0]})")
        falt = [c for c in cs if c not in api]
        if falt: avisos.append(f"{len(falt)} concursos fora de historico.csv (ex.: C{falt[0]})")
    ordem = os.path.join(RAIZ, "data", "historico_ordem.csv")
    if os.path.exists(ordem):
        o = {int(r[0]): sorted(int(x) for x in r[2:22]) for r in list(csv.reader(open(ordem)))[1:]}
        dif = [c for c, d in zip(cs, dz) if c in o and sorted(d) != o[c]]
        if dif: erros.append(f"{len(dif)} concursos divergem da ordem de saída")
    return erros, avisos, len(cs), cs[-1]

if __name__ == "__main__":
    e, a, n, ult = verificar()
    print(f"{n} sorteios até C{ult}"); [print("AVISO:", x) for x in a]; [print("ERRO:", x) for x in e]
    print("dados OK" if not e else "dados com problemas"); sys.exit(1 if e else 0)
