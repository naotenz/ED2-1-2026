"""
===========================================================
Archivo: bfs.py

Algoritmo:
Breadth First Search (BFS)

Descripción:
-------------
Este algoritmo recorre un grafo por niveles.

Primero visita todos los vecinos del nodo inicial,
después los vecinos de esos vecinos, y así sucesivamente.

Para lograrlo utiliza una COLA (Queue).

Complejidad:

Tiempo:
O(V + E)

Espacio:
O(V)

V = Número de vértices.
E = Número de aristas.
===========================================================
"""

from collections import deque


class BFS:
    """
    Clase encargada de ejecutar el algoritmo BFS.
    """

    def recorrer(self, grafo, origen):
        """
        Realiza el recorrido BFS.

        Parámetros
        ----------
        grafo : dict
            Grafo representado mediante lista de adyacencia.

        origen : str
            Nodo desde donde comienza el recorrido.

        Retorna
        -------
        list
            Lista con el orden de visita.
        """

        # Guarda los nodos visitados
        visitados = set()

        # Cola del algoritmo
        cola = deque()

        # Orden del recorrido
        recorrido = []

        if origen not in grafo:
            return []

        # Agregamos el nodo inicial
        cola.append(origen)

        while cola:

            # Extrae el primer elemento de la cola
            nodo = cola.popleft()

            # Si aún no fue visitado
            if nodo not in visitados:

                # Lo marcamos como visitado
                visitados.add(nodo)

                # Lo agregamos al recorrido
                recorrido.append(nodo)

                # Recorremos todos sus vecinos
                for vecino, peso in grafo.get(nodo, []):

                    # Solo agregamos vecinos no visitados
                    if vecino not in visitados:
                        cola.append(vecino)

        return recorrido