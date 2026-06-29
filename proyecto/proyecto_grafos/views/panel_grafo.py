"""
===========================================================
Archivo: panel_grafo.py

Descripción:
-------------
Este módulo se encarga EXCLUSIVAMENTE de dibujar el grafo.

Responsabilidades:
- Dibujar nodos
- Dibujar aristas
- Mostrar pesos
- Resaltar rutas (BFS/DFS/Dijkstra)
===========================================================
"""

import tkinter as tk


class PanelGrafo:

    def __init__(self, parent):

        self.canvas = tk.Canvas(
            parent,
            bg="white",
            width=700,
            height=500
        )

        self.canvas.pack(fill="both", expand=True)

        # posiciones fijas de nodos
        self.posiciones = {}

    # ------------------------------------------------------

    def set_posiciones(self, posiciones):
        """
        Guarda posiciones de los nodos.
        """
        self.posiciones = posiciones

    # ------------------------------------------------------

    def limpiar(self):
        """
        Limpia el canvas.
        """
        self.canvas.delete("all")

    # ------------------------------------------------------

    def dibujar(self, grafo):
        """
        Dibuja todo el grafo.
        """

        self.limpiar()

        # ARISTAS
        aristas_vistas = set()

        for origen in grafo:
            if origen not in self.posiciones:
                continue

            x1, y1 = self.posiciones[origen]

            for destino, peso in grafo[origen]:

                if destino not in self.posiciones:
                    continue

                x2, y2 = self.posiciones[destino]

                # línea
                self.canvas.create_line(
                    x1, y1, x2, y2,
                    fill="gray",
                    width=2,
                    arrow=tk.LAST
                )

                pareja = tuple(sorted((origen, destino)))
                if pareja not in aristas_vistas:
                    aristas_vistas.add(pareja)

                    # peso
                    px = (x1 + x2) / 2
                    py = (y1 + y2) / 2

                    dx = x2 - x1
                    dy = y2 - y1
                    longitud = (dx * dx + dy * dy) ** 0.5

                    if longitud > 0:
                        nx = -dy / longitud
                        ny = dx / longitud
                        offset = 16
                        px += nx * offset
                        py += ny * offset
                    else:
                        px += 10
                        py -= 10

                    rect_x1 = px - 14
                    rect_y1 = py - 9
                    rect_x2 = px + 14
                    rect_y2 = py + 9

                    self.canvas.create_rectangle(
                        rect_x1, rect_y1, rect_x2, rect_y2,
                        fill="white",
                        outline="black",
                        width=1
                    )

                    self.canvas.create_text(
                        px,
                        py,
                        text=str(peso),
                        fill="blue",
                        font=("Arial", 9, "bold"),
                        anchor="center",
                        tags="peso"
                    )

        # NODOS
        for nodo, (x, y) in self.posiciones.items():

            radio = 24
            self.canvas.create_oval(
                x - radio, y - radio,
                x + radio, y + radio,
                fill="lightblue",
                outline="black",
                width=1
            )

            self.canvas.create_text(
                x, y,
                text=nodo,
                font=("Arial", 11, "bold")
            )

    # ------------------------------------------------------

    def resaltar_ruta(self, ruta):
        """
        Resalta la ruta en rojo.
        """

        if not ruta:
            return

        for i in range(len(ruta) - 1):

            a = ruta[i]
            b = ruta[i + 1]

            if a not in self.posiciones or b not in self.posiciones:
                continue

            x1, y1 = self.posiciones[a]
            x2, y2 = self.posiciones[b]

            self.canvas.create_line(
                x1, y1, x2, y2,
                fill="red",
                width=4,
                arrow=tk.LAST
            )