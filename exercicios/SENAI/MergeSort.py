def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    resultado = []

    while esquerda and direita:
        if esquerda[0] < direita[0]:
            resultado.append(esquerda.pop(0))
        else:
            resultado.append(direita.pop(0))

    return resultado + esquerda + direita


numeros = [38, 27, 43, 3, 9, 82, 10]

print(merge_sort(numeros))