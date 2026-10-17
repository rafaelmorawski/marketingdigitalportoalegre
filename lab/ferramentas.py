from math import comb
from fractions import Fraction

def chance_exata(k, n=50, sorteadas=20, total=100):
    """P(exatamente k acertos) para um bilhete de n dezenas (hipergeométrica)."""
    return Fraction(comb(sorteadas, k) * comb(total - sorteadas, n - k), comb(total, n))

def tabela():
    return {k: chance_exata(k) for k in range(0, 21)}

if __name__ == "__main__":
    t = tabela()
    print("20 acertos : 1 em", round(1 / float(t[20])))
    print(" 0 acerto  : 1 em", round(1 / float(t[0])))
    p19 = t[19] + t[20]; print("19 ou mais : 1 em", round(1 / float(p19)))
    print("15 ou mais : %.3f%%" % (100 * float(sum(t[k] for k in range(15, 21)))))
    for k in (14, 13, 12): print(f"exatamente {k}: {100*float(t[k]):.3f}%")
    m = sum(k * float(t[k]) for k in t); v = sum((k - m) ** 2 * float(t[k]) for k in t)
    print("média %.2f  desvio %.2f" % (m, v ** .5))
