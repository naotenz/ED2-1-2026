from tkinter import messagebox

from arbol_mvias import ArbolMVias
from vista import Vista


class Controlador:

    def __init__(self):

        self.modelo = ArbolMVias()
        self.vista = Vista()

        self.vista.btn_insertar.config(
            command=self.insertar
        )

        self.vista.btn_buscar.config(
            command=self.buscar
        )

        self.vista.btn_eliminar.config(
            command=self.eliminar
        )

        self.vista.btn_mostrar.config(
            command=self.mostrar
        )

        self.vista.btn_estadisticas.config(
            command=self.estadisticas
        )

    def insertar(self):

        palabra = self.vista.entrada.get()

        self.modelo.insertar(
            palabra
        )

        messagebox.showinfo(
            "Éxito",
            "Palabra insertada"
        )

    def buscar(self):

        palabra = self.vista.entrada.get()

        encontrado, comparaciones = \
            self.modelo.buscar(
                palabra
            )

        if encontrado:

            messagebox.showinfo(
                "Resultado",
                f"Encontrada\nComparaciones: {comparaciones}"
            )

        else:

            messagebox.showwarning(
                "Resultado",
                "No encontrada"
            )

    def eliminar(self):

        palabra = self.vista.entrada.get()

        self.modelo.eliminar(
            palabra
        )

        messagebox.showinfo(
            "Eliminar",
            "Palabra eliminada"
        )

    def mostrar(self):

        palabras = self.modelo.obtener_palabras()

        self.vista.area.delete(
            "1.0",
            "end"
        )

        for palabra in palabras:

            self.vista.area.insert(
                "end",
                palabra + "\n"
            )

    def estadisticas(self):

        texto = (
            f"Palabras: {self.modelo.cantidad_palabras()}\n"
            f"Nodos: {self.modelo.contar_nodos()}\n"
            f"Altura: {self.modelo.altura()}\n"
        )

        messagebox.showinfo(
            "Estadísticas",
            texto
        )