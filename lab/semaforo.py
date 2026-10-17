# -*- coding: utf-8 -*-
"""Painel de semáforos pré-registrado (relatorios/PREREG_semaforos.md)."""
import sys, os
import numpy as np
from scipy.stats import norm, chi2
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(RAIZ, "lab"))
from dados import carregar_historico
from ferramentas import sorteios_simulados

PRIMOS = [d for d in range(2, 100) if all(d % k for k in range(2, int(d ** .5) + 1))]
BORDA = [d for d in range(100) if d // 10 in (0, 9) or d % 10 in (0, 9)]

def run_max(D):
    r, k, mx = D.astype(bool), 1, np.zeros(len(D), int)
    while r.any():
        mx[r.any(1)] = k; r = r[:, :-1] & D[:, k:].astype(bool); k += 1
    return mx

def indicadores(D):
    D = D.astype(np.int8); N = len(D); idx = np.arange(100); G = D.reshape(N, 10, 10); ix = np.nonzero(D)[1].reshape(N, 20)
    o = {}
    o["pares"] = D[:, ::2].sum(1); o["soma"] = ix.sum(1); o["acima50"] = D[:, 50:].sum(1)
    o["décadas vazias"] = (G.sum(2) == 0).sum(1); o["colunas vazias"] = (G.sum(1) == 0).sum(1)
    o["máx por década"] = G.sum(2).max(1); o["mín por década"] = G.sum(2).min(1); o["máx por coluna"] = G.sum(1).max(1)
    o["consecutivos"] = (D[:, :-1] & D[:, 1:]).sum(1); o["maior sequência"] = run_max(D)
    o["vizinhas linha"] = (G[:, :, :-1] & G[:, :, 1:]).sum((1, 2)); o["vizinhas coluna"] = (G[:, :-1] & G[:, 1:]).sum((1, 2))
    o["vizinhas diagonal"] = (G[:, :-1, :-1] & G[:, 1:, 1:]).sum((1, 2)) + (G[:, :-1, 1:] & G[:, 1:, :-1]).sum((1, 2))
    o["vizinhos-8 (agrupamento)"] = o["vizinhas linha"] + o["vizinhas coluna"] + o["vizinhas diagonal"]
    o["repetidas do anterior"] = np.r_[np.nan, (D[1:] & D[:-1]).sum(1)]
    o["maior buraco"] = np.diff(ix, axis=1).max(1); o["amplitude"] = ix[:, -1] - ix[:, 0]; o["desvio das dezenas"] = ix.std(1)
    o["borda"] = D[:, BORDA].sum(1); o["primos"] = D[:, PRIMOS].sum(1); o["múltiplos de 3"] = D[:, ::3].sum(1); o["múltiplos de 5"] = D[:, ::5].sum(1)
    q = [D[:, [r * 10 + c for r in rs for c in cs]].sum(1) for rs in (range(5), range(5, 10)) for cs in (range(5), range(5, 10))]
    o["quadrante mínimo"] = np.min(q, 0); o["pares inferior−superior"] = D[:, :50:2].sum(1) - D[:, 50::2].sum(1)
    o["dezenas ≤31"] = D[:, :32].sum(1)
    rep = np.r_[np.zeros((1, 100), np.int8), D[1:] & D[:-1]]; o["repetidas na maior década"] = rep.reshape(N, 10, 10).sum(2).max(1).astype(float); o["repetidas na maior década"][0] = np.nan
    return {k: np.asarray(v, float) for k, v in o.items()}

EVENTOS = {"década vazia": ("décadas vazias", ">=", 1), "2+ décadas vazias": ("décadas vazias", ">=", 2), "sequência ≥4": ("maior sequência", ">=", 4),
           "pares ≥13": ("pares", ">=", 13), "pares ≤7": ("pares", "<=", 7), "acima50 ≥13": ("acima50", ">=", 13), "acima50 ≤7": ("acima50", "<=", 7),
           "soma ≥ decil 90": ("soma", "q90", None), "soma ≤ decil 10": ("soma", "q10", None), "repetidas ≥8": ("repetidas do anterior", ">=", 8),
           "repetidas ≤1": ("repetidas do anterior", "<=", 1), "2+ colunas vazias": ("colunas vazias", ">=", 2)}

def evento(x, op, v, q):
    if op == ">=": return x >= v
    if op == "<=": return x <= v
    return x >= q["q90"] if op == "q90" else x <= q["q10"]

if __name__ == "__main__":
    hist = carregar_historico(); D = hist["D"]; N = len(D); X = indicadores(D)
    SIM = indicadores(sorteios_simulados(300_000, 99).astype(np.int8)); h = N // 2
    res, linhas = {}, []
    for k, x in X.items():
        s = SIM[k][1:] if k.startswith("repetid") else SIM[k]; mu, sd = np.nanmean(s), np.nanstd(s); q10, q90 = np.nanquantile(s, .1), np.nanquantile(s, .9)
        y = x[1:] if np.isnan(x[0]) else x
        zs = (y - mu) / sd; n = len(zs); r = [np.corrcoef(zs[:-l], zs[l:])[0, 1] for l in range(1, 11)]
        Q = n * (n + 2) * sum(ri ** 2 / (n - l) for l, ri in zip(range(1, 11), r)); pA = chi2.sf(Q, 10)
        def cond(mask):
            m = mask[:-1]; nn = m.sum(); nxt = y[1:][m]; z = (nxt.mean() - mu) / (sd / np.sqrt(nn)); return z, nn
        zB, nB = cond(y >= q90); zC, nC = cond(y <= q10)
        def rep(mask):
            out = []
            for a, b in ((0, len(y) // 2), (len(y) // 2, len(y))):
                m = mask[a:b][:-1]; nxt = y[a:b][1:][m]; out.append((nxt.mean() - mu) / (sd / np.sqrt(m.sum())))
            return out
        res[k] = dict(pA=pA, zB=zB, zC=zC, repB=rep(y >= q90), repC=rep(y <= q10), mu=mu, sd=sd, q10=q10, q90=q90, atual=x[-1], y=y)
    haz = {}
    for nome, (ind, op, v) in EVENTOS.items():
        s = SIM[ind][1:] if ind.startswith("repetid") else SIM[ind]; qq = {"q10": np.quantile(s, .1), "q90": np.quantile(s, .9)}
        pe = evento(s, op, v, qq).mean(); y = X[ind][1:] if np.isnan(X[ind][0]) else X[ind]; ev = evento(y, op, v, qq)
        m = int(np.ceil(np.log(0.25) / np.log(1 - pe))); gap = 0; aprox = []
        for t in range(len(ev)):
            if gap >= m: aprox.append(ev[t])
            gap = 0 if ev[t] else gap + 1
        aprox = np.array(aprox); z = (aprox.mean() - pe) / np.sqrt(pe * (1 - pe) / len(aprox))
        atual = 0; 
        for e in ev[::-1]:
            if e: break
            atual += 1
        haz[nome] = dict(pe=pe, m=m, n=len(aprox), taxa=aprox.mean(), z=z, atual=atual)
    nt = 3 * len(res) + len(haz); lim = 0.05 / nt; zl = norm.isf(lim / 2)
    print(f"{N} sorteios | {len(res)} indicadores | {nt} testes | Bonferroni p < {lim:.5f} (|z| > {zl:.2f})\n")
    print(f"{'indicador':30s} {'LB p':>7s} {'z após alto':>12s} {'z após baixo':>13s}")
    melhores = []
    for k, r in res.items():
        print(f"{k:30s} {r['pA']:7.3f} {r['zB']:+12.2f} {r['zC']:+13.2f}"); melhores += [(abs(r['zB']), k, 'alto'), (abs(r['zC']), k, 'baixo'), (norm.isf(r['pA']/2) if False else 0, k, 'LB')]
    print("\nTEMPO DE OCORRÊNCIA (depois de m sorteios sem o evento, a taxa sobe?)")
    print(f"{'evento':20s} {'p base':>7s} {'m':>3s} {'n':>5s} {'taxa':>7s} {'z':>7s} {'sem ocorrer há':>15s}")
    for nome, r in haz.items(): print(f"{nome:20s} {r['pe']:7.3f} {r['m']:3d} {r['n']:5d} {r['taxa']:7.3f} {r['z']:+7.2f} {r['atual']:10d} sorteios")
    mz = max([(abs(r['zB']), k, 'alto') for k, r in res.items()] + [(abs(r['zC']), k, 'baixo') for k, r in res.items()] + [(abs(r['z']), k, 'tempo') for k, r in haz.items()])
    mp = min((r['pA'], k) for k, r in res.items())
    print(f"\nmaior |z| entre {3*len(res)-len(res)+len(haz)} testes condicionais: {mz[0]:.2f} ({mz[1]}, {mz[2]}) | limiar {zl:.2f}")
    print(f"menor p de Ljung-Box entre {len(res)}: {mp[0]:.4f} ({mp[1]}) | limiar {lim:.5f}")
    # ---------- painel do estado atual ----------
    ultimo = hist["concursos"][-1]; linhas = [f"# Painel de semáforos — estado no C{ultimo}", "",
        f"Nulo: sorteio uniforme (300 mil simulados). Limiar de evidência: |z| > {zl:.2f} ({nt} testes, Bonferroni). **Nenhuma hipótese abaixo está confirmada: o selo existe para isso.**", "",
        "| | Indicador | Valor | Normal (média±dp) | z | Sequência do mesmo lado | Hipótese apontada | Evidência histórica |", "|---|---|---|---|---|---|---|---|"]
    ordem = sorted(res.items(), key=lambda kv: -abs((kv[1]["atual"] - kv[1]["mu"]) / kv[1]["sd"]))
    for k, r in ordem:
        z = (r["atual"] - r["mu"]) / r["sd"]; cor = "🔴" if abs(z) > 2 else "🟡" if abs(z) > 1.5 else "🟢"
        lado = np.sign(r["y"] - r["mu"]); st = 0
        for v in lado[::-1]:
            if v == lado[-1] and v != 0: st += 1
            else: break
        alto = z > 0; zc = r["zB"] if alto else r["zC"]
        hip = ("voltar à média no próximo" if zc * (1 if alto else -1) < 0 else "repetir o lado no próximo") if abs(z) > 1.5 else "—"
        evid = f"após {'alto' if alto else 'baixo'}: z={zc:+.2f}; LB p={r['pA']:.2f} → não confirmada" if abs(z) > 1.5 else "—"
        linhas.append(f"| {cor} | {k} | {r['atual']:.0f} | {r['mu']:.1f}±{r['sd']:.1f} | {z:+.2f} | {st} sorteio(s) {'acima' if lado[-1] > 0 else 'abaixo'} | {hip} | {evid} |")
    linhas += ["", "## Tempo de ocorrência (há quanto tempo cada evento não acontece)", "",
               "| Evento | Prob. por sorteio | Sem ocorrer há | Depois de m sorteios sem o evento, a taxa sobe? | Evidência |", "|---|---|---|---|---|"]
    for nome, r in sorted(haz.items(), key=lambda kv: -kv[1]["atual"] * kv[1]["pe"]):
        cor = "🔴" if r["atual"] >= 2 * r["m"] else "🟡" if r["atual"] >= r["m"] else "🟢"
        linhas.append(f"| {cor} {nome} | {r['pe']:.3f} | {r['atual']} sorteios (m={r['m']}) | taxa {r['taxa']:.3f} vs {r['pe']:.3f}, z={r['z']:+.2f} | não confirmada (limiar {zl:.2f}) |")
    linhas += ["", "## Como ler", "- 🟢 normal (|z|<1,5) · 🟡 atenção (1,5–2) · 🔴 extremo (>2). Extremo acontece sozinho: com 26 indicadores, em torno de 1 deles fica 🔴 em qualquer sorteio.",
               "- A hipótese é só a direção observada no histórico; nenhuma passou o limiar e nenhuma replicou. Não use para escolher dezenas.", ""]
    open(os.path.join(RAIZ, "relatorios", f"SEMAFORO_C{ultimo}.md"), "w", encoding="utf-8").write("\n".join(linhas) + "\n"); print("\n".join(linhas[:22]))
    import json; json.dump({"res": {k: {kk: (vv if not isinstance(vv, np.ndarray) else None) for kk, vv in r.items()} for k, r in res.items()}, "haz": haz, "lim": lim, "zl": float(zl)},
                              open(os.path.join(RAIZ, "data", "semaforo_estado.json"), "w"), default=float, ensure_ascii=False)
