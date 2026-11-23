def AreaQuadrada(*, num: float) -> float:
    areaFinal = (num ** 2)
    return areaFinal

num = float(input("Insira o tamanho do lado do quadrado: "))
AreaCalculada = AreaQuadrada(num=num)
print(f"A área é igual a: {AreaCalculada}")