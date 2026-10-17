"""Lê a planilha da Caixa (xlsx) mesmo com células numéricas inválidas ('-'). Gera CSV no formato de data/Lotomania.csv."""
import csv, re, sys, zipfile
import xml.etree.ElementTree as ET
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}

def col(ref):
    n = 0
    for c in re.match(r"[A-Z]+", ref).group(): n = n * 26 + ord(c) - 64
    return n - 1

def ler(caminho):
    z = zipfile.ZipFile(caminho)
    ss = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS):
            ss.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
    sh = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
    linhas = []
    for row in sh.iter("{%s}row" % NS["m"]):
        v = {}
        pos = 0
        for c in row.findall("m:c", NS):
            x = c.find("m:v", NS); t = c.get("t")
            if t == "inlineStr":
                val = "".join(e.text or "" for e in c.iter("{%s}t" % NS["m"]))
            elif x is None: val = ""
            elif t == "s": val = ss[int(x.text)]
            else: val = x.text
            i = col(c.get("r")) if c.get("r") else pos
            v[i] = val; pos = i + 1
        linhas.append([v.get(i, "") for i in range(max(v) + 1)] if v else [])
    return linhas

if __name__ == "__main__":
    L = ler(sys.argv[1])
    with open(sys.argv[2], "w", newline="", encoding="utf-8") as f: csv.writer(f).writerows(L)
    print(len(L), "linhas")
