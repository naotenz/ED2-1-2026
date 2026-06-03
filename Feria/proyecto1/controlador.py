from tkinter import filedialog, messagebox

from arbol_mvias import ArbolMVias
from vista import Vista


class Controlador:

    def __init__(self):

        self.modelo = ArbolMVias(4)
        self.vista = Vista()

        # ==========================
        # ASIGNAR EVENTOS
        # ==========================

        self.vista.btn_insertar.config(
            command=self.insertar
        )

        self.vista.btn_buscar.config(
            command=self.buscar
        )

        self.vista.btn_buscar_binaria.config(
            command=self.buscar_binaria
        )

        self.vista.btn_eliminar.config(
            command=self.eliminar
        )

        self.vista.btn_mostrar.config(
            command=self.mostrar_palabras
        )

        self.vista.btn_estadisticas.config(
            command=self.mostrar_estadisticas
        )

        self.vista.btn_cargar_txt.config(
            command=self.cargar_txt
        )

        self.vista.btn_cargar_csv.config(
            command=self.cargar_csv
        )

        # Dibujo inicial
        self.actualizar_vista()

    # =====================================
    # ACTUALIZAR ÁRBOL EN PANTALLA
    # =====================================

    def actualizar_vista(self):

        self.vista.dibujar_arbol(
            self.modelo.raiz
        )

    # =====================================
    # INSERTAR
    # =====================================

    def insertar(self):

        palabra = self.vista.obtener_palabra().strip()

        if not palabra:

            messagebox.showwarning(
                "Advertencia",
                "Ingrese una palabra"
            )

            return

        self.modelo.insertar(palabra)

        self.vista.mostrar_mensaje(
            f"✓ Insertada: {palabra.upper()}"
        )

        self.vista.limpiar_entrada()

        self.actualizar_vista()

    # =====================================
    # BUSCAR SECUENCIAL
    # =====================================

    def buscar(self):

        palabra = self.vista.obtener_palabra().strip()

        if not palabra:
            return

        encontrado, comparaciones = (
            self.modelo.buscar(palabra)
        )

        if encontrado:

            self.vista.mostrar_mensaje(
                f"✓ '{palabra.upper()}' encontrada "
                f"(Comparaciones: {comparaciones})"
            )

        else:

            self.vista.mostrar_mensaje(
                f"✗ '{palabra.upper()}' NO encontrada "
                f"(Comparaciones: {comparaciones})"
            )

    # =====================================
    # BUSCAR BINARIA
    # =====================================

    def buscar_binaria(self):

        palabra = self.vista.obtener_palabra().strip()

        if not palabra:
            return

        encontrado, comparaciones = (
            self.modelo.buscar_binaria(
                palabra
            )
        )

        if encontrado:

            self.vista.mostrar_mensaje(
                f"✓ Binaria: '{palabra.upper()}' encontrada "
                f"(Comparaciones: {comparaciones})"
            )

        else:

            self.vista.mostrar_mensaje(
                f"✗ Binaria: '{palabra.upper()}' NO encontrada "
                f"(Comparaciones: {comparaciones})"
            )

    # =====================================
    # ELIMINAR
    # =====================================

    def eliminar(self):

        palabra = self.vista.obtener_palabra().strip()

        if not palabra:
            return

        self.modelo.eliminar(palabra)

        self.vista.mostrar_mensaje(
            f"🗑 Eliminada: {palabra.upper()}"
        )

        self.vista.limpiar_entrada()

        self.actualizar_vista()

    # =====================================
    # MOSTRAR PALABRAS
    # =====================================

    def mostrar_palabras(self):

        palabras = self.modelo.obtener_palabras()

        self.vista.limpiar_area()

        self.vista.mostrar_mensaje(
            "===== PALABRAS ====="
        )

        for palabra in palabras:

            self.vista.mostrar_mensaje(
                palabra
            )

        self.vista.mostrar_mensaje(
            f"\nTotal: {len(palabras)}"
        )

    # =====================================
    # ESTADÍSTICAS
    # =====================================

    def mostrar_estadisticas(self):

        total_palabras = (
            self.modelo.cantidad_palabras()
        )

        total_nodos = (
            self.modelo.contar_nodos()
        )

        altura = (
            self.modelo.altura()
        )

        texto = (
            "\n===== ESTADÍSTICAS =====\n"
            f"Palabras almacenadas: {total_palabras}\n"
            f"Número de nodos: {total_nodos}\n"
            f"Altura del árbol: {altura}\n"
        )

        self.vista.mostrar_mensaje(texto)

        messagebox.showinfo(
            "Estadísticas",
            texto
        )

    # =====================================
    # CARGAR TXT
    # =====================================

    def cargar_txt(self):

        archivo = filedialog.askopenfilename(
            title="Seleccionar archivo TXT",
            filetypes=[
                ("Archivo TXT", "*.txt")
            ]
        )

        if not archivo:
            return

        try:

            self.modelo.cargar_txt(
                archivo
            )

            self.vista.mostrar_mensaje(
                f"TXT cargado:\n{archivo}"
            )

            self.actualizar_vista()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =====================================
    # CARGAR CSV
    # =====================================

    def cargar_csv(self):

        archivo = filedialog.askopenfilename(
            title="Seleccionar archivo CSV",
            filetypes=[
                ("Archivo CSV", "*.csv")
            ]
        )

        if not archivo:
            return

        try:

            self.modelo.cargar_csv(
                archivo
            )

            self.vista.mostrar_mensaje(
                f"CSV cargado:\n{archivo}"
            )

            self.actualizar_vista()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =====================================
    # EJECUTAR APP
    # =====================================

    def iniciar(self):

        self.vista.iniciar()