# =============================================================================
# MODEL - nodo.py
# Clase que representa un nodo del Arbol Binario de Busqueda (BST).
#
# Estructura de cada nodo:
#
#        [ contacto ]
#        /           \
#   izquierda      derecha
#  (nombre menor) (nombre mayor)
# =============================================================================

class Nodo:
    """Nodo del arbol BST que almacena un objeto Contacto."""

    def __init__(self, contacto):
        """
        Crea un nodo hoja (sin hijos) con el contacto dado.
        - contacto  : objeto de la clase Contacto
        - izquierda : hijo izquierdo (nombre alfabeticamente menor)
        - derecha   : hijo derecho   (nombre alfabeticamente mayor)
        """
        self.contacto   = contacto
        self.izquierda  = None   # Nodo recien creado no tiene hijos
        self.derecha    = None
