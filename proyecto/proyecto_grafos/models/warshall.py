"""
===========================================================
Archivo: warshall.py

Descripción:
-------------
Implementa el algoritmo de Floyd-Warshall para calcular la
ruta más corta entre todos los pares de nodos en un grafo.
===========================================================
"""


class Warshall:

    def calcular(self, grafo, origen, destino):
        """
        Calcula la ruta mínima entre dos nodos usando Floyd-Warshall.

        Parámetros
        ----------
        grafo : dict
            Lista de adyacencia con pesos.

        origen : str

        destino : str

        Retorna
        -------
        tuple
            (ruta, costo)
        """

        if origen not in grafo or destino not in grafo:
            return [], float("inf")

        nodos = list(grafo.keys())

        # Inicializar matrices de distancias y siguientes
        dist = {u: {v: float("inf") for v in nodos} for u in nodos}
        siguiente = {u: {v: None for v in nodos} for u in nodos}

        for u in nodos:
            dist[u][u] = 0
            siguiente[u][u] = u
            for v, peso in grafo[u]:
                dist[u][v] = peso
                siguiente[u][v] = v

        # Floyd-Warshall
        for k in nodos:
            for i in nodos:
                for j in nodos:
                    nueva_dist = dist[i][k] + dist[k][j]
                    if nueva_dist < dist[i][j]:
                        dist[i][j] = nueva_dist
                        siguiente[i][j] = siguiente[i][k]

        if siguiente[origen][destino] is None:
            return [], float("inf")

        ruta = [origen]
        nodo_actual = origen
        while nodo_actual != destino:
            nodo_actual = siguiente[nodo_actual][destino]
            ruta.append(nodo_actual)

        return ruta, dist[origen][destino]
