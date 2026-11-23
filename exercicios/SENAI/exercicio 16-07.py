def contadorLetras(palavra: str) -> int:
    quant = len(palavra)
    res = quant
    return res

palavra = input("Insira a palavra: ")
QuantTotalLetras = contadorLetras(palavra)
print(f"A quantidade de letras é: {QuantTotalLetras}")
        