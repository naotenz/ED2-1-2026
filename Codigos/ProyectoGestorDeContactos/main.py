# =============================================================================
# main.py - Punto de entrada del programa
#
# ARQUITECTURA MVC:
#   model/      --> Logica del arbol BST (contacto, nodo, arbol_bst)
#   view/       --> Interfaz de usuario (vista)
#   controller/ --> Coordinador entre Model y View (controlador)
#
# Solo crea el Controlador y llama a iniciar().
# =============================================================================

from controller.controlador import Controlador

if __name__ == "__main__":
    app = Controlador()
    app.iniciar()
