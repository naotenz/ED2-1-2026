# =============================================================================
# MODEL - contacto.py
# Clase que representa un contacto con sus datos personales.
# Esta clase es el "dato" que cada nodo del arbol BST almacena.
# =============================================================================

class Contacto:
    """Representa un contacto con nombre, telefono y correo."""

    def __init__(self, nombre, telefono, correo, contacto_id=None):
        """
        Crea un nuevo contacto.
        - nombre   : clave de ordenamiento en el BST (alfabetico)
        - telefono : numero de telefono
        - correo   : correo electronico
        """
        self.id = contacto_id
        self.nombre   = nombre
        self.telefono = telefono
        self.correo   = correo

    def __str__(self):
        """Representacion legible del contacto."""
        return f"{self.nombre:<20} | Tel: {self.telefono:<15} | Correo: {self.correo}"
