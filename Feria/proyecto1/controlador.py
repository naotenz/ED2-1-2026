from tkinter import filedialog, messagebox
from arbol_mvias import ArbolMVias
from vista import Vista


class Controlador:

    def __init__(self):

        self.vista = Vista()
        self.modelo = None

        self.vista.btn_crear.config(command=self.crear)
        self.vista.btn_insertar.config(command=self.insertar)
        self.vista.btn_buscar.config(command=self.buscar)
        self.vista.btn_binaria.config(command=self.buscar_bin)
        self.vista.btn_eliminar.config(command=self.eliminar)
        self.vista.btn_txt.config(command=self.txt)
        self.vista.btn_csv.config(command=self.csv)
        self.vista.btn_est.config(command=self.est)

    def validar(self):
        if not self.modelo:
            messagebox.showwarning("Error", "Crea el árbol primero")
            return False
        return True

    def crear(self):

        o = self.vista.get_orden()

        if o < 2:
            messagebox.showwarning("Error", "Orden mínimo 2")
            return

        self.modelo = ArbolMVias(o)
        self.vista.msg(f"Árbol creado orden {o}")
        self.actualizar()

    def insertar(self):

        if not self.validar():
            return

        w = self.vista.get_palabra()
        self.modelo.insertar(w)
        self.vista.msg(f"Insertado {w}")
        self.actualizar()

    def buscar(self):

        if not self.validar():
            return

        w = self.vista.get_palabra()
        ok, c = self.modelo.buscar(w)
        self.vista.msg(f"{w} -> {ok} ({c})")

    def buscar_bin(self):

        if not self.validar():
            return

        w = self.vista.get_palabra()
        ok, c = self.modelo.buscar_binaria(w)
        self.vista.msg(f"{w} -> {ok} ({c})")

    def eliminar(self):

        if not self.validar():
            return

        w = self.vista.get_palabra()
        self.modelo.eliminar(w)
        self.vista.msg(f"Eliminado {w}")
        self.actualizar()

    def txt(self):

        if not self.validar():
            return

        f = filedialog.askopenfilename(filetypes=[("txt", "*.txt")])
        if f:
            self.modelo.cargar_txt(f)
            self.actualizar()

    def csv(self):

        if not self.validar():
            return

        f = filedialog.askopenfilename(filetypes=[("csv", "*.csv")])
        if f:
            self.modelo.cargar_csv(f)
            self.actualizar()

    def est(self):

        if not self.validar():
            return

        self.vista.msg(
            f"Palabras: {self.modelo.cantidad_palabras()}\n"
            f"Nodos: {self.modelo.contar_nodos()}\n"
            f"Altura: {self.modelo.altura()}"
        )

    def actualizar(self):

        if self.modelo:
            self.vista.dibujar(self.modelo.raiz)
        else:
            self.vista.canvas.delete("all")

    def run(self):
        self.vista.run()

    def iniciar(self):
        self.run()