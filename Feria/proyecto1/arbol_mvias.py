import csv
from nodo_mvias import NodoMVias


class ArbolMVias:

    def __init__(self, orden):
        self.orden = orden
        self.raiz = None
        self.comparaciones = 0

    # =========================
    # INSERTAR
    # =========================

    def insertar(self, valor):

        if not valor:
            return

        valor = valor.upper()

        if self.raiz is None:
            self.raiz = NodoMVias(self.orden)
            self.raiz.claves.append(valor)
            return

        self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):

        if valor in nodo.claves:
            return

        if len(nodo.claves) < self.orden - 1:
            nodo.claves.append(valor)
            nodo.claves.sort()
            return

        i = 0
        while i < len(nodo.claves) and valor > nodo.claves[i]:
            i += 1

        if nodo.hijos[i] is None:
            nodo.hijos[i] = NodoMVias(self.orden)
            nodo.hijos[i].claves.append(valor)
        else:
            self._insertar(nodo.hijos[i], valor)

    # =========================
    # BÚSQUEDA SECUENCIAL
    # =========================

    def buscar(self, valor):

        valor = valor.upper()
        self.comparaciones = 0

        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):

        if nodo is None:
            return False, self.comparaciones

        for c in nodo.claves:
            self.comparaciones += 1
            if c == valor:
                return True, self.comparaciones

        i = 0
        while i < len(nodo.claves) and valor > nodo.claves[i]:
            self.comparaciones += 1
            i += 1

        return self._buscar(nodo.hijos[i], valor)

    # =========================
    # BÚSQUEDA BINARIA
    # =========================

    def buscar_binaria(self, valor):

        valor = valor.upper()
        self.comparaciones = 0

        return self._buscar_binaria(self.raiz, valor)

    def _buscar_binaria(self, nodo, valor):

        if nodo is None:
            return False, self.comparaciones

        izq = 0
        der = len(nodo.claves) - 1

        while izq <= der:

            mid = (izq + der) // 2
            self.comparaciones += 1

            if nodo.claves[mid] == valor:
                return True, self.comparaciones
            elif valor < nodo.claves[mid]:
                der = mid - 1
            else:
                izq = mid + 1

        return self._buscar_binaria(nodo.hijos[izq], valor)

    # =========================
    # ELIMINAR (simple)
    # =========================

    def eliminar(self, valor):

        if self.raiz is None:
            return

        valor = valor.upper()
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, valor):

        if nodo is None:
            return None

        if valor in nodo.claves:
            nodo.claves.remove(valor)

        i = 0
        while i < len(nodo.claves) and valor > nodo.claves[i]:
            i += 1

        nodo.hijos[i] = self._eliminar(nodo.hijos[i], valor)

        return nodo

    # =========================
    # RECORRIDO
    # =========================

    def obtener_palabras(self):

        res = []
        self._inorden(self.raiz, res)
        return res

    def _inorden(self, nodo, res):

        if nodo is None:
            return

        for i in range(len(nodo.claves)):
            self._inorden(nodo.hijos[i], res)
            res.append(nodo.claves[i])

        self._inorden(nodo.hijos[len(nodo.claves)], res)

    # =========================
    # ESTADÍSTICAS
    # =========================

    def contar_nodos(self):
        return self._contar(self.raiz)

    def _contar(self, nodo):

        if nodo is None:
            return 0

        total = 1
        for h in nodo.hijos:
            total += self._contar(h)
        return total

    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, nodo):

        if nodo is None:
            return 0

        return 1 + max(
            [self._altura(h) for h in nodo.hijos],
            default=0
        )

    def cantidad_palabras(self):
        return len(self.obtener_palabras())

    # =========================
    # ARCHIVOS
    # =========================

    def cargar_txt(self, ruta):

        with open(ruta, "r", encoding="utf-8") as f:
            for line in f:
                w = line.strip()
                if w:
                    self.insertar(w)

    def cargar_csv(self, ruta):

        with open(ruta, newline="", encoding="utf-8") as f:
            r = csv.reader(f)
            for row in r:
                for w in row:
                    w = w.strip()
                    if w:
                        self.insertar(w)