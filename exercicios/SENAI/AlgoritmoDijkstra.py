# Importa heapq para trabalhar com uma fila de prioridade
import heapq


# Representa o grafo por meio de um dicionário
# Cada vértice possui uma lista de vizinhos e seus respectivos pesos
grafo = {
    "A": [("B", 4), ("C", 2)],
    "B": [("D", 5)],
    "C": [("B", 1), ("D", 8)],
    "D": []
}


# Função que calcula os menores caminhos a partir de um vértice inicial
def dijkstra(grafo, inicio):

    # Cria um dicionário com todas as distâncias inicialmente infinitas
    distancias = {no: float("inf") for no in grafo}

    # Define a distância do vértice inicial como zero
    distancias[inicio] = 0

    # Cria uma fila de prioridade com a distância e o vértice inicial
    fila = [(0, inicio)]

    # Continua enquanto existirem elementos na fila
    while fila:

        # Remove o vértice com a menor distância da fila
        distancia, atual = heapq.heappop(fila)

        # Ignora caminhos antigos que não representam a menor distância
        if distancia > distancias[atual]:
            continue

        # Percorre todos os vizinhos do vértice atual
        for vizinho, peso in grafo[atual]:

            # Calcula a nova distância até o vizinho
            nova = distancia + peso

            # Verifica se o novo caminho é menor que o caminho conhecido
            if nova < distancias[vizinho]:

                # Atualiza a menor distância encontrada
                distancias[vizinho] = nova

                # Adiciona o vizinho na fila de prioridade
                heapq.heappush(fila, (nova, vizinho))

    # Retorna o dicionário com as menores distâncias encontradas
    return distancias


# Executa o algoritmo começando pelo vértice A
# Exibe as menores distâncias entre A e os demais vértices
print(dijkstra(grafo, "A"))