import tkinter as tk
from tkinter import scrolledtext


class Vista:

    def __init__(self):

        self.ventana = tk.Tk()

        self.ventana.title(
            "Sistema de Gestión de Diccionario - Árbol M-Vías"
        )

        self.ventana.geometry("1200x750")

        # =====================================
        # PANEL SUPERIOR
        # =====================================

        frame_superior = tk.Frame(
            self.ventana
        )

        frame_superior.pack(
            fill="x",
            padx=10,
            pady=10
        )

        # -------------------------------------
        # PALABRA
        # -------------------------------------

        tk.Label(
            frame_superior,
            text="Palabra:"
        ).pack(side="left")

        self.entrada_palabra = tk.Entry(
            frame_superior,
            width=25
        )

        self.entrada_palabra.pack(
            side="left",
            padx=5
        )

        # -------------------------------------
        # ORDEN DEL ÁRBOL
        # -------------------------------------

        tk.Label(
            frame_superior,
            text="Orden:"
        ).pack(
            side="left",
            padx=(20, 0)
        )

        self.entrada_orden = tk.Entry(
            frame_superior,
            width=5
        )

        self.entrada_orden.insert(
            0,
            "4"
        )

        self.entrada_orden.pack(
            side="left",
            padx=5
        )

        # =====================================
        # BOTONES
        # =====================================

        frame_botones = tk.Frame(
            self.ventana
        )

        frame_botones.pack(
            fill="x",
            padx=10
        )

        self.btn_crear_arbol = tk.Button(
            frame_botones,
            text="Crear Árbol",
            width=12
        )

        self.btn_insertar = tk.Button(
            frame_botones,
            text="Insertar",
            width=12
        )

        self.btn_buscar = tk.Button(
            frame_botones,
            text="Buscar",
            width=12
        )

        self.btn_buscar_binaria = tk.Button(
            frame_botones,
            text="Buscar Binaria",
            width=15
        )

        self.btn_eliminar = tk.Button(
            frame_botones,
            text="Eliminar",
            width=12
        )

        self.btn_mostrar = tk.Button(
            frame_botones,
            text="Mostrar",
            width=12
        )

        self.btn_estadisticas = tk.Button(
            frame_botones,
            text="Estadísticas",
            width=12
        )

        self.btn_cargar_txt = tk.Button(
            frame_botones,
            text="Cargar TXT",
            width=12
        )

        self.btn_cargar_csv = tk.Button(
            frame_botones,
            text="Cargar CSV",
            width=12
        )

        self.btn_crear_arbol.pack(
            side="left",
            padx=2
        )

        self.btn_insertar.pack(
            side="left",
            padx=2
        )

        self.btn_buscar.pack(
            side="left",
            padx=2
        )

        self.btn_buscar_binaria.pack(
            side="left",
            padx=2
        )

        self.btn_eliminar.pack(
            side="left",
            padx=2
        )

        self.btn_mostrar.pack(
            side="left",
            padx=2
        )

        self.btn_estadisticas.pack(
            side="left",
            padx=2
        )

        self.btn_cargar_txt.pack(
            side="left",
            padx=2
        )

        self.btn_cargar_csv.pack(
            side="left",
            padx=2
        )

        # =====================================
        # CONTENIDO
        # =====================================

        frame_central = tk.Frame(
            self.ventana
        )

        frame_central.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # -------------------------------------
        # ÁREA DE MENSAJES
        # -------------------------------------

        self.area_texto = scrolledtext.ScrolledText(
            frame_central,
            width=40,
            height=20
        )

        self.area_texto.pack(
            side="left",
            fill="y"
        )

        # -------------------------------------
        # CANVAS DEL ÁRBOL
        # -------------------------------------

        self.canvas = tk.Canvas(
            frame_central,
            bg="white"
        )

        self.canvas.pack(
            side="right",
            fill="both",
            expand=True
        )

    # =====================================
    # MÉTODOS AUXILIARES
    # =====================================

    def obtener_palabra(self):
        return self.entrada_palabra.get()

    def obtener_orden(self):

        try:
            return int(
                self.entrada_orden.get()
            )
        except:
            return 4

    def limpiar_entrada(self):

        self.entrada_palabra.delete(
            0,
            tk.END
        )

    def mostrar_mensaje(
        self,
        mensaje
    ):

        self.area_texto.insert(
            tk.END,
            mensaje + "\n"
        )

        self.area_texto.see(
            tk.END
        )

    def limpiar_area(self):

        self.area_texto.delete(
            "1.0",
            tk.END
        )

    # =====================================
    # DIBUJAR ÁRBOL
    # =====================================

    def dibujar_arbol(
        self,
        raiz
    ):

        self.canvas.delete("all")

        self.canvas.update_idletasks()

        ancho = self.canvas.winfo_width()

        if ancho < 100:
            ancho = 1000

        if raiz is None:

            self.canvas.create_text(
                ancho // 2,
                50,
                text="Árbol vacío",
                font=("Arial", 14)
            )

            return

        self._dibujar_nodo(
            raiz,
            ancho // 2,
            50,
            ancho // 4
        )

    def _dibujar_nodo(
        self,
        nodo,
        x,
        y,
        separacion
    ):

        if nodo is None:
            return

        texto = " | ".join(
            nodo.claves
        )

        ancho_nodo = max(
            70,
            len(texto) * 9
        )

        alto_nodo = 40

        self.canvas.create_rectangle(
            x - ancho_nodo // 2,
            y - alto_nodo // 2,
            x + ancho_nodo // 2,
            y + alto_nodo // 2
        )

        self.canvas.create_text(
            x,
            y,
            text=texto
        )

        hijos_validos = [
            h for h in nodo.hijos
            if h is not None
        ]

        cantidad = len(
            hijos_validos
        )

        if cantidad == 0:
            return

        inicio = x - separacion

        if cantidad == 1:
            paso = 0
        else:
            paso = (
                (2 * separacion)
                // (cantidad - 1)
            )

        indice = 0

        for hijo in nodo.hijos:

            if hijo is not None:

                nuevo_x = (
                    inicio
                    + indice * paso
                )

                nuevo_y = y + 100

                self.canvas.create_line(
                    x,
                    y + 20,
                    nuevo_x,
                    nuevo_y - 20
                )

                self._dibujar_nodo(
                    hijo,
                    nuevo_x,
                    nuevo_y,
                    max(
                        60,
                        separacion // 2
                    )
                )

                indice += 1

    # =====================================
    # EJECUTAR VENTANA
    # =====================================

    def iniciar(self):
        self.ventana.mainloop()