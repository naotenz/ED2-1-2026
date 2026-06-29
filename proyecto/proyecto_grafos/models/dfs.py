"""
===========================================================
Archivo: dfs.py

Algoritmo:
Depth First Search (DFS)

Descripción:
-------------
DFS recorre un grafo profundizando lo más posible
antes de retroceder.

Utiliza una PILA (Stack).

Complejidad:

Tiempo:
O(V + E)

Espacio:
O(V)

V = Número de vértices.
E = Número de aristas.
===========================================================
"""


class DFS:
    """
    Clase encargada del algoritmo DFS.
    """

    def recorrer(self, grafo, origen):
        """
        Recorre el grafo usando DFS.

        Parámetros
        ----------
        grafo : dict
            Lista de adyacencia.

        origen : str
            Nodo inicial.

        Retorna
        -------
        list
            Orden del recorrido.
        """

        # Guarda los nodos visitados
        visitados = set()

        # Pila del algoritmo
        pila = []

        # Lista del recorrido
        recorrido = []

        if origen not in grafo:
            return []

        # Agregamos el nodo inicial
        pila.append(origen)

        while pila:

            # Sacamos el último nodo agregado
            nodo = pila.pop()

            if nodo not in visitados:

                visitados.add(nodo)

                recorrido.append(nodo)

                # Recorremos los vecinos en orden inverso
                # para mantener un recorrido consistente
                vecinos = grafo.get(nodo, [])

                for vecino, peso in reversed(vecinos):

                    if vecino not in visitados:
                        pila.append(vecino)

        return recorrido