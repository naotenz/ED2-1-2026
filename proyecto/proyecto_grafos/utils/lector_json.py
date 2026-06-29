"""
===========================================================
Archivo: lector_json.py

Descripción:
-------------
Este módulo se encarga de cargar el grafo desde un archivo JSON.

Convierte el archivo mapa.json en un objeto Grafo.
===========================================================
"""

import json
import os


class LectorJSON:

    def cargar(self, ruta_archivo):
        """
        Carga el archivo JSON y lo convierte en diccionario.

        Parámetros
        ----------
        ruta_archivo : str

        Retorna
        -------
        dict
        """

        base_dir = os.path.dirname(os.path.abspath(__file__))

        posibles_rutas = [
            ruta_archivo,
            os.path.join(base_dir, ruta_archivo),
            os.path.join(base_dir, os.pardir, ruta_archivo),
            os.path.join(os.getcwd(), ruta_archivo)
        ]

        ruta_completa = None
        for ruta in posibles_rutas:
            ruta = os.path.normpath(ruta)
            if os.path.exists(ruta):
                ruta_completa = ruta
                break

        if ruta_completa is None:
            raise FileNotFoundError(
                f"No se encontró el archivo JSON en ninguna ruta válida: {posibles_rutas}"
            )

        try:
            with open(ruta_completa, "r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError as error:
            raise ValueError(
                f"Error al parsear JSON en {ruta_completa}: {error}"
            )

        return data