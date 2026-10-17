"""Hill-climbing no histórico real vs em sorteios sintéticos vs K10 vs J, no mesmo teste real (C1701+).
   Mostra quanto do ganho vem do histórico (nada) e quanto é só cobertura."""
import os, sys, numpy as np
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "lab"))
from dados import carregar_historico
from ferramentas import valido, sorteios_simulados
M=carregar_historico()["D"].astype(np.int8); N=len(M)
cons, sel, test = M[:1000], M[1000:1700], M[1700:]
def hc(DT, seed, tent):
    rng=np.random.default_rng(seed); J=[]
    while len(J)<10:
        g=set(rng.choice(100,50,replace=False).tolist())
        if valido(g): J.append(g)
    H=np.stack([DT[sorted(g)].sum(0,dtype=np.int16) for g in J]).astype(np.int8)
    f=lambda H:(lambda m:m.mean()+4*(m>=15).mean())(H.max(0)); cur=f(H)
    for _ in range(tent):
        j=int(rng.integers(10)); g=J[j]; s=int(rng.choice(sorted(g))); e=int(rng.choice(sorted(set(range(100))-g)))
        n=(g-{s})|{e}
        if not valido(n): continue
        old=H[j].copy(); H[j]=old-DT[s]+DT[e]; v=f(H)
        if v>cur: cur,J[j]=v,n
        else: H[j]=old
    return J
def av(D,J):
    V=np.zeros((100,10),np.float32)
    for j,g in enumerate(J): V[sorted(g),j]=1
    mx=(D.astype(np.float32)@V).max(1); return mx.mean(),(mx>=15).mean()
def ctrl(D,k=40,seed=5):
    rng=np.random.default_rng(seed); r=[]
    while len(r)<k:
        J=[set(rng.choice(100,50,replace=False).tolist()) for _ in range(10)]
        if all(valido(g) for g in J): r.append(av(D,J))
    return np.array(r)
print("HILL-CLIMBING SOBRE O HISTÓRICO REAL (construção C1–C1000, seleção C1001–C1700, teste C1701–C2988)")
DTc=np.ascontiguousarray(cons.T)
cands=[hc(DTc,s,20000) for s in range(6)]
scs=[av(sel,J) for J in cands]; b=int(np.argmax([a+4*p for a,p in scs])); J=cands[b]
print(f"  na construção (onde otimizou):  E[max] {av(cons,J)[0]:.3f}  P(>=15) {100*av(cons,J)[1]:.2f}%")
print(f"  na seleção (escolheu o melhor): E[max] {scs[b][0]:.3f}  P(>=15) {100*scs[b][1]:.2f}%")
R=ctrl(test); t=av(test,J)
print(f"  TESTE nunca visto (n={len(test)}):  E[max] {t[0]:.3f}  P(>=15) {100*t[1]:.2f}%")
print(f"  40 aleatórios no mesmo teste:   E[max] {R[:,0].mean():.3f} (faixa {R[:,0].min():.3f}–{R[:,0].max():.3f})  P(>=15) {100*R[:,1].mean():.2f}%")
print(f"  ganho no teste: {t[0]-R[:,0].mean():+.3f} em E[max]  | ganho prometido na construção: {av(cons,J)[0]-ctrl(cons)[:,0].mean():+.3f}")

print("\nCOMPARAÇÃO NO MESMO TESTE REAL (C1701–C2988): o histórico ensinou algo além de cobertura?")
sint=sorteios_simulados(1000,777).astype(np.int8); DTs=np.ascontiguousarray(sint.T)
res=[]
for s in range(6):
    Js=hc(DTs,100+s,20000); res.append((av(sel,Js),Js))   # seleciona pelo mesmo banco real de seleção
bs=max(res,key=lambda r:r[0][0]+4*r[0][1])[1]; a=av(test,bs)
print(f"  hill-climbing em 1.000 sorteios SINTÉTICOS: E[max] {a[0]:.3f}  P(>=15) {100*a[1]:.2f}%  (ganho {a[0]-R[:,0].mean():+.3f})")
print(f"  hill-climbing no HISTÓRICO REAL:            E[max] {t[0]:.3f}  P(>=15) {100*t[1]:.2f}%  (ganho {t[0]-R[:,0].mean():+.3f})")
import json
K=[g for g in json.load(open(os.path.join(RAIZ,"data","jogos_C2989_K10.json")))["jogos"].values()]
k=av(test,K); print(f"  K10 (otimizado em 150 mil simulados):       E[max] {k[0]:.3f}  P(>=15) {100*k[1]:.2f}%  (ganho {k[0]-R[:,0].mean():+.3f})")
Jj=[g["dezenas"] for gr in json.load(open(os.path.join(RAIZ,"data","jogos_C2988.json")))["grupos"] if gr["id"]=="J" for g in gr["jogos"]]
j=av(test,Jj); print(f"  J espiral (feito com C2986; vê o teste só como futuro parcial): E[max] {j[0]:.3f}  P(>=15) {100*j[1]:.2f}%  (ganho {j[0]-R[:,0].mean():+.3f})")
