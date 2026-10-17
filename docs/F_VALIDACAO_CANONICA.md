# VALIDAÇÃO CANÔNICA — ÚNICA FONTE DE VERDADE
**Anexo ao arquivo D — nunca reescrever esta lógica do zero em nenhuma construção futura**

---

## POR QUE ESTE ARQUIVO EXISTE

Histórico de bugs que esta função já preveniu, e que aconteceram por
reescrever a validação "de memória" em vez de reutilizar código salvo:

- **H12** (arsenal de 12 palpites): L6 zerou porque a checagem só
  bloqueava L=1, não L=0
- **Tentativa L2/L5/L7 vazias**: L8 zerou pelo mesmo motivo
- **H5_equilíbrio**: L7 zerou pelo mesmo motivo, **pela terceira vez**

Regra: **sempre copiar esta função exata para qualquer script novo de
construção de palpite — nunca recriar a lógica de validação do zero.**

---

## O CÓDIGO

```python
def valid_palpite(p, ESP=[(11,88),(32,67),(10,89)], tamanho=50, minimo_por_decada=2):
    """
    Validação completa e única. SEMPRE usar esta função, nunca recriar.
    Retorna (True/False, mensagem explicando o motivo se inválido).
    """
    if len(p) != tamanho:
        return False, f"tamanho={len(p)}, esperado {tamanho}"
    for a, b in ESP:
        if a in p and b in p:
            return False, f"ESP violado: {a} e {b} juntos"
    lv = [len([d for d in p if d // 10 == i]) for i in range(10)]
    for i, v in enumerate(lv):
        if v < minimo_por_decada:
            return False, f"L{i}={v}, abaixo do mínimo {minimo_por_decada}"
    return True, "válido"


# Teste automático — se isso falhar, a função está quebrada
if __name__ == "__main__":
    p_teste_bom = list(range(0, 50))  # propositalmente ruim: só cobre L0-L4
    ok, msg = valid_palpite(p_teste_bom)
    print(f"Teste (deve reportar problema de década): {ok} - {msg}")
```

---

## COMO USAR

1. Antes de qualquer construção nova de palpite, copiar a função
   `valid_palpite` acima para o script — não escrever uma versão nova
2. Chamar `valid_palpite(p)` para cada palpite antes de considerá-lo
   pronto — nunca assumir validade sem checar
3. Se `ok=False`, a mensagem já explica o motivo exato — corrigir e
   testar de novo antes de prosseguir

Isso transforma "deveria lembrar de checar década vazia e ESP" em
"o código força a checagem sempre" — o único tipo de generalização que
funciona de forma confiável neste projeto (ver arquivo D, Parte 3).
