# -*- coding: utf-8 -*-
"""Testes de regressão: os números de referência do laboratório precisam continuar reproduzindo. Sem rede, sem dependências pesadas.
Rodar: python3 -m unittest discover -s tests -v"""
import glob, json, os, sys, unittest
import numpy as np
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(RAIZ, "lab"))
from math import comb
from fractions import Fraction
from ferramentas import valido, P20, P19MAIS

def chance_exata(k, n=50, s=20, t=100):
    return Fraction(comb(s, k) * comb(t - s, n - k), comb(t, n))
from dados import carregar_historico
import validar_dados

class Matematica(unittest.TestCase):
    def test_chances_exatas(self):
        self.assertEqual(round(1 / float(chance_exata(20))), 11372636)
        self.assertEqual(round(1 / float(chance_exata(0))), 11372636)             # simetria: 0 de T = 20 do espelho
        self.assertAlmostEqual(100 * float(sum(chance_exata(k) for k in range(15, 21))), 1.142, places=3)
        self.assertAlmostEqual(100 * float(chance_exata(14)), 2.781, places=3)
        m = sum(k * float(chance_exata(k)) for k in range(21)); self.assertAlmostEqual(m, 10.0, places=9)
        self.assertEqual(round(1 / P20), 11372636); self.assertEqual(round(1 / P19MAIS), 341951)   # constantes do pacote

class Dados(unittest.TestCase):
    def test_integridade(self):
        erros, _, n, ult = validar_dados.verificar()
        self.assertEqual(erros, []); self.assertGreaterEqual(n, 2988)

    def test_c2988(self):
        h = carregar_historico(); self.assertEqual(h["dezenas"][h["concursos"].index(2988)], [4, 8, 13, 17, 21, 23, 28, 29, 30, 47, 70, 75, 78, 79, 80, 85, 89, 92, 95, 97])

class Jogos(unittest.TestCase):
    def test_arquivos_de_jogos_validos(self):
        achou = 0
        for f in glob.glob(os.path.join(RAIZ, "data", "jogos_*.json")):
            d = json.load(open(f, encoding="utf-8"))
            js = [g["dezenas"] for gr in d["grupos"] for g in gr["jogos"]] if "grupos" in d else list(d["jogos"].values())
            for g in js:
                achou += 1; self.assertEqual(len(set(g)), 50, f); self.assertTrue(0 <= min(g) and max(g) <= 99, f)
        self.assertGreater(achou, 0)

    def test_conferencia_c2988_reproduz(self):
        d = json.load(open(os.path.join(RAIZ, "data", "jogos_C2988.json"), encoding="utf-8")); r = {4, 8, 13, 17, 21, 23, 28, 29, 30, 47, 70, 75, 78, 79, 80, 85, 89, 92, 95, 97}
        J = [len(r & set(g["dezenas"])) for gr in d["grupos"] if gr["id"] == "J" for g in gr["jogos"]]
        self.assertEqual((max(J), round(float(np.mean(J)), 2)), (11, 9.9))
        todos = [len(r & set(g["dezenas"])) for gr in d["grupos"] for g in gr["jogos"]]
        self.assertEqual(len(todos), 24); self.assertEqual(max(todos), 13)

    def test_piso_garantido(self):
        from garantia import pior_sorteio
        K = list(json.load(open(os.path.join(RAIZ, "data", "jogos_C2989_K10.json")))["jogos"].values())
        self.assertEqual(pior_sorteio([K[0], sorted(set(range(100)) - set(K[0]))], 30)[0], 10)   # jogo + espelho garantem 10

if __name__ == "__main__":
    unittest.main()
