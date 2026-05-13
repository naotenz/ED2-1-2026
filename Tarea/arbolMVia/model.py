from typing import List, Optional


class Nodo:
    """
    Representa un nodo de un árbol m-vías.

    Atributos:
        m (int): orden máximo del nodo.
        claves (List[int]): lista ordenada de claves almacenadas.
        hijos (List[Nodo]): lista de referencias a nodos hijos.
    """
    def __init__(self, m: int):
        self.m = m
        self.claves: List[int] = []
        self.hijos: List['Nodo'] = []


class ArbolMViasModel:
    """
    Modelo de un árbol m-vías.

    Implementa operaciones básicas:
    - inserción
    - búsqueda
    - recorridos (inorden, preorden, postorden)
    - eliminación por reconstrucción
    """
    def __init__(self, m: int = 3):
        """
        Inicializa el árbol.

        Args:
            m (int): número máximo de claves por nodo.
        """
        self.m = m
        self.raiz: Optional[Nodo] = None

    # ---------------- INSERTAR ----------------
    def insertar(self, clave: int):
        """
        Inserta una clave en el árbol.

        Si el árbol está vacío, crea la raíz.
        Si no, delega la inserción al método recursivo.
        """
        if not self.raiz:
            self.raiz = Nodo(self.m)
            self.raiz.claves.append(clave)
            return
        self._insertar(self.raiz, clave)

    def _insertar(self, nodo: Nodo, clave: int):
        """
        Inserción recursiva en un nodo del árbol.

        Determina la posición correcta de la clave
        y la inserta en hoja o la envía a hijos.
        """
        i = 0
        while i < len(nodo.claves) and clave > nodo.claves[i]:
            i += 1

        if len(nodo.hijos) == 0:
            if len(nodo.claves) < nodo.m:
                nodo.claves.insert(i, clave)
            else:
                nuevo = Nodo(self.m)
                nuevo.claves.append(clave)

                while len(nodo.hijos) < len(nodo.claves) + 1:
                    nodo.hijos.append(None)

                nodo.hijos[i] = nuevo
        else:
            while len(nodo.hijos) < len(nodo.claves) + 1:
                nodo.hijos.append(None)

            if nodo.hijos[i] is None:
                nuevo = Nodo(self.m)
                nuevo.claves.append(clave)
                nodo.hijos[i] = nuevo
            else:
                self._insertar(nodo.hijos[i], clave)

    # ---------------- BUSCAR ----------------
    def buscar(self, nodo: Nodo, clave: int):
        """
        Busca una clave en el árbol.

        Retorna:
            bool: True si existe, False si no.
        """
        if not nodo:
            return False

        i = 0
        while i < len(nodo.claves) and clave > nodo.claves[i]:
            i += 1

        if i < len(nodo.claves) and nodo.claves[i] == clave:
            return True

        if len(nodo.hijos) == 0:
            return False

        if i < len(nodo.hijos) and nodo.hijos[i]:
            return self.buscar(nodo.hijos[i], clave)

        return False

    # ---------------- RECORRIDOS ----------------
    def inorden(self, nodo: Nodo, res):
        
        if not nodo:
            return

        for i in range(len(nodo.claves)):
            if i < len(nodo.hijos) and nodo.hijos[i]:
                self.inorden(nodo.hijos[i], res)
            res.append(nodo.claves[i])

        if len(nodo.hijos) > len(nodo.claves):
            self.inorden(nodo.hijos[-1], res)

    def preorden(self, nodo: Nodo, res):
        if not nodo:
            return

        for c in nodo.claves:
            res.append(c)

        for h in nodo.hijos:
            if h:
                self.preorden(h, res)

    def postorden(self, nodo: Nodo, res):
        if not nodo:
            return

        for h in nodo.hijos:
            if h:
                self.postorden(h, res)

        for c in nodo.claves:
            res.append(c)

    # ---------------- ELIMINAR (básico) ----------------
    def eliminar(self, clave: int):
        """
        Elimina una clave del árbol.

        Estrategia:
        - convierte el árbol a lista (inorden)
        - elimina la clave
        - reconstruye el árbol desde cero
        """
        if not self.raiz:
            return

        valores = []
        self.inorden(self.raiz, valores)

        if clave not in valores:
            return

        valores.remove(clave)

        # reconstruir correctamente
        self.raiz = None

        for v in valores:
            self.insertar(v)

    # limpiar canvas correctamente lo hará el controller con dibujar
    
    def _eliminar_rec(self, nodo, clave):
        """
        (No usado en la versión actual)

        Eliminación recursiva directa.
        No se usa porque esta implementación
        reconstruye el árbol.
        """
        if not nodo:
            return

        if clave in nodo.claves:
            nodo.claves.remove(clave)
            return

        for h in nodo.hijos:
            if h:
                self._eliminar_rec(h, clave)

    def get_raiz(self):
        
        return self.raiz