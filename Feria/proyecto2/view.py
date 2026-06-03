"""
VIEW
Interfaz gráfica del sistema (Tkinter)
"""

import tkinter as tk


class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Archivos MVC - Árbol M-Vías")

        self.codigo = tk.Entry(root)
        self.nombre = tk.Entry(root)
        self.tipo = tk.Entry(root)
        self.tamano = tk.Entry(root)

        tk.Label(root, text="Código").pack()
        self.codigo.pack()

        tk.Label(root, text="Nombre").pack()
        self.nombre.pack()

        tk.Label(root, text="Tipo").pack()
        self.tipo.pack()

        tk.Label(root, text="Tamaño").pack()
        self.tamano.pack()

        self.btn_agregar = tk.Button(root, text="Agregar")
        self.btn_buscar = tk.Button(root, text="Buscar")
        self.btn_eliminar = tk.Button(root, text="Eliminar")
        self.btn_mostrar = tk.Button(root, text="Mostrar")

        self.btn_agregar.pack()
        self.btn_buscar.pack()
        self.btn_eliminar.pack()
        self.btn_mostrar.pack()

        self.resultado = tk.Text(root, height=10)
        self.resultado.pack()