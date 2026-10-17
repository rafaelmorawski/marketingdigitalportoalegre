#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conferência de um resultado contra os jogos apostados, por grupo.

  python3 lab/conferir.py --concurso 2988 --dezenas "07 12 ... 99"
  python3 lab/conferir.py --concurso 2987 --sem-ledger          # reconfere um sorteio que já está em data/extras.csv

O que faz:
  1. Acerta cada jogo (mínimo, máximo e média) e resume POR GRUPO: melhor placar e média do grupo.
  2. Atualiza o ciclo (quantas faltavam, quais saíram, quais faltam) e as repetidas do sorteio anterior.
  3. Registra uma linha por grupo em data/ledger_grupos.csv e escreve relatorios/C<concurso>.md.
Se o concurso ainda não estiver em data/extras.csv, ele é acrescentado (mantém o histórico crescendo).
Leitura honesta: um sorteio só não distingue um grupo de outro (seriam ~170 para dois erros-padrão);
esperado: média por jogo 10,0 e melhor de um grupo de 10 jogos ~13,2.
"""
import argparse
import csv
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dados import caminho, carregar_historico, estado_ciclo  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--concurso", type=int, required=True)
    ap.add_argument("--dezenas", help="as 20 dezenas do resultado (se ainda não estiver em data/extras.csv)")
    ap.add_argument("--data", default="", help="data do sorteio dd/mm/aaaa (opcional)")
    ap.add_argument("--jogos", default=caminho("data", "jogos_C2988.json"))
    ap.add_argument("--sem-ledger", action="store_true", help="não grava no ledger nem acrescenta ao extras.csv")
    a = ap.parse_args()

    h = carregar_historico()
    conc = a.concurso
    if conc in h["concursos"]:
        i = h["concursos"].index(conc)
        res = set(h["dezenas"][i])
        D_antes, c_antes = h["D"][:i], h["concursos"][:i]
    else:
        if not a.dezenas:
            sys.exit(f"C{conc} não está no histórico: passe --dezenas com as 20 dezenas")
        nums = [int(x) for x in a.dezenas.replace(",", " ").split()]
        if len(nums) != 20 or len(set(nums)) != 20 or min(nums) < 0 or max(nums) > 99:
            sys.exit("--dezenas precisa de 20 dezenas distintas entre 00 e 99")
        res = set(nums)
        D_antes, c_antes = h["D"], h["concursos"]
        if not a.sem_ledger:
            novo = not os.path.exists(caminho("data", "extras.csv"))
            with open(caminho("data", "extras.csv"), "a", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                if novo:
                    w.writerow(["concurso", "data", "dezenas"])
                w.writerow([conc, a.data, " ".join(f"{x:02d}" for x in sorted(nums))])

    antes = estado_ciclo(D_antes, c_antes)
    anterior = {int(x) for x in np.flatnonzero(D_antes[-1])}
    saiu_ciclo = sorted(res & set(antes["faltam"]))
    depois = sorted(set(antes["faltam"]) - res) if not antes["completo"] else antes["faltam"]

    cfg = json.load(open(a.jogos, encoding="utf-8"))
    linhas, ledger = [], []
    todos = []
    for g in cfg["grupos"]:
        acertos = {j["nome"]: len(set(j["dezenas"]) & res) for j in g["jogos"]}
        v = list(acertos.values())
        todos += v
        linhas.append((g["id"], g["nome"], len(v), max(v), float(np.mean(v)), acertos))
        ledger.append((conc, g["id"], len(v), max(v), round(float(np.mean(v)), 2), ""))

    texto = [f"# Conferência do C{conc}", "",
             f"Resultado: {' '.join(f'{x:02d}' for x in sorted(res))} (soma {sum(res)}, {sum(1 for x in res if x % 2 == 0)} pares)", "",
             "| Grupo | Jogos | Melhor | Média | Acertos por jogo |", "|---|---|---|---|---|"]
    for gid, nome, n, mx, mean, ac in linhas:
        texto.append(f"| {gid} — {nome} | {n} | {mx} | {mean:.2f} | {', '.join(f'{k}:{v}' for k, v in ac.items())} |")
    texto += ["", f"Todos os {len(todos)} jogos: melhor {max(todos)}, média {np.mean(todos):.2f} (esperado 10,00).", "",
              f"## Ciclo (iniciado em C2978)",
              f"- Antes do sorteio faltavam {len(antes['faltam'])}: {' '.join(f'{x:02d}' for x in antes['faltam'])}",
              f"- Saíram {len(saiu_ciclo)} delas: {' '.join(f'{x:02d}' for x in saiu_ciclo) or '—'} (esperado {0.2 * len(antes['faltam']):.1f})",
              f"- Faltam agora {len(depois)}: {' '.join(f'{x:02d}' for x in depois)}",
              f"- Repetidas do sorteio anterior: {len(res & anterior)} {' '.join(f'{x:02d}' for x in sorted(res & anterior))} (esperado 4,0)", ""]
    print("\n".join(texto))
    os.makedirs(caminho("relatorios"), exist_ok=True)
    open(caminho("relatorios", f"C{conc}.md"), "w", encoding="utf-8").write("\n".join(texto))
    if not a.sem_ledger:
        lp = caminho("data", "ledger_grupos.csv")
        existentes = set()
        if os.path.exists(lp):
            existentes = {(r[0], r[1]) for r in list(csv.reader(open(lp, encoding="utf-8")))[1:]}
        with open(lp, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            for r in ledger:
                if (str(r[0]), r[1]) not in existentes:
                    w.writerow(r)
        print(f"Ledger atualizado: {lp}")


if __name__ == "__main__":
    main()
