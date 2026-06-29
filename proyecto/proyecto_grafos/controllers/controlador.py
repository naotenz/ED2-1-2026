from models.grafo import Grafo
from models.bfs import BFS
from models.dfs import DFS
from models.dijkstra import Dijkstra
from models.warshall import Warshall
from utils.lector_json import LectorJSON
from views.ventana import Ventana


class Controlador:
    
    def __init__(self):

        self.grafo = Grafo()

        self.bfs = BFS()
        self.dfs = DFS()
        self.dijkstra = Dijkstra()
        self.warshall = Warshall()
        self.cargar_datos()

        self.vista = Ventana(self)

    # ------------------------------------------

    def cargar_datos(self):

        lector = LectorJSON()

        data = lector.cargar("data/mapa.json")

        for origen in data:
            self.grafo.agregar_nodo(origen)

        for origen, vecinos in data.items():
            for destino, peso in vecinos:
                self.grafo.agregar_arista(origen, destino, peso)

                if origen != destino:
                    self.grafo.agregar_arista(destino, origen, peso)

    # ------------------------------------------

    def iniciar(self):
        self.vista.iniciar()

    # ------------------------------------------

    def obtener_grafo(self):
        return self.grafo.obtener_grafo()

    # ------------------------------------------

    def ejecutar_bfs(self, origen):
        return self.bfs.recorrer(self.grafo.obtener_grafo(), origen)

    def ejecutar_dfs(self, origen):
        return self.dfs.recorrer(self.grafo.obtener_grafo(), origen)

    def ejecutar_dijkstra(self, origen, destino):
        return self.dijkstra.calcular(self.grafo.obtener_grafo(), origen, destino)

    def ejecutar_warshall(self, origen, destino):
        return self.warshall.calcular(self.grafo.obtener_grafo(), origen, destino)

    # ------------------------------------------

    def agregar_nodo(self, nombre):
        """
        Agrega un nuevo nodo al grafo.
        """
        self.grafo.agregar_nodo(nombre)

    # ------------------------------------------

    def agregar_arista(self, origen, destino, peso):
        """
        Agrega una nueva arista entre dos nodos.
        """
        self.grafo.agregar_arista(origen, destino, peso)

    # ------------------------------------------

    def eliminar_nodo(self, nombre):
        """
        Elimina un nodo del grafo.
        """
        self.grafo.eliminar_nodo(nombre)

    # ------------------------------------------

    def limpiar_grafo(self):
        """
        Limpia todo el grafo.
        """
        self.grafo.limpiar_grafo()
