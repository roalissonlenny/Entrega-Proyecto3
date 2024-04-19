class Grafo:
    def __init__(self, matriz_adyacencia):
        self.matriz_adyacencia = matriz_adyacencia

    def __str__(self):
        return "\n".join(["\t".join(map(str, fila)) for fila in self.matriz_adyacencia])

    def dijkstra(self, inicio, fin):
        nodos = len(self.matriz_adyacencia)
        distancias = [float('inf')] * nodos
        visitado = [False] * nodos
        path = [-1] * nodos

        distancias[inicio] = 0

        for _ in range(nodos):
            u = self.minima_distancia(distancias, visitado)
            visitado[u] = True

            for v in range(nodos):
                if (not visitado[v]) and self.matriz_adyacencia[u][v] and \
                        distancias[u] + self.matriz_adyacencia[u][v] < distancias[v]:
                    distancias[v] = distancias[u] + self.matriz_adyacencia[u][v]
                    path[v] = u

        self.mostrar_path(path, inicio, fin)
        print(f"Peso Total del Camino: {distancias[fin]}")

    def minima_distancia(self, distancias, visitado):
        min_dist = float('inf')
        min_index = -1

        for i in range(len(distancias)):
            if not visitado[i] and distancias[i] < min_dist:
                min_dist = distancias[i]
                min_index = i

        return min_index

    def mostrar_path(self, path, inicio, fin):
        if path[fin] == -1 and inicio != fin:
            print("No hay camino desde el vértice inicial al vértice final.")
            return

        camino = []
        actual = fin
        while actual != -1:
            camino.append(actual)
            actual = path[actual]

        camino.reverse()
        path_str = " -> ".join([chr(65 + nodo) for nodo in camino])
        print(f"Camino más corto desde {chr(65 + inicio)} hasta {chr(65 + fin)}: {path_str}")
