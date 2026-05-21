# view.py

class Vista:
    def menu(self):
        print("\n--- MENU ---")
        print("1. Insertar en árbol M-vías")
        print("2. Mostrar ordenado")
        print("3. Eliminar")
        print("4. Insertar en AVL")
        print("5. Mostrar AVL")
        print("6. Salir")
        return input("Seleccione: ")

    def pedir_valor(self):
        return int(input("Ingrese valor: "))

    def mostrar(self, datos):
        print("Resultado:", datos)