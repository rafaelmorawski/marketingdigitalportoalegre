# -*- coding: utf-8 -*-
"""Bateria pré-registrada: 24 estatísticas de cada sorteio (historico real vs 100 mil sorteios uniformes).
Teste KS de duas amostras por estatística; limiar de Bonferroni para 24 testes (alfa 0,05 => p < 0,0021)."""
import numpy as np
from scipy.stats import ks_2samp, chi2
from dados import carregar_historico
from ferramentas import sorteios_simulados

def stats(D):
    n = len(D); idx = np.arange(100); out = {}
    D = D.astype(np.int16)
    out["pares"] = D[:, idx % 2 == 0].sum(1)
    out["soma"] = (D * idx).sum(1)
    out["consecutivos(i,i+1)"] = (D[:, :-1] & D[:, 1:]).sum(1)
    out["mesma coluna(d%10) max"] = np.stack([D[:, idx % 10 == c].sum(1) for c in range(10)], 1).max(1)
    out["mesma década max"] = np.stack([D[:, idx // 10 == c].sum(1) for c in range(10)], 1).max(1)
    out["mesma década min"] = np.stack([D[:, idx // 10 == c].sum(1) for c in range(10)], 1).min(1)
    out["dezenas 00-49"] = D[:, :50].sum(1)
    out["quadrantes (min)"] = np.stack([D[:, [r*10+c for r in rows for c in cols]].sum(1)
                                        for rows in (range(0,5), range(5,10)) for cols in (range(0,5), range(5,10))], 1).min(1)
    out["borda do volante"] = D[:, [d for d in range(100) if d//10 in (0,9) or d%10 in (0,9)]].sum(1)
    out["diagonal principal"] = D[:, [i*11 for i in range(10)]].sum(1)
    out["múltiplos de 3"] = D[:, idx % 3 == 0].sum(1)
    out["primos"] = D[:, [d for d in range(2,100) if all(d%k for k in range(2,int(d**.5)+1))]].sum(1)
    out["quadrados perfeitos"] = D[:, [0,1,4,9,16,25,36,49,64,81]].sum(1)
    out["terminam 0 ou 5"] = D[:, idx % 5 == 0].sum(1)
    out["linhas vazias(década sem dezena)"] = (np.stack([D[:, idx // 10 == c].sum(1) for c in range(10)], 1) == 0).sum(1)
    out["colunas vazias"] = (np.stack([D[:, idx % 10 == c].sum(1) for c in range(10)], 1) == 0).sum(1)
    out["maior sequência de vizinhas"] = np.array([max((len(s) for s in "".join(map(str, r)).split("0")), default=0) for r in D])
    out["diferença média entre ordenadas"] = np.array([np.diff(np.flatnonzero(r)).mean() for r in D])
    out["maior buraco entre sorteadas"] = np.array([np.diff(np.flatnonzero(r)).max() for r in D])
    out["menor dezena"] = np.array([np.flatnonzero(r)[0] for r in D])
    out["maior dezena"] = np.array([np.flatnonzero(r)[-1] for r in D])
    out["número de pares adjacentes na coluna"] = (D[:, :-10] & D[:, 10:]).sum(1)
    out["pares em 00-49 menos pares em 50-99"] = D[:, :50][:, ::2].sum(1) - D[:, 50:][:, ::2].sum(1)
    out["paridade igual à do sorteio anterior"] = np.r_[0, (out["pares"][1:] == out["pares"][:-1]).astype(int)]
    return out

def main():
    D = carregar_historico()["D"]; S = sorteios_simulados(100_000, 4242).astype(np.int8)
    a, b = stats(D), stats(S)
    k = len(a); lim = 0.05 / k
    print(f"{len(D)} sorteios reais vs 100.000 simulados | {k} testes | limiar Bonferroni p < {lim:.4f}\n")
    print(f"{'estatística':40s} {'média real':>10s} {'média unif.':>11s} {'KS p':>8s}")
    for nome in a:
        p = ks_2samp(a[nome], b[nome]).pvalue
        flag = "  <-- passa" if p < lim else ""
        print(f"{nome:40s} {a[nome].mean():10.3f} {b[nome].mean():11.3f} {p:8.4f}{flag}")
    # paridade: distribuição do número de pares vs hipergeométrica (chi2)
    from scipy.stats import hypergeom
    obs = np.bincount(a["pares"], minlength=21)[:21]; esp = hypergeom.pmf(np.arange(21), 100, 50, 20) * len(D)
    m = esp >= 5; c2 = ((obs[m] - esp[m]) ** 2 / esp[m]).sum(); df = m.sum() - 1
    print(f"\nChi² do nº de pares no sorteio vs hipergeométrica: {c2:.1f} (gl {df}), p = {chi2.sf(c2, df):.3f}")
    print("Distribuição observada de pares:", {int(i): int(obs[i]) for i in range(5, 16)})
    print("Fração com exatamente 10 pares: real %.3f | esperado %.3f" % (obs[10] / len(D), hypergeom.pmf(10, 100, 50, 20)))

if __name__ == "__main__":
    main()
