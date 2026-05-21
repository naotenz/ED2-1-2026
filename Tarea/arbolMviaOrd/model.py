# model.py

class NodoMVias:
    def __init__(self, orden):
        self.orden = orden
        self.claves = []
        self.hijos = [None] * orden


class ArbolMVias:
    def __init__(self, orden):
        self.raiz = None
        self.orden = orden

    # INSERTAR
    def insertar(self, clave):
        if self.raiz is None:
            self.raiz = NodoMVias(self.orden)
            self.raiz.claves.append(clave)
        else:
            self._insertar(self.raiz, clave)

    def _insertar(self, nodo, clave):
        if len(nodo.claves) < self.orden - 1:
            nodo.claves.append(clave)
            nodo.claves.sort()
            return

        for i in range(len(nodo.claves)):
            if clave < nodo.claves[i]:
                if nodo.hijos[i] is None:
                    nodo.hijos[i] = NodoMVias(self.orden)
                    nodo.hijos[i].claves.append(clave)
                else:
                    self._insertar(nodo.hijos[i], clave)
                return

        if nodo.hijos[len(nodo.claves)] is None:
            nodo.hijos[len(nodo.claves)] = NodoMVias(self.orden)
            nodo.hijos[len(nodo.claves)].claves.append(clave)
        else:
            self._insertar(nodo.hijos[len(nodo.claves)], clave)

    # RECORRIDO ORDENADO
    def inorder(self):
        resultado = []
        self._inorder(self.raiz, resultado)
        return resultado

    def _inorder(self, nodo, resultado):
        if nodo is None:
            return

        for i in range(len(nodo.claves)):
            self._inorder(nodo.hijos[i], resultado)
            resultado.append(nodo.claves[i])

        self._inorder(nodo.hijos[len(nodo.claves)], resultado)

    # ELIMINAR
    def eliminar(self, clave):
        self.raiz = self._eliminar(self.raiz, clave)

    def _eliminar(self, nodo, clave):
        if nodo is None:
            return None

        if clave in nodo.claves:
            nodo.claves.remove(clave)
            return nodo

        for hijo in nodo.hijos:
            self._eliminar(hijo, clave)

        return nodo


# ---------------- AVL ----------------

class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1


class AVL:
    def __init__(self):
        self.raiz = None

    def altura(self, nodo):
        return nodo.altura if nodo else 0

    def balance(self, nodo):
        return self.altura(nodo.izq) - self.altura(nodo.der)

    def rotacion_derecha(self, y):
        x = y.izq
        T2 = x.der

        x.der = y
        y.izq = T2

        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))

        return x

    def rotacion_izquierda(self, x):
        y = x.der
        T2 = y.izq

        y.izq = x
        x.der = T2

        x.altura = 1 + max(self.altura(x.izq), self.altura(x.der))
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))

        return y

    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if not nodo:
            return NodoAVL(valor)

        if valor < nodo.valor:
            nodo.izq = self._insertar(nodo.izq, valor)
        else:
            nodo.der = self._insertar(nodo.der, valor)

        nodo.altura = 1 + max(self.altura(nodo.izq), self.altura(nodo.der))

        balance = self.balance(nodo)

        if balance > 1 and valor < nodo.izq.valor:
            return self.rotacion_derecha(nodo)

        if balance < -1 and valor > nodo.der.valor:
            return self.rotacion_izquierda(nodo)

        return nodo

    def inorder(self):
        resultado = []
        self._inorder(self.raiz, resultado)
        return resultado

    def _inorder(self, nodo, resultado):
        if nodo:
            self._inorder(nodo.izq, resultado)
            resultado.append(nodo.valor)
            self._inorder(nodo.der, resultado)