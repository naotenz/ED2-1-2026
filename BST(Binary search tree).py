class NodoArbol:
    """
    Representa un nodo del árbol binario.

    Un nodo almacena:
        - Un valor
        - Referencia al hijo izquierdo
        - Referencia al hijo derecho
    """

    def __init__(self, valor):
        """
        Inicializa un nodo.

        Qué hace:
            Crea un nodo con un valor.

        Cómo lo hace:
            Asigna el valor y deja los hijos en None.

        Parámetros:
            valor: dato a almacenar.
        """
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    """
    Implementa un Árbol Binario de Búsqueda (BST).

    Permite:
        - Insertar valores
        - Buscar valores
        - Recorrer el árbol (recursivo e iterativo)
    """

    def __init__(self):
        """
        Inicializa el árbol vacío.
        """
        self.raiz = None

    # =========================
    # 🔵 MÉTODOS BÁSICOS
    # =========================

    def EsVacio(self):
        """
        Verifica si el árbol está vacío.

        Qué hace:
            Indica si no hay nodos en el árbol.

        Cómo lo hace:
            Comprueba si la raíz es None.

        Retorna:
            True si está vacío, False en caso contrario.
        """
        return self.raiz is None

    def EsHoja(self, nodo):
        """
        Determina si un nodo es hoja.

        Qué hace:
            Verifica si un nodo no tiene hijos.

        Cómo lo hace:
            Revisa si izquierda y derecha son None.

        Parámetros:
            nodo: nodo a evaluar.

        Retorna:
            True si es hoja.
        """
        return nodo.izquierda is None and nodo.derecha is None

    # =========================
    # 🔵 INSERCIÓN (RECURSIVA)
    # =========================

    def InsertarNodo(self, x):
        """
        Inserta un valor en el árbol.

        Qué hace:
            Agrega un nodo respetando el orden del BST.

        Cómo lo hace:
            Si el árbol está vacío, crea la raíz.
            Caso contrario, usa recursión.

        Parámetros:
            x: valor a insertar.
        """
        if self.raiz is None:
            self.raiz = NodoArbol(x)
        else:
            self._insertar_recursivo(self.raiz, x)

    def _insertar_recursivo(self, nodo, x):
        """
        Inserta un valor de forma recursiva.

        Qué hace:
            Busca la posición correcta.

        Cómo lo hace:
            - Menor → izquierda
            - Mayor o igual → derecha
        """
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

    # =========================
    # 🔵 BÚSQUEDA
    # =========================

    def BuscarX(self, x):
        """
        Búsqueda recursiva.

        Qué hace:
            Determina si un valor existe.

        Cómo lo hace:
            Recorre el árbol recursivamente.

        Retorna:
            True o False.
        """
        return self._buscar_recursivo(self.raiz, x)

    def _buscar_recursivo(self, nodo, x):
        """
        Método auxiliar recursivo.
        """
        if nodo is None:
            return False
        if nodo.valor == x:
            return True
        elif x < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, x)
        else:
            return self._buscar_recursivo(nodo.derecha, x)

    def BuscarX_Iterativo(self, x):
        """
        Búsqueda iterativa.

        Qué hace:
            Busca un valor sin recursión.

        Cómo lo hace:
            Usa un bucle while para recorrer el árbol.

        Parámetros:
            x: valor a buscar.

        Retorna:
            True si existe, False si no.
        """
        nodo = self.raiz

        while nodo:
            if nodo.valor == x:
                return True
            elif x < nodo.valor:
                nodo = nodo.izquierda
            else:
                nodo = nodo.derecha

        return False

    # =========================
    # 🔵 RECORRIDOS RECURSIVOS
    # =========================

    def InOrden(self):
        """
        Recorrido inorden (recursivo).

        Qué hace:
            Devuelve los valores ordenados.

        Cómo lo hace:
            izquierda → raíz → derecha.
        """
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            self._inorden_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecha, resultado)

    def PreOrden(self):
        """
        Recorrido preorden (recursivo).

        Qué hace:
            Visita primero la raíz.
        """
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado

    def _preorden_recursivo(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden_recursivo(nodo.izquierda, resultado)
            self._preorden_recursivo(nodo.derecha, resultado)

    def PostOrden(self):
        """
        Recorrido postorden (recursivo).

        Qué hace:
            Visita el nodo al final.
        """
        resultado = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado

    def _postorden_recursivo(self, nodo, resultado):
        if nodo:
            self._postorden_recursivo(nodo.izquierda, resultado)
            self._postorden_recursivo(nodo.derecha, resultado)
            resultado.append(nodo.valor)

    # =========================
    # 🟢 RECORRIDOS ITERATIVOS
    # =========================

    def InOrden_Iterativo(self):
        """
        Recorrido inorden iterativo.

        Qué hace:
            Devuelve los valores ordenados.

        Cómo lo hace:
            Usa una pila para simular la recursión.
        """
        resultado = []
        pila = []
        nodo = self.raiz

        while pila or nodo:
            while nodo:
                pila.append(nodo)
                nodo = nodo.izquierda

            nodo = pila.pop()
            resultado.append(nodo.valor)
            nodo = nodo.derecha

        return resultado

    def PreOrden_Iterativo(self):
        """
        Recorrido preorden iterativo.

        Qué hace:
            Visita raíz → izquierda → derecha.

        Cómo lo hace:
            Usa una pila (LIFO).
        """
        if self.raiz is None:
            return []

        resultado = []
        pila = [self.raiz]

        while pila:
            nodo = pila.pop()
            resultado.append(nodo.valor)

            if nodo.derecha:
                pila.append(nodo.derecha)
            if nodo.izquierda:
                pila.append(nodo.izquierda)

        return resultado

    def PostOrden_Iterativo(self):
        """
        Recorrido postorden iterativo.

        Qué hace:
            izquierda → derecha → raíz.

        Cómo lo hace:
            Usa dos pilas.
        """
        if self.raiz is None:
            return []

        resultado = []
        pila1 = [self.raiz]
        pila2 = []

        while pila1:
            nodo = pila1.pop()
            pila2.append(nodo)

            if nodo.izquierda:
                pila1.append(nodo.izquierda)
            if nodo.derecha:
                pila1.append(nodo.derecha)

        while pila2:
            resultado.append(pila2.pop().valor)

        return resultado
