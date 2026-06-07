"""

Conecta la Vista con el Modelo.
"""

from archivo import Archivo
from arbol_binario import ArbolBinario
from vista import Vista


class Controlador:

    def __init__(self):

        self.vista = Vista()
        self.arbol = ArbolBinario()

    def ejecutar(self):

        while True:

            opcion = self.vista.mostrar_menu()

            if opcion == "1":

                nombre, tamano, tipo = self.vista.pedir_datos_archivo()

                archivo = Archivo(nombre, tamano, tipo)

                self.arbol.insertar(archivo)

                self.vista.mostrar_mensaje(
                    "Archivo registrado correctamente."
                )

            elif opcion == "2":

                nombre = self.vista.pedir_nombre()

                resultado = self.arbol.buscar(nombre)

                if resultado:
                    self.vista.mostrar_mensaje(resultado)
                else:
                    self.vista.mostrar_mensaje(
                        "Archivo no encontrado."
                    )

            elif opcion == "3":

                print("\n===== ARCHIVOS REGISTRADOS =====")

                self.arbol.mostrar_inorden(
                    self.arbol.raiz
                )

            elif opcion == "4":

                print("Saliendo del sistema...")
                break

            else:

                print("Opción inválida.")