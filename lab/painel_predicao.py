"""Painel de predição fora da amostra: boosting, logística e controle com rótulos embaralhados.
Hipótese nula: o sorteio é uniforme -> AUC 0,5 e top-50 = 10,00 acertos."""
import argparse, numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from dados import carregar

JAN = (5, 10, 20, 50, 100, 300)

def features(M, t):
    """Features por dezena usando só sorteios < t."""
    H = M[:t]
    cols = []
    for j in JAN:
        cols.append(H[-j:].mean(0))
    ult = H[-1]
    gap = np.zeros(100)
    for d in range(100):
        idx = np.flatnonzero(H[:, d])
        gap[d] = t - idx[-1] if len(idx) else t
    cols += [ult, gap, np.arange(100) // 10, np.arange(100) % 10,
             H[-2], H[-3], (H[-10:].sum(0))]
    # pendente do ciclo: não saiu desde o início do ciclo atual
    vis = np.zeros(100, bool); ini = t
    for s in range(t - 1, -1, -1):
        vis |= H[s].astype(bool)
        if vis.all(): ini = s; break
    ciclo = np.ones(100)
    vis = np.zeros(100, bool)
    for s in range(ini + 1, t): vis |= H[s].astype(bool)
    ciclo = (~vis).astype(float)
    cols.append(ciclo)
    return np.stack(cols, 1)

def montar(M, a, b):
    X, y = [], []
    for t in range(a, b):
        X.append(features(M, t)); y.append(M[t])
    return np.vstack(X), np.concatenate(y)

def top50(prob, y, n):
    p = prob.reshape(n, 100); yy = y.reshape(n, 100)
    return np.mean([yy[i][np.argsort(-p[i])[:50]].sum() for i in range(n)])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default="data/historico.csv")
    ap.add_argument("--treino", default="300:2000"); ap.add_argument("--teste", default="2000:0")
    a = ap.parse_args()
    _, _, M = carregar(a.csv)
    t0, t1 = map(int, a.treino.split(":")); s0, s1 = map(int, a.teste.split(":"))
    s1 = s1 or len(M)
    Xtr, ytr = montar(M, t0, t1); Xte, yte = montar(M, s0, s1); n = s1 - s0
    rng = np.random.default_rng(7)
    mod = {
        "boosting": HistGradientBoostingClassifier(max_iter=150, learning_rate=0.05),
        "logística": LogisticRegression(max_iter=500),
    }
    for nome, m in mod.items():
        m.fit(Xtr, ytr); p = m.predict_proba(Xte)[:, 1]
        print(f"{nome:10s} AUC {roc_auc_score(yte, p):.4f}  top-50 {top50(p, yte, n):.3f} (esperado 10,000)")
    c = HistGradientBoostingClassifier(max_iter=150, learning_rate=0.05)
    c.fit(Xtr, rng.permutation(ytr)); p = c.predict_proba(Xte)[:, 1]
    print(f"{'controle':10s} AUC {roc_auc_score(yte, p):.4f}  top-50 {top50(p, yte, n):.3f}  (rótulos embaralhados)")
    # erro-padrão do top-50 sob H0: desvio por sorteio 2,01
    print(f"erro-padrão do top-50 sob H0 ≈ {2.01/np.sqrt(n):.3f}  (n={n} sorteios de teste)")

if __name__ == "__main__":
    main()
