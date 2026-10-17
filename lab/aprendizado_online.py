# -*- coding: utf-8 -*-
"""Aprendiz online (hedge / pesos multiplicativos) sobre 14 lentes de hipótese.
A cada sorteio t: usa só o passado para pontuar as 100 dezenas, monta o bilhete top-50 de cada lente e do aprendiz,
confere com o resultado, atualiza os pesos pelo erro. Fases: aprendizado C1001..C2888, teste fora da amostra C2889..C2988
(últimos 100). Nulo: 10,00 acertos por bilhete (desvio 2,01)."""
import numpy as np
from dados import carregar_historico

LENTES = ["freq50", "freq300", "frias300", "atraso", "pendente_ciclo", "repetida", "repetida_lag2", "vizinhas±1",
          "coluna±10", "espelho99-d", "fora_do_ultimo", "paridade_oposta", "decada_subrep", "soma_compensa"]

def ciclo_pend(M, t):
    vis = np.zeros(100, bool); ini = 0
    for s in range(t - 1, -1, -1):
        vis |= M[s].astype(bool)
        if vis.all(): ini = s + 1; break
    pen = np.ones(100, bool)
    for s in range(ini, t): pen &= ~M[s].astype(bool)
    return pen

def scores(M, cs, t):
    u = M[t - 1].astype(float); idx = np.arange(100)
    gap = np.full(100, t, float)
    for d in range(100):
        w = np.flatnonzero(M[:t, d])
        if len(w): gap[d] = t - 1 - w[-1]
    viz = np.zeros(100)
    for d in np.flatnonzero(u):
        for dd in (d - 1, d + 1):
            if 0 <= dd < 100: viz[dd] += 1
    col = np.zeros(100)
    for d in np.flatnonzero(u):
        for dd in (d - 10, d + 10):
            if 0 <= dd < 100: col[dd] += 1
    pares_ult = u[idx % 2 == 0].sum()
    dec_ult = np.array([u[idx // 10 == c].sum() for c in range(10)])
    soma = (u * idx).sum()
    return [cs[t - 50:t].mean(0) if False else M[t-50:t].mean(0), M[max(0, t-300):t].mean(0), -M[max(0, t-300):t].mean(0), gap,
            ciclo_pend(M, t).astype(float), u, M[t - 2].astype(float), viz, col, u[99 - idx], 1 - u,
            (idx % 2 == 0) * (1 if pares_ult < 10 else -1) + 0.0, -dec_ult[idx // 10] + 0.0,
            idx * (1 if soma > 990 else -1) * -1.0]

def z(v):
    r = np.argsort(np.argsort(v + 1e-9 * np.random.default_rng(0).random(100)))
    return (r - 49.5) / 28.9

def top50(s): return np.argsort(-s, kind="stable")[:50]

def main():
    M = carregar_historico()["D"]; cs = None; N = len(M)
    ini, ini_teste = 1000, N - 100
    w = np.ones(len(LENTES)); eta = 0.03
    reg = []   # por sorteio: hits do aprendiz, hits por lente, bilhete, peso
    for t in range(ini, N):
        S = scores(M, cs, t); Z = np.array([z(s) for s in S])
        bil = top50(w @ Z / w.sum()); hits_ap = int(M[t, bil].sum())
        h = np.array([int(M[t, top50(s)].sum()) for s in S])
        reg.append((t, hits_ap, h, set(bil.tolist()), w.copy()))
        w = w * np.exp(eta * (h - 10) / 2.0); w = np.clip(w / w.mean(), 0.05, 20)
    H = np.array([r[1] for r in reg]); HL = np.array([r[2] for r in reg]); T = np.array([r[0] for r in reg])
    def resumo(nome, m):
        n = m.sum(); a = H[m]; print(f"  {nome:28s} n={n:4d}  aprendiz {a.mean():.3f}  z={(a.mean()-10)/(2.01/np.sqrt(n)):+.2f}  máx {a.max()}")
    print("APRENDIZ ONLINE (top-50 dos pesos aprendidos), nulo 10,000")
    resumo("aprendizado C1001–C2888", T < ini_teste); resumo("TESTE últimos 100 (C2889–C2988)", T >= ini_teste)
    print("\nCada lente isolada (média de acertos do top-50), aprendizado | teste:")
    for i, nm in enumerate(LENTES):
        a, b = HL[T < ini_teste, i], HL[T >= ini_teste, i]
        print(f"  {nm:16s} {a.mean():.3f} (z {(a.mean()-10)/(2.01/np.sqrt(len(a))):+.2f}) | {b.mean():.3f} (z {(b.mean()-10)/(2.01/np.sqrt(len(b))):+.2f})")
    # persistência: o que foi bom no sorteio t continua bom em t+1?
    E = HL - 10; pers = [np.corrcoef(E[:-1, i], E[1:, i])[0, 1] for i in range(len(LENTES))]
    print(f"\nPersistência (corr. do desempenho da lente entre sorteios consecutivos): média {np.mean(pers):+.3f}  (limite 2σ ≈ ±{2/np.sqrt(len(E)):.3f})")
    # autópsia dos últimos 100
    print("\nAUTÓPSIA DOS ÚLTIMOS 100 SORTEIOS")
    mel = HL[T >= ini_teste].argmax(1); distintas = len(set(mel))
    print(f"  melhor lente a posteriori em cada sorteio: {distintas} lentes diferentes entre 14; média de acertos da melhor a posteriori: {HL[T>=ini_teste].max(1).mean():.2f}")
    prox = [HL[k + 1, mel[j]] for j, k in enumerate(np.flatnonzero(T >= ini_teste)[:-1])]
    print(f"  essa mesma lente no sorteio SEGUINTE: {np.mean(prox):.3f} (viés de seleção: {HL[T>=ini_teste].max(1).mean():.2f} → {np.mean(prox):.2f})")
    pert = np.zeros(100); n = 0
    for r in reg[-100:]:
        t, _, _, bil, _ = r; pert += np.array([d in bil for d in range(100)]) * (1 - M[t]); n += 1
    perdidas = np.array([len(set(np.flatnonzero(M[r[0]])) - r[3]) for r in reg[-100:]])
    print(f"  dezenas sorteadas que ficaram FORA do bilhete do aprendiz: média {perdidas.mean():.2f} de 20 (esperado 10,00)")
    # as dezenas perdidas tinham algo em comum? testa se ficar de fora de t prevê sair em t+1
    fora = np.array([[d not in r[3] and M[r[0], d] == 1 for d in range(100)] for r in reg[:-1]])
    prox_s = np.array([M[r[0] + 1] for r in reg[:-1]])
    p1 = prox_s[fora].mean(); p0 = prox_s[~fora].mean()
    print(f"  dezena que o aprendiz errou em t: chance de sair em t+1 = {p1:.4f}; demais dezenas = {p0:.4f} (uniforme 0,2000)")
    ult = reg[-1]
    print("  pesos finais das lentes:", {nm: round(float(x), 2) for nm, x in zip(LENTES, ult[4])})

if __name__ == "__main__":
    main()
