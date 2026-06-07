"""

Punto de entrada del programa.
"""

from controlador import Controlador


def main():

    sistema = Controlador()

    sistema.ejecutar()


if __name__ == "__main__":
    main()