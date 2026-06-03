class NodoMVias:

    def __init__(self, orden):

        self.orden = orden
        self.claves = []
        self.hijos = [None] * orden