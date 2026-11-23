import heapq

grafo = {
    "A": [("B", 4), ("C", 2)],
    "B": [("D", 5)],
    "C": [("B", 1), ("D", 8)],
    "D": []
}

def dijkstra(grafo, inicio):
    distancias = {no: float("inf") for no in grafo}
    distancias[inicio] = 0

    fila = [(0, inicio)]

    while fila:
        distancia, atual = heapq.heappop(fila)

        if distancia > distancias[atual]:
            continue

        for vizinho, peso in grafo[atual]:
            nova = distancia + peso

            if nova < distancias[vizinho]:
                distancias[vizinho] = nova
                heapq.heappush(fila, (nova, vizinho))

    return distancias


print(dijkstra(grafo, "A"))