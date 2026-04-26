# Controlador - Lógica de aplicación
from model import DiccionarioBST
from view import Vista
class Controlador:
    """Gestiona interacción entre Vista y Modelo."""

    def __init__(self):
        self.diccionario = DiccionarioBST()
        self.vista = Vista()
        
    

    def ejecutar(self):
        """Ejecuta el programa principal."""
        while True:
            self.vista.menu()
            opcion = self.vista.obtener_entrada()
            if opcion == "1":
                self.insertar_palabra()
            elif opcion == "2":
                self.buscar_palabra()
            elif opcion == "3":
                self.eliminar_palabra()
            elif opcion == "4":
                self.vista.mostrar_resultado("¡Hasta luego!")
                break
            else:
                self.vista.mostrar_resultado("Opción no válida")

    def insertar_palabra(self):
        """Inserta nueva palabra en el diccionario."""
        palabra = input("Palabra (español): ").strip()
        traduccion = input("Traducción (inglés): ").strip()
        self.diccionario.insertar(palabra, traduccion)
        self.vista.mostrar_resultado(f"'{palabra}' insertado correctamente")

    def buscar_palabra(self):
        """Busca traducción de una palabra."""
        palabra = input("Palabra a buscar: ").strip()
        resultado = self.diccionario.buscar(palabra)
        if resultado:
            self.vista.mostrar_resultado(f"'{palabra}' = '{resultado}'")
        else:
            self.vista.mostrar_resultado("Palabra no encontrada")

    def eliminar_palabra(self):
        palabra = input("Palabra a eliminar: ").strip()
    
        # Verificar si existe
        resultado = self.diccionario.buscar(palabra)
    
        if resultado:
            self.diccionario.eliminar(palabra)
            self.vista.mostrar_resultado(f"'{palabra}' eliminado")
        else:
            self.vista.mostrar_resultado("Palabra no registrada")

