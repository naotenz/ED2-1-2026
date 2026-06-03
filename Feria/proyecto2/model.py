"""
MODEL
Contiene la lógica del Árbol M-Vías y la clase Archivo.
"""

class Archivo:
    def __init__(self, codigo, nombre, tipo, tamano):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo = tipo
        self.tamano = tamano


class ArbolMVias:
    def __init__(self):
        self.datos = []  # versión simplificada tipo M-Vías

    def insertar(self, archivo):
        """Inserta archivo en el árbol"""
        self.datos.append(archivo)
        self.datos.sort(key=lambda x: x.codigo)

    def buscar(self, codigo):
        """Busca archivo por código"""
        for a in self.datos:
            if a.codigo == codigo:
                return a
        return None

    def eliminar(self, codigo):
        """Elimina archivo por código"""
        self.datos = [a for a in self.datos if a.codigo != codigo]

    def inorden(self):
        """Devuelve lista ordenada"""
        return self.datos