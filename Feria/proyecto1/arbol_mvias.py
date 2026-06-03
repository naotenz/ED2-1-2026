from nodo_mvias import NodoMVias
import csv


class ArbolMVias:

    def __init__(self, orden=4):
        self.orden = orden
        self.raiz = None
        self.comparaciones = 0

    # ==================================================
    # INSERCIÓN
    # ==================================================

    def insertar(self, palabra):

        palabra = palabra.strip().upper()

        if not palabra:
            return

        if self.raiz is None:
            self.raiz = NodoMVias(self.orden)
            self.raiz.claves.append(palabra)
            return

        self._insertar(self.raiz, palabra)

    def _insertar(self, nodo, palabra):

        if palabra in nodo.claves:
            return

        if len(nodo.claves) < self.orden - 1:
            nodo.claves.append(palabra)
            nodo.claves.sort()
            return

        i = 0

        while i < len(nodo.claves) and palabra > nodo.claves[i]:
            i += 1

        if nodo.hijos[i] is None:
            nodo.hijos[i] = NodoMVias(self.orden)
            nodo.hijos[i].claves.append(palabra)
        else:
            self._insertar(nodo.hijos[i], palabra)

    # ==================================================
    # BÚSQUEDA SECUENCIAL
    # ==================================================

    def buscar(self, palabra):

        palabra = palabra.upper()
        self.comparaciones = 0

        encontrado = self._buscar(self.raiz, palabra)

        return encontrado, self.comparaciones

    def _buscar(self, nodo, palabra):

        if nodo is None:
            return False

        for clave in nodo.claves:

            self.comparaciones += 1

            if clave == palabra:
                return True

        i = 0

        while i < len(nodo.claves) and palabra > nodo.claves[i]:
            self.comparaciones += 1
            i += 1

        return self._buscar(nodo.hijos[i], palabra)

    # ==================================================
    # BÚSQUEDA BINARIA
    # ==================================================

    def buscar_binaria(self, palabra):

        palabra = palabra.upper()
        self.comparaciones = 0

        return self._buscar_binaria(
            self.raiz,
            palabra
        )

    def _buscar_binaria(self, nodo, palabra):

        if nodo is None:
            return False, self.comparaciones

        izquierda = 0
        derecha = len(nodo.claves) - 1

        while izquierda <= derecha:

            medio = (izquierda + derecha) // 2

            self.comparaciones += 1

            if nodo.claves[medio] == palabra:
                return True, self.comparaciones

            elif palabra < nodo.claves[medio]:
                derecha = medio - 1

            else:
                izquierda = medio + 1

        return self._buscar_binaria(
            nodo.hijos[izquierda],
            palabra
        )

    # ==================================================
    # ELIMINAR
    # ==================================================

    def eliminar(self, palabra):

        palabra = palabra.upper()

        self.raiz = self._eliminar(
            self.raiz,
            palabra
        )

    def _eliminar(self, nodo, palabra):

        if nodo is None:
            return None

        if palabra in nodo.claves:

            nodo.claves.remove(palabra)

            if len(nodo.claves) == 0 and nodo.es_hoja():
                return None

            return nodo

        i = 0

        while i < len(nodo.claves) and palabra > nodo.claves[i]:
            i += 1

        nodo.hijos[i] = self._eliminar(
            nodo.hijos[i],
            palabra
        )

        return nodo

    # ==================================================
    # RECORRIDO
    # ==================================================

    def obtener_palabras(self):

        resultado = []

        self._inorden(
            self.raiz,
            resultado
        )

        return resultado

    def _inorden(self, nodo, lista):

        if nodo is None:
            return

        for i in range(len(nodo.claves)):

            self._inorden(
                nodo.hijos[i],
                lista
            )

            lista.append(
                nodo.claves[i]
            )

        self._inorden(
            nodo.hijos[len(nodo.claves)],
            lista
        )

    # ==================================================
    # CARGA TXT
    # ==================================================

    def cargar_txt(self, archivo):

        with open(
            archivo,
            "r",
            encoding="utf-8"
        ) as f:

            for linea in f:

                palabra = linea.strip()

                if palabra:
                    self.insertar(palabra)

    # ==================================================
    # CARGA CSV
    # ==================================================

    def cargar_csv(self, archivo):

        with open(
            archivo,
            newline="",
            encoding="utf-8"
        ) as f:

            lector = csv.reader(f)

            for fila in lector:

                for palabra in fila:

                    palabra = palabra.strip()

                    if palabra:
                        self.insertar(palabra)

    # ==================================================
    # ESTADÍSTICAS
    # ==================================================

    def cantidad_palabras(self):
        return len(self.obtener_palabras())

    def contar_nodos(self):
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo):

        if nodo is None:
            return 0

        total = 1

        for hijo in nodo.hijos:
            total += self._contar_nodos(hijo)

        return total

    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, nodo):

        if nodo is None:
            return 0

        alturas = []

        for hijo in nodo.hijos:
            alturas.append(
                self._altura(hijo)
            )

        return 1 + max(alturas, default=0)