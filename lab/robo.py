# -*- coding: utf-8 -*-
"""Robô operacional do laboratório (automação, não previsão).
Fluxo da seção 7 do CLAUDE.md, sem intervenção: busca o último resultado na API da Caixa; se houver concurso novo,
confere os jogos por grupo (+ grupo K10 se existir), atualiza ledger/ciclo/extras, roda o painel de predição, confere e
renova o pré-registro das lentes, e escreve relatorios/ROBO_C<n>.md.
  python3 lab/robo.py            # opera
  python3 lab/robo.py --dry-run  # só mostra o que faria
  python3 lab/robo.py --concurso 2989 --dezenas "..."  # sem API (se estiver fora do ar)"""
import argparse, csv, glob, json, os, re, subprocess, sys, urllib.error, urllib.request
import numpy as np

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = "https://servicebus2.caixa.gov.br/portaldeloterias/api/lotomania/"

def caminho(*p): return os.path.join(RAIZ, *p)

def api(n=""):
    try:
        with urllib.request.urlopen(URL + str(n), timeout=30) as r: d = json.load(r)
    except urllib.error.HTTPError:   # concurso ainda não publicado (a API responde 404/500)
        return None
    if not d.get("numero"): return None
    return int(d["numero"]), d["dataApuracao"], " ".join(sorted(d["listaDezenas"])), d

def ultimo_no_ledger():
    f = caminho("data", "ledger_grupos.csv")
    return max((int(r["concurso"]) for r in csv.DictReader(open(f, encoding="utf-8"))), default=0)

def jogos_do_concurso(n):
    """jogos_C<n>.json se existir; senão a grade vigente mais recente (mantém a grade)."""
    exato = caminho("data", f"jogos_C{n}.json")
    if os.path.exists(exato): return exato
    cand = sorted((int(re.findall(r"C(\d+)\.json", f)[0]), f) for f in glob.glob(caminho("data", "jogos_C[0-9]*.json"))
                  if re.search(r"C\d+\.json$", f))
    return [f for k, f in cand if k <= n][-1]

def conferir_k10(n, dezenas):
    f = caminho("data", f"jogos_C{n}_K10.json")
    if not os.path.exists(f): return None
    K = json.load(open(f, encoding="utf-8"))["jogos"]; r = set(int(x) for x in dezenas.split())
    ac = {k: len(r & set(v)) for k, v in K.items()}
    return ac, max(ac.values()), float(np.mean(list(ac.values())))

def rodar(cmd):
    p = subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True)
    return (p.stdout + p.stderr).strip()

def processar(n, data, dez, dry):
    jogos = jogos_do_concurso(n)
    print(f"Concurso novo: C{n} ({data}) {dez}\nGrade usada: {os.path.relpath(jogos, RAIZ)}")
    if dry: print("(dry-run: nada foi gravado)"); return
    out = ["# Robô — conferência do C%d (%s)" % (n, data), "", f"Resultado: {dez}", ""]
    out += ["## Conferência por grupo", rodar([sys.executable, "lab/conferir.py", "--concurso", str(n), "--dezenas", dez,
                                              "--data", data, "--jogos", jogos])]
    k = conferir_k10(n, dez)
    if k:
        ac, mel, med = k
        with open(caminho("data", "ledger_grupos.csv"), "a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([n, "K10", 10, mel, round(med, 2), "cobertura otimizada (3 bancos)"])
        out += ["", "## Grupo K10", f"melhor {mel}, média {med:.2f} (esperado 10,00 e melhor de 10 ≈ 13,2)", str(ac)]
    if os.path.exists(caminho("data", "lentes_previsoes.json")) and str(n) in json.load(open(caminho("data", "lentes_previsoes.json"))):
        out += ["", "## Lente pré-registrada (forward)", rodar([sys.executable, "lab/lentes_forward.py", "conferir", str(n), dez])]
    painel = rodar([sys.executable, "lab/painel_predicao.py", "--csv", "data/Lotomania.csv",
                    "--extras-file", "data/extras.csv", "--log", "data/painel_log.csv"])
    out += ["", "## Painel de predição", "\n".join(painel.splitlines()[-5:])]
    rodar([sys.executable, "lab/semaforo.py"])
    out += ["", "## Semáforos", f"Painel atualizado em relatorios/SEMAFORO_C{n}.md (nenhuma hipótese do painel está confirmada)."]
    out += ["", "## Pré-registro do próximo concurso", rodar([sys.executable, "lab/lentes_forward.py", "prever", str(n + 1)])]
    out += ["", "Nada aqui prevê o sorteio; ver seção 10 do CLAUDE.md."]
    rel = caminho("relatorios", f"ROBO_C{n}.md"); open(rel, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\n".join(out)); print("\nRelatório:", os.path.relpath(rel, RAIZ))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--concurso", type=int); ap.add_argument("--dezenas")
    ap.add_argument("--data", default="")
    a = ap.parse_args()
    if a.concurso and a.dezenas:
        pend = [(a.concurso, a.data, a.dezenas)] if a.concurso > ultimo_no_ledger() else []
    else:   # o endpoint "último" da Caixa atrasa; consulta o seguinte ao do ledger, um a um
        pend, n = [], ultimo_no_ledger() + 1
        while True:
            r = api(n)
            if not r: break
            pend.append(r[:3]); n += 1
    if not pend: print(f"Nada novo: ledger já tem até C{ultimo_no_ledger()} e a API ainda não publicou o seguinte."); return
    for n, data, dez in pend: processar(n, data, dez, a.dry_run)

if __name__ == "__main__":
    main()
