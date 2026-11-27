# Função responsável por ordenar a lista usando Merge Sort
def merge_sort(lista):

    # Caso base: se a lista tiver zero ou um elemento,
    # ela já está ordenada
    if len(lista) <= 1:
        return lista

    # Encontra a posição do meio da lista
    meio = len(lista) // 2

    # Divide a lista e chama a função recursivamente
    # para ordenar a primeira metade
    esquerda = merge_sort(lista[:meio])

    # Divide e ordena a segunda metade
    direita = merge_sort(lista[meio:])

    # Cria uma lista vazia para armazenar os elementos ordenados
    resultado = []

    # Compara os elementos enquanto as duas listas possuem valores
    while esquerda and direita:

        # Verifica qual dos primeiros elementos é menor
        if esquerda[0] < direita[0]:

            # Adiciona o menor elemento ao resultado
            resultado.append(esquerda.pop(0))

        else:
            # Adiciona o elemento da direita se ele for menor
            resultado.append(direita.pop(0))

    # Junta o resultado com os elementos que sobraram
    # em uma das duas listas
    return resultado + esquerda + direita


# Cria uma lista de números desordenados
numeros = [38, 27, 43, 3, 9, 82, 10]

# Executa o Merge Sort e exibe a lista ordenada
print(merge_sort(numeros))