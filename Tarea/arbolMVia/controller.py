from tkinter import messagebox
from model import ArbolMViasModel


class ArbolMViasController:
    """
    Controlador del sistema MVC para el árbol m-vías.

    Se encarga de:
    - Conectar la vista con el modelo
    - Manejar eventos de botones
    - Validar entradas del usuario
    - Actualizar la visualización del árbol
    """

    def __init__(self, view):
        """
        Inicializa el controlador.

        Args:
            view: instancia de la vista (Tkinter)
        """
        self.view = view
        self.model = None
        self.conectar()

    def conectar(self):
        """
        Conecta los botones de la interfaz con sus respectivas funciones.
        """
        self.view.btn_definir.config(command=self.definir)
        self.view.btn_insertar.config(command=self.insertar)

        self.view.btn_buscar.config(command=self.buscar)
        self.view.btn_eliminar.config(command=self.eliminar)
        self.view.btn_inorden.config(command=self.inorden)
        self.view.btn_preorden.config(command=self.preorden)
        self.view.btn_postorden.config(command=self.postorden)

    # ---------------- DEFINIR ÁRBOL ----------------
    def definir(self):
        """
        Define el orden del árbol m-vías (m) e inicializa el modelo.

        Valida que el valor ingresado sea un entero válido y >= 2.
        """
        try:
            m = int(self.view.entry_m.get())

            if m < 2:
                messagebox.showerror("Error", "El orden debe ser >= 2")
                return

            self.model = ArbolMViasModel(m)

            self.view.btn_insertar.config(state="normal")
            self.view.dibujar_arbol(self.model.get_raiz())

        except ValueError:
            messagebox.showerror("Error", "m debe ser un número entero")

    # ---------------- INSERTAR ----------------
    def insertar(self):
        """
        Inserta una clave en el árbol y actualiza la vista.
        """
        if not self.model:
            messagebox.showwarning("Aviso", "Primero define el árbol")
            return

        try:
            v = int(self.view.entry_valor.get())
            self.model.insertar(v)
            self.view.dibujar_arbol(self.model.get_raiz())

        except ValueError:
            messagebox.showerror("Error", "Valor inválido")

    # ---------------- BUSCAR ----------------
    def buscar(self):
        """
        Busca una clave en el árbol y muestra el resultado.
        """
        if not self.model:
            return

        try:
            v = int(self.view.entry_valor.get())
            ok = self.model.buscar(self.model.get_raiz(), v)

            messagebox.showinfo(
                "Buscar",
                "Encontrado" if ok else "No encontrado"
            )

        except ValueError:
            messagebox.showerror("Error", "Valor inválido")

    # ---------------- ELIMINAR ----------------
    def eliminar(self):
        """
        Elimina una clave del árbol y actualiza la vista.
        """
        if not self.model:
            return

        try:
            v = int(self.view.entry_valor.get())
            self.model.eliminar(v)
            self.view.dibujar_arbol(self.model.get_raiz())

        except ValueError:
            messagebox.showerror("Error", "Valor inválido")

    # ---------------- RECORRIDOS ----------------
    def inorden(self):
        """
        Muestra el recorrido inorden del árbol.
        """
        if not self.model:
            return

        res = []
        self.model.inorden(self.model.get_raiz(), res)
        messagebox.showinfo("Inorden", str(res))

    def preorden(self):
        """
        Muestra el recorrido preorden del árbol.
        """
        if not self.model:
            return

        res = []
        self.model.preorden(self.model.get_raiz(), res)
        messagebox.showinfo("Preorden", str(res))

    def postorden(self):
        """
        Muestra el recorrido postorden del árbol.
        """
        if not self.model:
            return

        res = []
        self.model.postorden(self.model.get_raiz(), res)
        messagebox.showinfo("Postorden", str(res))