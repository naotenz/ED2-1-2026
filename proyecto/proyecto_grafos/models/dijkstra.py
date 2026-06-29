"""
===========================================================
Archivo: dijkstra.py

Algoritmo:
Dijkstra

Descripción:
-------------
Calcula la ruta de menor costo entre un nodo origen
y un nodo destino.

Este algoritmo funciona únicamente cuando los pesos
son positivos.

Utiliza una Cola de Prioridad (heapq).

Complejidad:

Tiempo:
O((V + E) log V)

Espacio:
O(V)

V = Número de vértices
E = Número de aristas
===========================================================
"""

import heapq


class Dijkstra:
    """
    Clase que implementa el algoritmo de Dijkstra.
    """

    def calcular(self, grafo, origen, destino):
        """
        Calcula la ruta mínima.

        Parámetros
        ----------
        grafo : dict

        origen : str

        destino : str

        Retorna
        -------
        tuple

        (ruta, costo)
        """

        # Distancia infinita para todos los nodos
        distancias = {}

        # Nodo anterior para reconstruir la ruta
        anteriores = {}

        # Inicializamos las distancias
        for nodo in grafo:
            distancias[nodo] = float("inf")
            anteriores[nodo] = None

        if origen not in grafo or destino not in grafo:
            return [], float("inf")

        # El origen tiene distancia 0
        distancias[origen] = 0

        # Cola de prioridad
        cola = []

        # (distancia, nodo)
        heapq.heappush(cola, (0, origen))

        while cola:

            distancia_actual, nodo_actual = heapq.heappop(cola)

            # Si llegamos al destino terminamos
            if nodo_actual == destino:
                break

            # Recorremos vecinos
            for vecino, peso in grafo[nodo_actual]:

                nueva_distancia = distancia_actual + peso

                if nueva_distancia < distancias[vecino]:

                    distancias[vecino] = nueva_distancia

                    anteriores[vecino] = nodo_actual

                    heapq.heappush(
                        cola,
                        (nueva_distancia, vecino)
                    )

        # Reconstruir ruta

        if distancias[destino] == float("inf"):
            return [], float("inf")

        ruta = []

        actual = destino

        while actual is not None:

            ruta.insert(0, actual)

            actual = anteriores[actual]

        return ruta, distancias[destino]