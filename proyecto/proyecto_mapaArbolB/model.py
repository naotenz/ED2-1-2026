class Nodo:
    def __init__(self, valor):
        self.valor = valor              # aquí guarda el valor del nodo
        self.izquierda = None           # aquí referencia al hijo izquierdo
        self.derecha = None             # aquí referencia al hijo derecho


class ArbolBinario:
    def __init__(self):
        self.raiz = None                # aquí inicializa la raíz vacía

    def insertar(self, valor):
        # aquí llama a la función recursiva para insertar
        self.raiz = self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)

        if self._comparar(valor, nodo.valor) < 0:
            # aquí va a la izquierda
            nodo.izquierda = self._insertar_rec(nodo.izquierda, valor)
        else:
            # aquí va a la derecha
            nodo.derecha = self._insertar_rec(nodo.derecha, valor)

        return nodo

    def inorden(self, nodo, resultado):
        if nodo is not None:
            # aquí verifica que el nodo exista

            self.inorden(nodo.izquierda, resultado)
            # aquí recorre el lado izquierdo

            resultado.append(nodo.valor)
            # aquí agrega el nodo actual

            self.inorden(nodo.derecha, resultado)
            # aquí recorre el lado derecho

    def preorden(self, nodo, resultado):
        if nodo is not None:
            # aquí verifica que el nodo exista

            resultado.append(nodo.valor)
            # aquí agrega primero el nodo actual

            self.preorden(nodo.izquierda, resultado)
            # aquí recorre el lado izquierdo

            self.preorden(nodo.derecha, resultado)
            # aquí recorre el lado derecho

    def postorden(self, nodo, resultado):
        if nodo is not None:
            # aquí verifica que el nodo exista

            self.postorden(nodo.izquierda, resultado)
            # aquí recorre el lado izquierdo

            self.postorden(nodo.derecha, resultado)
            # aquí recorre el lado derecho

            resultado.append(nodo.valor)
            # aquí agrega el nodo al final

    def obtener_estructura(self, nodo):
        if nodo is None:
            # aquí verifica si el nodo está vacío
            return None

        return {
            "valor": nodo.valor,
            # aquí guarda el valor del nodo

            "izquierda": self.obtener_estructura(nodo.izquierda),
            # aquí obtiene recursivamente el hijo izquierdo

            "derecha": self.obtener_estructura(nodo.derecha)
            # aquí obtiene recursivamente el hijo derecho
        }

    def _es_numero(self, valor):
        try:
            float(valor)
            # aquí intenta convertir a número
            return True
        except:
            # aquí falla → no es número
            return False


    def _comparar(self, a, b):
            # prioridad: números primero

        if self._es_numero(a) and not self._es_numero(b):
            return -1   # a es menor

        if not self._es_numero(a) and self._es_numero(b):
            return 1    # a es mayor

        # ambos números
        if self._es_numero(a) and self._es_numero(b):
            return float(a) - float(b)

        # ambos letras
        return (a > b) - (a < b)