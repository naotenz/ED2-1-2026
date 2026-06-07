"""

Maneja la interacción con el usuario.
"""

class Vista:

    def mostrar_menu(self):

        print("\n===== GESTOR DE ARCHIVOS =====")
        print("1. Registrar archivo")
        print("2. Buscar archivo")
        print("3. Mostrar archivos")
        print("4. Salir")

        return input("Seleccione una opción: ")

    def pedir_datos_archivo(self):

        nombre = input("Nombre del archivo: ")
        tamano = int(input("Tamaño (KB): "))
        tipo = input("Tipo de archivo: ")

        return nombre, tamano, tipo

    def pedir_nombre(self):

        return input("Ingrese el nombre del archivo: ")

    def mostrar_mensaje(self, mensaje):

        print(mensaje)