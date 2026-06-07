"""

Implementación de un Árbol Binario de Búsqueda.
"""

class Nodo:

    def __init__(self, archivo):
        self.archivo = archivo
        self.izquierda = None
        self.derecha = None


class ArbolBinario:

    def __init__(self):
        self.raiz = None

    def insertar(self, archivo):

        nuevo = Nodo(archivo)

        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz

        while True:

            if archivo.nombre.lower() < actual.archivo.nombre.lower():

                if actual.izquierda is None:
                    actual.izquierda = nuevo
                    return

                actual = actual.izquierda

            else:

                if actual.derecha is None:
                    actual.derecha = nuevo
                    return

                actual = actual.derecha

    def buscar(self, nombre):

        actual = self.raiz

        while actual:

            if nombre.lower() == actual.archivo.nombre.lower():
                return actual.archivo

            elif nombre.lower() < actual.archivo.nombre.lower():
                actual = actual.izquierda

            else:
                actual = actual.derecha

        return None

    def mostrar_inorden(self, nodo):

        if nodo is not None:

            self.mostrar_inorden(nodo.izquierda)

            print(nodo.archivo)

            self.mostrar_inorden(nodo.derecha)