import tkinter as tk
from tkinter import scrolledtext


class Vista:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Diccionario M-Vías")
        self.root.geometry("1200x750")

        # ======================
        # ENTRADAS
        # ======================

        top = tk.Frame(self.root)
        top.pack(fill="x")

        tk.Label(top, text="Palabra").pack(side="left")

        self.entrada = tk.Entry(top, width=25)
        self.entrada.pack(side="left")

        tk.Label(top, text="Orden").pack(side="left")

        self.orden = tk.Entry(top, width=5)
        self.orden.insert(0, "4")
        self.orden.pack(side="left")

        # ======================
        # BOTONES
        # ======================

        btns = tk.Frame(self.root)
        btns.pack(fill="x")

        self.btn_crear = tk.Button(btns, text="Crear Árbol")
        self.btn_insertar = tk.Button(btns, text="Insertar")
        self.btn_buscar = tk.Button(btns, text="Buscar")
        self.btn_binaria = tk.Button(btns, text="Buscar Binaria")
        self.btn_eliminar = tk.Button(btns, text="Eliminar")
        self.btn_txt = tk.Button(btns, text="TXT")
        self.btn_csv = tk.Button(btns, text="CSV")
        self.btn_est = tk.Button(btns, text="Ubicacion")

        for b in [
            self.btn_crear,
            self.btn_insertar,
            self.btn_buscar,
            self.btn_binaria,
            self.btn_eliminar,
            self.btn_txt,
            self.btn_csv,
            self.btn_est
        ]:
            b.pack(side="left")

        # ======================
        # SALIDA
        # ======================

        cont = tk.Frame(self.root)
        cont.pack(fill="both", expand=True)

        self.texto = scrolledtext.ScrolledText(cont, width=40)
        self.texto.pack(side="left", fill="y")

        self.canvas = tk.Canvas(cont, bg="white")
        self.canvas.pack(side="right", fill="both", expand=True)

    # ======================
    # MÉTODOS
    # ======================

    def get_palabra(self):
        return self.entrada.get()

    def get_orden(self):
        try:
            return int(self.orden.get())
        except:
            return 4

    def limpiar(self):
        self.entrada.delete(0, tk.END)

    def msg(self, m):
        self.texto.insert(tk.END, m + "\n")

    def dibujar(self, raiz):

        self.canvas.delete("all")

        if not raiz:
            self.canvas.create_text(400, 50, text="Árbol vacío")
            return

        self._dibujar(raiz, 500, 50, 200)

    def _dibujar(self, nodo, x, y, sep):

        txt = " | ".join(nodo.claves)

        self.canvas.create_rectangle(x-50, y-20, x+50, y+20)
        self.canvas.create_text(x, y, text=txt)

        hijos = [h for h in nodo.hijos if h]

        i = 0
        for h in nodo.hijos:
            if h:
                nx = x - sep + i * 80
                ny = y + 80

                self.canvas.create_line(x, y+20, nx, ny-20)
                self._dibujar(h, nx, ny, max(50, sep//2))
                i += 1

    def run(self):
        self.root.mainloop()