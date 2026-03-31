class NodoArbol:
    """
    Módulo de Árbol Binario de Búsqueda (BST)
    Este módulo implementa un Árbol Binario de Búsqueda completo con operaciones
    de inserción, búsqueda y recorrido en sus tres formas principales.
    Clases:
        - NodoArbol: Representa un nodo individual del árbol
        - ArbolBinario: Implementa la estructura completa del árbol binario
    Ejemplo de uso:
        arbol = ArbolBinario()
        arbol.InsertarNodo(50)
        arbol.InsertarNodo(30)
        arbol.InsertarNodo(70)
        print(arbol.InOrden())  # [30, 50, 70]
    """
    """
    Representa un nodo individual en el Árbol Binario de Búsqueda.
    Atributos:
        valor (int/float): El valor almacenado en el nodo
        izquierda (NodoArbol): Referencia al hijo izquierdo (valores menores)
        derecha (NodoArbol): Referencia al hijo derecho (valores mayores o iguales)
    """
    pass
    """
    Implementa un Árbol Binario de Búsqueda (BST) con operaciones completas.
    Un Árbol Binario de Búsqueda es una estructura de datos donde cada nodo tiene
    como máximo dos hijos, y mantiene la propiedad de que los valores en el subárbol
    izquierdo son menores y los del subárbol derecho son mayores o iguales.
    Atributos:
        raiz (NodoArbol): el nodo raíz del árbol
    Métodos públicos:
        EsVacio(): Verifica si el árbol no contiene nodos
        InsertarNodo(x): Añade un nuevo nodo con valor x manteniendo la propiedad BST
        EsHoja(nodo): Determina si un nodo dado es terminal (sin descendientes)
        BuscarX(x): Busca un valor específico en el árbol
        InOrden(): Retorna lista de valores recorriendo Izquierda-Raíz-Derecha
        PreOrden(): Retorna lista de valores recorriendo Raíz-Izquierda-Derecha
        PostOrden(): Retorna lista de valores recorriendo Izquierda-Derecha-Raíz
        """
    pass
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def EsVacio(self):
        """Verifica si el árbol está vacío"""
        return self.raiz is None
    
    def InsertarNodo(self, x):
        """Inserta un nodo con valor x en el árbol"""
        if self.raiz is None:
            self.raiz = NodoArbol(x)
        else:
            self._insertar_recursivo(self.raiz, x)
    
    def _insertar_recursivo(self, nodo, x):
        """Método auxiliar para insertar de forma recursiva"""
        if x < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(x)
            else:
                self._insertar_recursivo(nodo.izquierda, x)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(x)
            else:
                self._insertar_recursivo(nodo.derecha, x)
    
    def EsHoja(self, nodo):
        """Verifica si un nodo es hoja (sin hijos)"""
        return nodo.izquierda is None and nodo.derecha is None
    
    def BuscarX(self, x):
        """Busca un valor x en el árbol"""
        return self._buscar_recursivo(self.raiz, x)
    
    def _buscar_recursivo(self, nodo, x):
        """Método auxiliar para buscar de forma recursiva"""
        if nodo is None:
            return False
        if nodo.valor == x:
            return True
        elif x < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, x)
        else:
            return self._buscar_recursivo(nodo.derecha, x)
    
    def InOrden(self):
        """Recorrido en orden (Izquierda-Raíz-Derecha)"""
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _inorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecha, resultado)
    
    def PreOrden(self):
        """Recorrido preorden (Raíz-Izquierda-Derecha)"""
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _preorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.valor)
            self._preorden_recursivo(nodo.izquierda, resultado)
            self._preorden_recursivo(nodo.derecha, resultado)
    
    def PostOrden(self):
        """Recorrido postorden (Izquierda-Derecha-Raíz)"""
        resultado = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _postorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._postorden_recursivo(nodo.izquierda, resultado)
            self._postorden_recursivo(nodo.derecha, resultado)
            resultado.append(nodo.valor)