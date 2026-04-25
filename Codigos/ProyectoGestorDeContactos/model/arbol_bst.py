# =============================================================================
# MODEL - arbol_bst.py
# Arbol Binario de Busqueda (BST) que almacena contactos ordenados
# ALFABETICAMENTE por nombre.
#
# REGLA DEL BST:
#   nombre < nodo.nombre  --> va a la IZQUIERDA
#   nombre > nodo.nombre  --> va a la DERECHA
#   nombre == nodo.nombre --> ya existe (no se duplica)
#
# La clave de comparacion es: nombre.lower()
# Todas las operaciones usan RECURSIVIDAD.


from model.nodo import Nodo
from model.contacto import Contacto


class ArbolBST:
    """Arbol Binario de Busqueda para gestionar contactos alfabeticamente."""

    def __init__(self):
        """Crea un arbol vacio."""
        self.raiz = None

    # 1. INSERTAR CONTACTO
   
    def insertar(self, contacto):
        """
        Inserta un contacto en el arbol (metodo publico).
        Retorna True si se inserto, False si el nombre ya existe.
        """
        if self._buscar_nodo(self.raiz, contacto.nombre) is not None:
            return False   # Nombre duplicado, no se inserta
        self.raiz = self._insertar_rec(self.raiz, contacto)
        return True

    def _insertar_rec(self, nodo, contacto):
        """
        RECURSIVO: Recorre el arbol para encontrar la posicion correcta.

        Caso base   : nodo es None --> crear nuevo nodo aqui
        Caso recursivo: comparar nombre y bajar izquierda o derecha
        """
        # -- CASO BASE: posicion vacia encontrada -----------------------------
        if nodo is None:
            return Nodo(contacto)   # aqui va el nuevo nodo

        # -- COMPARACION ALFABETICA (ignora mayusculas/minusculas) ------------
        if contacto.nombre.lower() < nodo.contacto.nombre.lower():
            # Nombre MENOR --> bajar por la IZQUIERDA
            nodo.izquierda = self._insertar_rec(nodo.izquierda, contacto)

        elif contacto.nombre.lower() > nodo.contacto.nombre.lower():
            # Nombre MAYOR --> bajar por la DERECHA
            nodo.derecha = self._insertar_rec(nodo.derecha, contacto)

        # Si son iguales, no se hace nada (duplicado ya validado arriba)
        return nodo

    # 2. BUSCAR CONTACTO
    
    def buscar(self, nombre):
        """
        Busca un contacto por nombre (metodo publico).
        Retorna el objeto Contacto si existe, o None si no.
        """
        nodo = self._buscar_nodo(self.raiz, nombre)
        return nodo.contacto if nodo is not None else None

    def _buscar_nodo(self, nodo, nombre):
        """
        RECURSIVO: Busca el nodo con el nombre dado.

        Caso base 1: nodo es None        --> no encontrado
        Caso base 2: nombre coincide     --> encontrado
        Caso recursivo: bajar izquierda o derecha segun comparacion
        """
        # -- CASO BASE 1: llegamos a una hoja vacia ---------------------------
        if nodo is None:
            return None

        # -- COMPARACION -----------------------------------------------------
        comparacion = nombre.lower()

        if comparacion == nodo.contacto.nombre.lower():
            # -- CASO BASE 2: encontrado -------------------------------------
            return nodo

        elif comparacion < nodo.contacto.nombre.lower():
            # Buscar a la IZQUIERDA
            return self._buscar_nodo(nodo.izquierda, nombre)

        else:
            # Buscar a la DERECHA
            return self._buscar_nodo(nodo.derecha, nombre)

    # 3. ELIMINAR CONTACTO
    
    def eliminar(self, nombre):
        """
        Elimina un contacto por nombre (metodo publico).
        Retorna True si fue eliminado, False si no existia.
        """
        if self._buscar_nodo(self.raiz, nombre) is None:
            return False
        self.raiz = self._eliminar_rec(self.raiz, nombre)
        return True

    def _eliminar_rec(self, nodo, nombre):
        """
        RECURSIVO: Elimina el nodo con el nombre dado.

        Maneja los 3 CASOS DE ELIMINACION en BST:
          CASO 1: Nodo hoja (sin hijos)   --> simplemente eliminar
          CASO 2: Nodo con UN hijo        --> reemplazar por ese hijo
          CASO 3: Nodo con DOS hijos      --> reemplazar con sucesor inorden
        """
        if nodo is None:
            return None

        if nombre.lower() < nodo.contacto.nombre.lower():
            # El nodo a eliminar esta en la IZQUIERDA
            nodo.izquierda = self._eliminar_rec(nodo.izquierda, nombre)

        elif nombre.lower() > nodo.contacto.nombre.lower():
            # El nodo a eliminar esta en la DERECHA
            nodo.derecha = self._eliminar_rec(nodo.derecha, nombre)

        else:
            # -- ENCONTRADO: aplicar los 3 casos ------------------------------

            # CASO 1 y 2a: Sin hijo izquierdo
            if nodo.izquierda is None:
                return nodo.derecha

            # CASO 2b: Sin hijo derecho
            if nodo.derecha is None:
                return nodo.izquierda

            # CASO 3: Tiene DOS hijos
            # --> Buscar el SUCESOR INORDEN (minimo del subarbol derecho)
            sucesor = self._minimo_nodo(nodo.derecha)
            # --> Reemplazar el dato del nodo actual con el sucesor
            nodo.contacto = sucesor.contacto
            # --> Eliminar el sucesor del subarbol derecho
            nodo.derecha = self._eliminar_rec(nodo.derecha, sucesor.contacto.nombre)

        return nodo

    def _minimo_nodo(self, nodo):
        """
        Retorna el nodo con el nombre minimo (mas a la izquierda).
        Usado en eliminacion con 2 hijos para encontrar el sucesor.
        """
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo

    # 4. EDITAR CONTACTO
    
    def editar(self, nombre, nuevo_telefono, nuevo_correo):
        """
        Edita telefono y/o correo de un contacto existente.
        El nombre NO se puede editar (es la clave del BST).
        Retorna True si se edito, False si no encontro el contacto.
        """
        nodo = self._buscar_nodo(self.raiz, nombre)
        if nodo is None:
            return False

        # Solo actualiza si el nuevo valor no esta vacio
        if nuevo_telefono.strip():
            nodo.contacto.telefono = nuevo_telefono
        if nuevo_correo.strip():
            nodo.contacto.correo = nuevo_correo
        return True

    # 5. RECORRIDOS (todos recursivos)
    
    def inorden(self):
        """
        INORDEN: Izquierda --> Raiz --> Derecha
        Resultado: lista en ORDEN ALFABETICO
        """
        lista = []
        self._inorden_rec(self.raiz, lista)
        return lista

    def _inorden_rec(self, nodo, lista):
        """RECURSIVO del recorrido inorden."""
        if nodo is None:
            return                               # CASO BASE
        self._inorden_rec(nodo.izquierda, lista) # 1. Recorrer izquierda
        lista.append(nodo.contacto)              # 2. Visitar raiz
        self._inorden_rec(nodo.derecha, lista)   # 3. Recorrer derecha

    def preorden(self):
        """
        PREORDEN: Raiz --> Izquierda --> Derecha
        Util para copiar o guardar el arbol (preserva estructura).
        """
        lista = []
        self._preorden_rec(self.raiz, lista)
        return lista

    def _preorden_rec(self, nodo, lista):
        """RECURSIVO del recorrido preorden."""
        if nodo is None:
            return                                # CASO BASE
        lista.append(nodo.contacto)              # 1. Visitar raiz
        self._preorden_rec(nodo.izquierda, lista) # 2. Recorrer izquierda
        self._preorden_rec(nodo.derecha, lista)   # 3. Recorrer derecha

    def postorden(self):
        """
        POSTORDEN: Izquierda --> Derecha --> Raiz
        Util para eliminar el arbol completo.
        """
        lista = []
        self._postorden_rec(self.raiz, lista)
        return lista

    def _postorden_rec(self, nodo, lista):
        """RECURSIVO del recorrido postorden."""
        if nodo is None:
            return                                # CASO BASE
        self._postorden_rec(nodo.izquierda, lista) # 1. Recorrer izquierda
        self._postorden_rec(nodo.derecha, lista)   # 2. Recorrer derecha
        lista.append(nodo.contacto)               # 3. Visitar raiz

    # 6. VISUALIZACION GRAFICA DEL ARBOL (en consola)
    
    def visualizar_arbol(self):
        """
        Genera una representacion visual del arbol en consola.
        El arbol se dibuja rotado 90 grados (raiz al centro-izquierda).

        Ejemplo:
            |   +---[Mario]
            +---[Luis]
            |   +---[Diana]
        ---[Carlos]
            |   +---[Bruno]
            +---[Ana]
        """
        if self.raiz is None:
            return "  (arbol vacio)"
        lineas = []
        self._visualizar_rec(self.raiz, lineas, "", "")
        return "\n".join(lineas)

    def _visualizar_rec(self, nodo, lineas, prefijo, conector):
        """
        RECURSIVO: Dibuja el arbol rotado 90 grados.
        Subarbol derecho aparece arriba, izquierdo abajo.
        """
        if nodo is None:
            return
        # Primero el subarbol DERECHO (aparece arriba en consola)
        self._visualizar_rec(nodo.derecha,    lineas, prefijo + "|   ", "+---")
        # Luego el nodo actual
        lineas.append(prefijo + conector + "[" + nodo.contacto.nombre + "]")
        # Finalmente el subarbol IZQUIERDO (aparece abajo en consola)
        self._visualizar_rec(nodo.izquierda,  lineas, prefijo + "|   ", "+---")

    # 7. UTILIDADES
    
    def esta_vacio(self):
        """Retorna True si el arbol esta vacio."""
        return self.raiz is None

    def contar_contactos(self):
        """Cuenta el total de contactos en el arbol."""
        return self._contar_rec(self.raiz)

    def _contar_rec(self, nodo):
        """RECURSIVO: cuenta nodos."""
        if nodo is None:
            return 0
        return 1 + self._contar_rec(nodo.izquierda) + self._contar_rec(nodo.derecha)
