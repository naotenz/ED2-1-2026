# Modelo - Nodo del árbol
class Nodo:
    """Nodo del BST para almacenar palabra y traducción."""
    def __init__(self, palabra, traduccion):
        self.palabra = palabra
        self.traduccion = traduccion
        self.izq = None
        self.der = None


# Modelo - Árbol de búsqueda binario
class DiccionarioBST:
    """BST bilingüe español-inglés."""
    def __init__(self):
        self.raiz = None

    def insertar(self, palabra, traduccion):
        """Inserta palabra y traducción en el árbol."""
        if self.raiz is None:
            self.raiz = Nodo(palabra, traduccion)
        else:
            self._insertar_recursivo(self.raiz, palabra, traduccion)

    def _insertar_recursivo(self, nodo, palabra, traduccion):
        """Inserta recursivamente en el árbol manteniendo orden."""
        if palabra < nodo.palabra:
            if nodo.izq is None:
                nodo.izq = Nodo(palabra, traduccion)
            else:
                self._insertar_recursivo(nodo.izq, palabra, traduccion)
        else:
            if nodo.der is None:
                nodo.der = Nodo(palabra, traduccion)
            else:
                self._insertar_recursivo(nodo.der, palabra, traduccion)

    def buscar(self, palabra):
        """Busca y retorna la traducción de una palabra."""
        return self._buscar_recursivo(self.raiz, palabra)

    def _buscar_recursivo(self, nodo, palabra):
        """Busca recursivamente la palabra en el árbol."""
        if nodo is None:
            return None
        if palabra == nodo.palabra:
            return nodo.traduccion
        elif palabra < nodo.palabra:
            return self._buscar_recursivo(nodo.izq, palabra)
        else:
            return self._buscar_recursivo(nodo.der, palabra)

    def eliminar(self, palabra):
        """Elimina una entrada del diccionario."""
        self.raiz = self._eliminar_recursivo(self.raiz, palabra)

    def _eliminar_recursivo(self, nodo, palabra):
        """Elimina recursivamente manteniendo propiedades del BST."""
        if nodo is None:
            return None
        if palabra < nodo.palabra:   #La palabra que busco es menor al nodo actual 
            nodo.izq = self._eliminar_recursivo(nodo.izq, palabra)
        elif palabra > nodo.palabra:
            nodo.der = self._eliminar_recursivo(nodo.der, palabra)
        else:
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            temp = self._minimo(nodo.der)
            nodo.palabra = temp.palabra
            nodo.traduccion = temp.traduccion
            nodo.der = self._eliminar_recursivo(nodo.der, temp.palabra)
        return nodo

    def _minimo(self, nodo):
        """Encuentra el nodo con valor mínimo."""
        while nodo.izq:
            nodo = nodo.izq
        return nodo