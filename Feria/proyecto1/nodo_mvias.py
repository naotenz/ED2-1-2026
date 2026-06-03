class NodoMVias:
    """
    Nodo para Árbol M-Vías.
    Un nodo puede almacenar hasta (orden - 1) claves
    y tener hasta (orden) hijos.
    """

    def __init__(self, orden):
        self.orden = orden
        self.claves = []
        self.hijos = [None] * orden

    def esta_lleno(self):
        return len(self.claves) >= self.orden - 1

    def es_hoja(self):
        return all(hijo is None for hijo in self.hijos)

    def __str__(self):
        return str(self.claves)