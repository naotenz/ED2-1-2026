"""

Representa un archivo dentro del gestor.
"""

class Archivo:

    def __init__(self, nombre, tamano, tipo):
        self.nombre = nombre
        self.tamano = tamano
        self.tipo = tipo

    def __str__(self):
        return f"Nombre: {self.nombre} | Tamaño: {self.tamano} KB | Tipo: {self.tipo}"