"""
===========================================================
Proyecto: Sistema de Rutas para Delivery Urbano
Autor: (Tu nombre)
Materia: Grafos
Lenguaje: Python
Arquitectura: MVC
===========================================================

Archivo: main.py

Descripción:
------------
Este es el punto de entrada del programa.

Su única responsabilidad es crear el controlador e iniciar
la aplicación.

No contiene lógica de negocio ni algoritmos.
"""

from controllers.controlador import Controlador


def main():
    """
    Función principal del programa.

    Crea una instancia del controlador e inicia la aplicación.
    """
    controlador = Controlador()
    controlador.iniciar()


if __name__ == "__main__":
    main()