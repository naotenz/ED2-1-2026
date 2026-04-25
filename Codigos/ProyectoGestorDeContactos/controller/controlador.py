# =============================================================================
# CONTROLLER - controlador.py
# Responsabilidad: COORDINAR la Vista y el Model.
#
# El Controlador:
#   - Recibe acciones del usuario (a traves de la Vista)
#   - Llama al Model (ArbolBST) para ejecutarlas
#   - Entrega los resultados a la Vista para mostrarlos
#
# El Controlador NO dibuja nada (eso es la Vista).
# El Controlador NO tiene logica del arbol (eso es el Model).
#
#  USUARIO
#     | (elige opcion)
#  VISTA  <-------------- CONTROLADOR --------------> MODEL
#  (muestra)              (coordina)                (arbol BST)
# =============================================================================

from model.arbol_bst import ArbolBST
from model.contacto  import Contacto
from view.vista      import Vista


class Controlador:
    """Coordinador entre la Vista y el Modelo (ArbolBST)."""

    def __init__(self):
        """Crea el arbol BST (Model) y la interfaz (View)."""
        self.arbol = ArbolBST()   # Model
        self.vista = Vista()       # View

    # =========================================================================
    # METODO PRINCIPAL: inicia la aplicacion y maneja el bucle del menu
    # =========================================================================

    def iniciar(self):
        """
        Arranca la aplicacion.
        Muestra el menu y despacha cada opcion al metodo correspondiente.
        """
        self.vista.mostrar_bienvenida()
        self._cargar_datos_demostracion()

        while True:
            opcion = self.vista.mostrar_menu()
            if opcion == 0:
                break
            self._procesar_opcion(opcion)

        self.vista.mostrar_despedida()

    # =========================================================================
    # DESPACHADOR DE OPCIONES
    # =========================================================================

    def _procesar_opcion(self, opcion):
        """Llama al metodo correspondiente segun la opcion elegida."""
        opciones = {
            1: self._insertar_contacto,
            2: self._buscar_contacto,
            3: self._editar_contacto,
            4: self._eliminar_contacto,
            5: self._listar_alfabetico,
            6: self._mostrar_arbol,
            7: self._mostrar_preorden,
            8: self._mostrar_postorden,
        }
        accion = opciones.get(opcion)
        if accion:
            accion()
        else:
            self.vista.mostrar_error("Opcion invalida. Elige entre 0 y 8.")

    # =========================================================================
    # 1. INSERTAR
    # =========================================================================

    def _insertar_contacto(self):
        """Pide datos al usuario, crea el Contacto y lo inserta en el BST."""
        # 1. Vista pide los datos
        nombre, telefono, correo = self.vista.pedir_datos_contacto()

        # 2. Validar que el nombre no este vacio
        if not nombre:
            self.vista.mostrar_error("El nombre no puede estar vacio.")
            return

        # 3. Model: crear contacto e insertar en BST
        nuevo = Contacto(nombre, telefono, correo)
        insertado = self.arbol.insertar(nuevo)

        # 4. Vista muestra resultado
        if insertado:
            self.vista.mostrar_exito(f"Contacto '{nombre}' insertado correctamente.")
            self.vista.mostrar_info(f"Total de contactos: {self.arbol.contar_contactos()}")
        else:
            self.vista.mostrar_error(f"Ya existe un contacto con el nombre '{nombre}'.")
        self.vista.pausar()

    # =========================================================================
    # 2. BUSCAR
    # =========================================================================

    def _buscar_contacto(self):
        """Busca un contacto por nombre en el BST."""
        nombre = self.vista.pedir_nombre("buscar")

        # Model: buscar en el BST
        encontrado = self.arbol.buscar(nombre)

        # Vista muestra resultado
        if encontrado:
            self.vista.mostrar_contacto(encontrado)
        else:
            self.vista.mostrar_error(f"No se encontro el contacto '{nombre}'.")
        self.vista.pausar()

    # =========================================================================
    # 3. EDITAR
    # =========================================================================

    def _editar_contacto(self):
        """
        Edita telefono y/o correo de un contacto existente.
        El NOMBRE no se puede cambiar (es la clave del BST).
        """
        nombre = self.vista.pedir_nombre("editar")

        # Verificar que existe
        actual = self.arbol.buscar(nombre)
        if actual is None:
            self.vista.mostrar_error(f"No se encontro el contacto '{nombre}'.")
            self.vista.pausar()
            return

        # Vista pide nuevos datos
        nuevo_telefono, nuevo_correo = self.vista.pedir_datos_edicion(actual)

        # Model: actualizar en el BST
        editado = self.arbol.editar(nombre, nuevo_telefono, nuevo_correo)

        if editado:
            self.vista.mostrar_exito(f"Contacto '{nombre}' actualizado correctamente.")
            self.vista.mostrar_contacto(self.arbol.buscar(nombre))
        else:
            self.vista.mostrar_error("No se pudo editar el contacto.")
        self.vista.pausar()

    # =========================================================================
    # 4. ELIMINAR
    # =========================================================================

    def _eliminar_contacto(self):
        """Elimina un contacto del BST (maneja los 3 casos de eliminacion)."""
        nombre = self.vista.pedir_nombre("eliminar")

        # Model: eliminar del BST
        eliminado = self.arbol.eliminar(nombre)

        if eliminado:
            self.vista.mostrar_exito(f"Contacto '{nombre}' eliminado correctamente.")
            self.vista.mostrar_info(f"Total de contactos: {self.arbol.contar_contactos()}")
        else:
            self.vista.mostrar_error(f"No se encontro el contacto '{nombre}'.")
        self.vista.pausar()

    # =========================================================================
    # 5. LISTAR ALFABETICAMENTE (INORDEN)
    # =========================================================================

    def _listar_alfabetico(self):
        """
        Muestra todos los contactos en orden alfabetico.
        Usa el recorrido INORDEN del BST (Izq --> Raiz --> Der).
        """
        lista = self.arbol.inorden()
        self.vista.mostrar_lista("CONTACTOS EN ORDEN ALFABETICO (Inorden)", lista)
        self.vista.pausar()

    # =========================================================================
    # 6. ARBOL VISUAL
    # =========================================================================

    def _mostrar_arbol(self):
        """Muestra el arbol BST de forma grafica en consola."""
        visual = self.arbol.visualizar_arbol()
        self.vista.mostrar_arbol_visual(visual, self.arbol.contar_contactos())
        self.vista.pausar()

    # =========================================================================
    # 7. PREORDEN
    # =========================================================================

    def _mostrar_preorden(self):
        """Muestra recorrido PREORDEN: Raiz --> Izquierda --> Derecha."""
        lista = self.arbol.preorden()
        self.vista.mostrar_lista("RECORRIDO PREORDEN (Raiz --> Izq --> Der)", lista)
        self.vista.pausar()

    # =========================================================================
    # 8. POSTORDEN
    # =========================================================================

    def _mostrar_postorden(self):
        """Muestra recorrido POSTORDEN: Izquierda --> Derecha --> Raiz."""
        lista = self.arbol.postorden()
        self.vista.mostrar_lista("RECORRIDO POSTORDEN (Izq --> Der --> Raiz)", lista)
        self.vista.pausar()

    # =========================================================================
    # DATOS DE DEMOSTRACION
    # =========================================================================

    def _cargar_datos_demostracion(self):
        # Carga 6 contactos de ejemplo para que el arbol no este vacio al inicio.
        # Arbol resultante:
        #           [Carlos]
        #          /         |
        #       [Ana]       [Luis]
        #          |        /    |
        #       [Bruno] [Diana] [Mario]
        # Inorden: Ana, Bruno, Carlos, Diana, Luis, Mario
        datos = [
            ("Carlos", "70011001", "carlos@mail.com"),
            ("Ana",    "70022002", "ana@mail.com"),
            ("Luis",   "70033003", "luis@mail.com"),
            ("Bruno",  "70044004", "bruno@mail.com"),
            ("Diana",  "70055005", "diana@mail.com"),
            ("Mario",  "70066006", "mario@mail.com"),
        ]
        for nombre, telefono, correo in datos:
            self.arbol.insertar(Contacto(nombre, telefono, correo))

        self.vista.mostrar_info("Se cargaron 6 contactos de demostracion.")
