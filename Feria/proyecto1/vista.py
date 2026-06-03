import tkinter as tk
from tkinter import scrolledtext


class Vista:

    def __init__(self):

        self.ventana = tk.Tk()

        self.ventana.title(
            "Diccionario M-Vías"
        )

        self.ventana.geometry(
            "700x500"
        )

        self.entrada = tk.Entry(
            self.ventana,
            width=40
        )

        self.entrada.pack(pady=10)

        self.btn_insertar = tk.Button(
            self.ventana,
            text="Insertar"
        )

        self.btn_insertar.pack()

        self.btn_buscar = tk.Button(
            self.ventana,
            text="Buscar"
        )

        self.btn_buscar.pack()

        self.btn_eliminar = tk.Button(
            self.ventana,
            text="Eliminar"
        )

        self.btn_eliminar.pack()

        self.btn_mostrar = tk.Button(
            self.ventana,
            text="Mostrar"
        )

        self.btn_mostrar.pack()

        self.btn_estadisticas = tk.Button(
            self.ventana,
            text="Estadísticas"
        )

        self.btn_estadisticas.pack()

        self.area = scrolledtext.ScrolledText(
            self.ventana,
            width=80,
            height=20
        )

        self.area.pack(pady=10)

    def iniciar(self):
        self.ventana.mainloop()