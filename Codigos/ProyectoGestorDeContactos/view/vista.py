# =============================================================================
# VIEW - vista.py
# Responsabilidad: TODO lo que se muestra al usuario.
#
# La Vista NO conoce al arbol BST directamente.
# Solo recibe datos del Controlador y los muestra.
# Tambien recoge la entrada del usuario y la entrega al Controlador.
# =============================================================================


class Vista:
    """Interfaz de usuario en consola. Solo muestra y pide datos."""

    # =========================================================================
    # MENU PRINCIPAL
    # =========================================================================

    def mostrar_menu(self):
        """Muestra el menu principal y retorna la opcion elegida."""
        print()
        print("=" * 55)
        print("     GESTOR DE CONTACTOS ALFABETICO")
        print("=" * 55)
        print("  1. Insertar contacto")
        print("  2. Buscar contacto")
        print("  3. Editar contacto")
        print("  4. Eliminar contacto")
        print("  5. Listar en orden ALFABETICO (Inorden)")
        print("  6. Mostrar arbol visual")
        print("  7. Recorrido Preorden")
        print("  8. Recorrido Postorden")
        print("  0. Salir")
        print("=" * 55)
        return self._leer_entero("  Elige una opcion: ")

    # =========================================================================
    # FORMULARIOS DE ENTRADA
    # =========================================================================

    def pedir_datos_contacto(self):
        """Pide todos los datos para un nuevo contacto."""
        print()
        print("-- NUEVO CONTACTO " + "-" * 36)
        nombre   = input("  Nombre    : ").strip()
        telefono = input("  Telefono  : ").strip()
        correo   = input("  Correo    : ").strip()
        return nombre, telefono, correo

    def pedir_nombre(self, accion):
        """Pide el nombre para buscar, eliminar o editar."""
        return input(f"\n  Nombre a {accion}: ").strip()

    def pedir_datos_edicion(self, contacto_actual):
        """Pide datos para editar (puede dejarse en blanco para no cambiar)."""
        print()
        print("-- EDITAR CONTACTO " + "-" * 35)
        print(f"  Contacto actual: {contacto_actual}")
        print("  (Deja en blanco para no cambiar)")
        nuevo_telefono = input("  Nuevo telefono  : ").strip()
        nuevo_correo   = input("  Nuevo correo    : ").strip()
        return nuevo_telefono, nuevo_correo

    # =========================================================================
    # MOSTRAR RESULTADOS
    # =========================================================================

    def mostrar_contacto(self, contacto):
        """Muestra un contacto encontrado con formato detallado."""
        print()
        print("  Contacto encontrado:")
        print("  " + "-" * 45)
        print(f"  Nombre  : {contacto.nombre}")
        print(f"  Telefono: {contacto.telefono}")
        print(f"  Correo  : {contacto.correo}")
        print("  " + "-" * 45)

    def mostrar_lista(self, titulo, lista):
        """
        Muestra una lista de contactos con encabezado personalizado.
        - titulo : nombre del recorrido (Inorden, Preorden, Postorden)
        - lista  : lista de objetos Contacto
        """
        print()
        print(f"-- {titulo} " + "-" * max(1, 50 - len(titulo)))
        if not lista:
            print("  (no hay contactos)")
            return
        print(f"  {'#':<4} {'NOMBRE':<20} {'TELEFONO':<16} CORREO")
        print("  " + "-" * 60)
        for i, contacto in enumerate(lista, 1):
            print(f"  {i:<4} {contacto.nombre:<20} {contacto.telefono:<16} {contacto.correo}")
        print("  " + "-" * 60)
        print(f"  Total: {len(lista)} contacto(s)")

    def mostrar_arbol_visual(self, arbol_visual, total):
        """
        Muestra el arbol BST de forma grafica en consola.
        El arbol se dibuja rotado 90 grados (raiz a la izquierda).

        Derecha del arbol = arriba en pantalla
        Izquierda del arbol = abajo en pantalla
        """
        print()
        print("-- ARBOL BST VISUAL " + "-" * 34)
        print("   (Rotado 90 grados: raiz a la izquierda)")
        print("   Derecha = arriba | Izquierda = abajo")
        print("-" * 50)
        print(arbol_visual)
        print("-" * 50)
        print(f"  Total de nodos: {total}")

    # =========================================================================
    # MENSAJES DE ESTADO
    # =========================================================================

    def mostrar_exito(self, mensaje):
        print(f"\n  OK: {mensaje}")

    def mostrar_error(self, mensaje):
        print(f"\n  ERROR: {mensaje}")

    def mostrar_info(self, mensaje):
        print(f"\n  INFO: {mensaje}")

    def mostrar_bienvenida(self):
        print()
        print("=" * 55)
        print("  GESTOR DE CONTACTOS ALFABETICO - BST en Python")
        print("  Estructura de Datos II | Metodo MVC")
        print("=" * 55)
        print("  Los contactos se almacenan en un BST ordenado")
        print("  alfabeticamente por nombre.")
        print("=" * 55)

    def mostrar_despedida(self):
        print()
        print("  Hasta luego.")
        print("=" * 55)

    def pausar(self):
        input("\n  [Presiona ENTER para continuar...]")

    # =========================================================================
    # UTILIDADES INTERNAS
    # =========================================================================

    def _leer_entero(self, mensaje):
        """Lee un entero del teclado con manejo de errores."""
        try:
            return int(input(mensaje).strip())
        except ValueError:
            return -1   # Opcion invalida
