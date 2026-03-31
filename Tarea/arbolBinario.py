"""
Módulo de Árbol Binario de Búsqueda (BST)

Implementa un árbol binario de búsqueda con operaciones de inserción,
búsqueda y recorridos.
"""


class NodoArbol:
    """
    Representa un nodo del árbol binario.

    Un nodo almacena un valor y referencias a sus hijos izquierdo y derecho.
    """

    def __init__(self, valor):
        """
        Inicializa un nodo con un valor dado.

        Qué hace:
            Crea un nodo con un valor y sin hijos.

        Cómo lo hace:
            Asigna el valor recibido y establece los hijos como None.

        Parámetros:
            valor: número a almacenar en el nodo.
        """
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    """
    Implementa un Árbol Binario de Búsqueda (BST).

    Permite insertar valores, buscarlos y recorrer el árbol.
    """

    def __init__(self):
        """
        Inicializa el árbol vacío.

        Qué hace:
            Crea un árbol sin nodos.

        Cómo lo hace:
            Define la raíz como None.
        """
        self.raiz = None
    
    def EsVacio(self):
        """
        Verifica si el árbol está vacío.

        Qué hace:
            Determina si el árbol no contiene elementos.

        Cómo lo hace:
            Comprueba si la raíz es None.

        Retorna:
            True si está vacío, False en caso contrario.

        Ejemplo:
            arbol = ArbolBinario()
            print(arbol.EsVacio())  # True
        """
        return self.raiz is None
    
    def InsertarNodo(self, x):
        """
        Inserta un valor en el árbol.

        Qué hace:
            Agrega un nuevo nodo respetando la propiedad del BST.

        Cómo lo hace:
            Si el árbol está vacío, crea la raíz.
            Si no, usa recursión para ubicar el lugar correcto.

        Parámetros:
            x: valor a insertar.

        Ejemplo:
            arbol = ArbolBinario()
            arbol.InsertarNodo(50)
            arbol.InsertarNodo(30)
            arbol.InsertarNodo(70)
        """
        if self.raiz is None:
            self.raiz = NodoArbol(x)
        else:
            self._insertar_recursivo(self.raiz, x)
    
    def _insertar_recursivo(self, nodo, x):
        """
        Inserta un nodo de forma recursiva.

        Qué hace:
            Encuentra la posición correcta para insertar el valor.

        Cómo lo hace:
            Compara el valor con el nodo actual:
            - Si es menor, va a la izquierda.
            - Si es mayor o igual, va a la derecha.

        Parámetros:
            nodo: nodo actual.
            x: valor a insertar.
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
    
    def EsHoja(self, nodo):
        """
        Determina si un nodo es hoja.

        Qué hace:
            Verifica si un nodo no tiene hijos.

        Cómo lo hace:
            Comprueba que ambos hijos sean None.

        Parámetros:
            nodo: nodo a evaluar.

        Retorna:
            True si es hoja, False si tiene hijos.

        Ejemplo:
            arbol = ArbolBinario()
            arbol.InsertarNodo(50)
            nodo = arbol.raiz
            print(arbol.EsHoja(nodo))  # True
        """
        return nodo.izquierda is None and nodo.derecha is None
    
    def BuscarX(self, x):
        """
        Busca un valor en el árbol.

        Qué hace:
            Determina si un valor existe en el árbol.

        Cómo lo hace:
            Realiza una búsqueda recursiva desde la raíz.

        Parámetros:
            x: valor a buscar.

        Retorna:
            True si existe, False si no.

        Ejemplo:
            arbol = ArbolBinario()
            arbol.InsertarNodo(50)
            arbol.InsertarNodo(30)

            print(arbol.BuscarX(30))  # True
            print(arbol.BuscarX(10))  # False
        """
        return self._buscar_recursivo(self.raiz, x)
    
    def _buscar_recursivo(self, nodo, x):
        """
        Busca un valor de forma recursiva.

        Qué hace:
            Recorre el árbol buscando el valor.

        Cómo lo hace:
            - Si el nodo es None, no existe.
            - Si coincide, retorna True.
            - Si es menor, busca a la izquierda.
            - Si es mayor, busca a la derecha.

        Parámetros:
            nodo: nodo actual.
            x: valor buscado.
        """
        if nodo is None:
            return False
        if nodo.valor == x:
            return True
        elif x < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, x)
        else:
            return self._buscar_recursivo(nodo.derecha, x)
    
    def InOrden(self):
        """
        Realiza recorrido inorden.

        Qué hace:
            Devuelve los valores ordenados.

        Cómo lo hace:
            Recorre izquierda → raíz → derecha.

        Retorna:
            Lista de valores.

        Ejemplo:
            arbol = ArbolBinario()
            arbol.InsertarNodo(50)
            arbol.InsertarNodo(30)
            arbol.InsertarNodo(70)

            print(arbol.InOrden())  # [30, 50, 70]
        """
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _inorden_recursivo(self, nodo, resultado):
        """
        Recorrido inorden recursivo.

        Qué hace:
            Visita los nodos en orden.

        Cómo lo hace:
            Aplica recursión izquierda → raíz → derecha.

        Parámetros:
            nodo: nodo actual.
            resultado: lista acumuladora.
        """
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecha, resultado)
    
    def PreOrden(self):
        """
        Realiza recorrido preorden.

        Qué hace:
            Devuelve los valores en orden raíz → izquierda → derecha.

        Retorna:
            Lista de valores.

        Ejemplo:
            arbol = ArbolBinario()
            arbol.InsertarNodo(50)
            arbol.InsertarNodo(30)
            arbol.InsertarNodo(70)

            print(arbol.PreOrden())  # [50, 30, 70]
        """
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _preorden_recursivo(self, nodo, resultado):
        """
        Recorrido preorden recursivo.

        Qué hace:
            Visita primero la raíz.

        Cómo lo hace:
            Aplica recursión raíz → izquierda → derecha.

        Parámetros:
            nodo: nodo actual.
            resultado: lista acumuladora.
        """
        if nodo is not None:
            resultado.append(nodo.valor)
            self._preorden_recursivo(nodo.izquierda, resultado)
            self._preorden_recursivo(nodo.derecha, resultado)
    
    def PostOrden(self):
        """
        Realiza recorrido postorden.

        Qué hace:
            Devuelve los valores en orden izquierda → derecha → raíz.

        Retorna:
            Lista de valores.

        Ejemplo:
            arbol = ArbolBinario()
            arbol.InsertarNodo(50)
            arbol.InsertarNodo(30)
            arbol.InsertarNodo(70)

            print(arbol.PostOrden())  # [30, 70, 50]
        """
        resultado = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _postorden_recursivo(self, nodo, resultado):
        """
        Recorrido postorden recursivo.

        Qué hace:
            Visita el nodo al final.

        Cómo lo hace:
            Aplica recursión izquierda → derecha → raíz.

        Parámetros:
            nodo: nodo actual.
            resultado: lista acumuladora.
        """
        if nodo is not None:
            self._postorden_recursivo(nodo.izquierda, resultado)
            self._postorden_recursivo(nodo.derecha, resultado)
            resultado.append(nodo.valor)

if __name__ == "__main__":
    # Crear el árbol
    arbol = ArbolBinario()

    # Insertar valores
    arbol.InsertarNodo(50)
    arbol.InsertarNodo(30)
    arbol.InsertarNodo(70)
    arbol.InsertarNodo(20)
    arbol.InsertarNodo(40)
    arbol.InsertarNodo(60)
    arbol.InsertarNodo(80)

    # Mostrar recorridos
    print("Recorrido InOrden:", arbol.InOrden())
    print("Recorrido PreOrden:", arbol.PreOrden())
    print("Recorrido PostOrden:", arbol.PostOrden())

    # Buscar valores
    print("¿Existe 40?:", arbol.BuscarX(40))
    print("¿Existe 100?:", arbol.BuscarX(100))

    # Verificar si la raíz es hoja
    print("¿La raíz es hoja?:", arbol.EsHoja(arbol.raiz))