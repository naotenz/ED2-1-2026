"""
===========================================================
Archivo: ventana.py

Descripción:
-------------
Interfaz principal del sistema de delivery.

Incluye:
- Selección de origen y destino
- Selección de algoritmo
- Botón de ejecución
- Panel de grafo
===========================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox

from views.panel_grafo import PanelGrafo


class Ventana:

    def __init__(self, controlador):

        self.controlador = controlador

        self.root = tk.Tk()
        self.root.title("Sistema de Rutas - Delivery")
        self.root.geometry("1000x700")

        # ---------------- VARIABLES ----------------

        self.origen = tk.StringVar()
        self.destino = tk.StringVar()
        self.algoritmo = tk.StringVar(value="DIJKSTRA")

        # ---------------- CONTROLES ----------------

        top = tk.Frame(self.root)
        top.pack(pady=10)

        tk.Label(top, text="Origen").grid(row=0, column=0)
        self.cb_origen = ttk.Combobox(top, textvariable=self.origen, width=20)
        self.cb_origen.grid(row=0, column=1, padx=5)

        tk.Label(top, text="Destino").grid(row=0, column=2)
        self.cb_destino = ttk.Combobox(top, textvariable=self.destino, width=20)
        self.cb_destino.grid(row=0, column=3, padx=5)

        # ---------------- RADIO BUTTONS ----------------

        algo_frame = tk.Frame(self.root)
        algo_frame.pack()

        tk.Radiobutton(algo_frame, text="BFS",
                       variable=self.algoritmo, value="BFS").pack(side="left")

        tk.Radiobutton(algo_frame, text="DFS",
                       variable=self.algoritmo, value="DFS").pack(side="left")

        tk.Radiobutton(algo_frame, text="Dijkstra",
                       variable=self.algoritmo, value="DIJKSTRA").pack(side="left")

        tk.Radiobutton(algo_frame, text="Warshall",
                       variable=self.algoritmo, value="WARSHALL").pack(side="left")

        # ---------------- BOTÓN ----------------

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=10)

        tk.Button(
            buttons_frame,
            text="Buscar Ruta",
            command=self.buscar
        ).pack(side="left", padx=5)

        tk.Button(
            buttons_frame,
            text="Reiniciar",
            command=self.reiniciar
        ).pack(side="left", padx=5)

        tk.Button(
            buttons_frame,
            text="Crear Nodo",
            command=self.crear_nodo
        ).pack(side="left", padx=5)

        tk.Button(
            buttons_frame,
            text="Conectar Nodos",
            command=self.conectar_nodos
        ).pack(side="left", padx=5)

        tk.Button(
            buttons_frame,
            text="Eliminar Nodo",
            command=self.eliminar_nodo
        ).pack(side="left", padx=5)

        tk.Button(
            buttons_frame,
            text="Limpiar Todo",
            command=self.limpiar_todo
        ).pack(side="left", padx=5)

        # ---------------- RESULTADOS ----------------

        self.lbl_ruta = tk.Label(self.root, text="Ruta:")
        self.lbl_ruta.pack()

        self.lbl_costo = tk.Label(self.root, text="Costo:")
        self.lbl_costo.pack()

        # ---------------- PANEL ----------------

        panel_frame = tk.Frame(self.root)
        panel_frame.pack(fill="both", expand=True)

        self.panel = PanelGrafo(panel_frame)

    # --------------------------------------------------

    def iniciar(self):

        grafo = self.controlador.obtener_grafo()

        nodos = list(grafo.keys())

        self.cb_origen["values"] = nodos
        self.cb_destino["values"] = nodos

        # posiciones automáticas simples (en círculo)
        posiciones = self.generar_posiciones(nodos)

        self.panel.set_posiciones(posiciones)
        self.panel.dibujar(grafo)

        self.root.mainloop()

    # --------------------------------------------------

    def generar_posiciones(self, nodos):

        import math

        posiciones = {}
        n = len(nodos)
        radio = 200
        centro_x, centro_y = 350, 250

        for i, nodo in enumerate(nodos):

            angulo = 2 * math.pi * i / n

            x = centro_x + radio * math.cos(angulo)
            y = centro_y + radio * math.sin(angulo)

            posiciones[nodo] = (x, y)

        return posiciones

    # --------------------------------------------------

    def reiniciar(self):
        """
        Vuelve a mostrar el grafo original y limpia la selección.
        """

        grafo = self.controlador.obtener_grafo()

        self.origen.set("")
        self.destino.set("")
        self.algoritmo.set("DIJKSTRA")

        self.lbl_ruta.config(text="Ruta:")
        self.lbl_costo.config(text="Costo:")

        self.panel.dibujar(grafo)

    # --------------------------------------------------

    def buscar(self):

        origen = self.origen.get()
        destino = self.destino.get()
        algoritmo = self.algoritmo.get()

        if not origen:
            messagebox.showerror("Error", "Seleccione origen")
            return

        grafo = self.controlador.obtener_grafo()

        if algoritmo == "BFS":

            ruta = self.controlador.ejecutar_bfs(origen)

            self.lbl_ruta.config(text="Recorrido: " + " -> ".join(ruta))
            self.lbl_costo.config(text="Costo: No aplica")

        elif algoritmo == "DFS":

            ruta = self.controlador.ejecutar_dfs(origen)

            self.lbl_ruta.config(text="Recorrido: " + " -> ".join(ruta))
            self.lbl_costo.config(text="Costo: No aplica")

        elif algoritmo == "WARSHALL":

            if not destino:
                messagebox.showerror("Error", "Seleccione destino")
                return

            ruta, costo = self.controlador.ejecutar_warshall(origen, destino)

            if not ruta:
                self.lbl_ruta.config(text="Ruta: No hay ruta")
                self.lbl_costo.config(text="Costo: No disponible")
            else:
                self.lbl_ruta.config(text="Ruta más corta: " + " -> ".join(ruta))
                self.lbl_costo.config(text=f"Costo: {costo}")

            self.panel.dibujar(grafo)
            self.panel.resaltar_ruta(ruta)

        else:

            if not destino:
                messagebox.showerror("Error", "Seleccione destino")
                return

            ruta, costo = self.controlador.ejecutar_dijkstra(origen, destino)

            if not ruta:
                self.lbl_ruta.config(text="Ruta: No hay ruta")
                self.lbl_costo.config(text="Costo: No disponible")
            else:
                self.lbl_ruta.config(text="Ruta más corta: " + " -> ".join(ruta))
                self.lbl_costo.config(text=f"Costo: {costo}")

            self.panel.dibujar(grafo)
            self.panel.resaltar_ruta(ruta)

    # --------------------------------------------------

    def crear_nodo(self):
        """
        Crea un nuevo nodo en el grafo.
        """

        ventana = tk.Toplevel(self.root)
        ventana.title("Crear Nodo")
        ventana.geometry("300x150")

        tk.Label(ventana, text="Nombre del nodo:").pack(pady=5)
        entrada_nodo = tk.Entry(ventana, width=30)
        entrada_nodo.pack(pady=5)

        def agregar():
            nombre = entrada_nodo.get().strip()
            if not nombre:
                messagebox.showerror("Error", "Ingrese un nombre")
                return
            
            self.controlador.agregar_nodo(nombre)
            messagebox.showinfo("Éxito", f"Nodo '{nombre}' creado")
            
            grafo = self.controlador.obtener_grafo()
            nodos = list(grafo.keys())
            
            posiciones = self.generar_posiciones(nodos)
            self.panel.set_posiciones(posiciones)
            self.panel.dibujar(grafo)
            
            self.cb_origen["values"] = nodos
            self.cb_destino["values"] = nodos
            
            ventana.destroy()

        tk.Button(ventana, text="Crear", command=agregar).pack(pady=10)

    # --------------------------------------------------

    def conectar_nodos(self):
        """
        Conecta dos nodos existentes con un peso.
        """

        grafo = self.controlador.obtener_grafo()
        nodos = list(grafo.keys())

        if len(nodos) < 2:
            messagebox.showerror("Error", "Se necesitan al menos 2 nodos")
            return

        ventana = tk.Toplevel(self.root)
        ventana.title("Conectar Nodos")
        ventana.geometry("300x250")

        tk.Label(ventana, text="Nodo origen:").pack(pady=5)
        cb_origen = ttk.Combobox(ventana, values=nodos, width=25)
        cb_origen.pack(pady=5)

        tk.Label(ventana, text="Nodo destino:").pack(pady=5)
        cb_destino = ttk.Combobox(ventana, values=nodos, width=25)
        cb_destino.pack(pady=5)

        tk.Label(ventana, text="Peso:").pack(pady=5)
        entrada_peso = tk.Entry(ventana, width=30)
        entrada_peso.pack(pady=5)

        def conectar():
            origen = cb_origen.get().strip()
            destino = cb_destino.get().strip()
            peso_str = entrada_peso.get().strip()

            if not origen or not destino or not peso_str:
                messagebox.showerror("Error", "Complete todos los campos")
                return

            try:
                peso = int(peso_str)
            except ValueError:
                messagebox.showerror("Error", "El peso debe ser un número")
                return

            if origen == destino:
                messagebox.showerror("Error", "No puede conectar un nodo consigo mismo")
                return

            self.controlador.agregar_arista(origen, destino, peso)
            messagebox.showinfo("Éxito", f"Conexión creada: {origen} -> {destino} ({peso})")

            grafo = self.controlador.obtener_grafo()
            self.panel.dibujar(grafo)

            ventana.destroy()

        tk.Button(ventana, text="Conectar", command=conectar).pack(pady=10)

    # --------------------------------------------------

    def eliminar_nodo(self):
        """
        Elimina un nodo del grafo.
        """

        grafo = self.controlador.obtener_grafo()
        nodos = list(grafo.keys())

        if len(nodos) == 0:
            messagebox.showerror("Error", "No hay nodos para eliminar")
            return

        ventana = tk.Toplevel(self.root)
        ventana.title("Eliminar Nodo")
        ventana.geometry("300x150")

        tk.Label(ventana, text="Seleccione nodo a eliminar:").pack(pady=5)
        cb_nodo = ttk.Combobox(ventana, values=nodos, width=25)
        cb_nodo.pack(pady=5)

        def eliminar():
            nodo = cb_nodo.get().strip()
            if not nodo:
                messagebox.showerror("Error", "Seleccione un nodo")
                return

            self.controlador.eliminar_nodo(nodo)
            messagebox.showinfo("Éxito", f"Nodo '{nodo}' eliminado")

            grafo = self.controlador.obtener_grafo()
            nodos_actualizados = list(grafo.keys())

            posiciones = self.generar_posiciones(nodos_actualizados)
            self.panel.set_posiciones(posiciones)
            self.panel.dibujar(grafo)

            self.cb_origen["values"] = nodos_actualizados
            self.cb_destino["values"] = nodos_actualizados

            self.origen.set("")
            self.destino.set("")
            self.lbl_ruta.config(text="Ruta:")
            self.lbl_costo.config(text="Costo:")

            ventana.destroy()

        tk.Button(ventana, text="Eliminar", command=eliminar).pack(pady=10)

    # --------------------------------------------------

    def limpiar_todo(self):
        """
        Limpia todo el grafo.
        """

        if messagebox.askyesno("Confirmación", "¿Desea eliminar todo el grafo?"):
            self.controlador.limpiar_grafo()
            
            self.origen.set("")
            self.destino.set("")
            self.algoritmo.set("DIJKSTRA")
            self.lbl_ruta.config(text="Ruta:")
            self.lbl_costo.config(text="Costo:")

            self.cb_origen["values"] = []
            self.cb_destino["values"] = []

            self.panel.set_posiciones({})
            self.panel.limpiar()

            messagebox.showinfo("Éxito", "Grafo limpiado")
