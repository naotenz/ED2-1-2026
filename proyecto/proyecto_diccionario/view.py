#Vista - Interfaz de usuario
class Vista:
    """Interface para interactuar con el diccionario."""
    @staticmethod
    def menu():
        """Muestra el menú de opciones disponibles."""
        print("\n=== Diccionario Bilingüe BST ===")
        print("1. Insertar palabra")
        print("2. Buscar traducción")
        print("3. Eliminar palabra")
        print("4. Salir")

    @staticmethod
    def obtener_entrada():
        """Captura entrada del usuario."""
        return input("Seleccione opción: ")

    @staticmethod
    def mostrar_resultado(mensaje):
        """Muestra resultado de operación."""
        print(f"→ {mensaje}")

