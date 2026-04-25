from model.arbol_bst import ArbolBST
from model.contacto import Contacto


class NombreDuplicadoError(Exception):
    pass


class ContactoNoEncontradoError(Exception):
    pass


class ContactoService:
    def __init__(self):
        self._arbol = ArbolBST()
        self._id_a_nombre: dict[int, str] = {}
        self._next_id = 1

    def cargar_demostracion_si_vacio(self, datos: list[tuple[str, str, str]]) -> bool:
        if not self._arbol.esta_vacio():
            return False

        for nombre, telefono, correo in datos:
            self.crear(nombre, telefono, correo)
        return True

    def visualizar_arbol(self) -> str:
        return self._arbol.visualizar_arbol()

    def total_contactos(self) -> int:
        return self._arbol.contar_contactos()

    def listar_alfabetico(self) -> list[Contacto]:
        return self._arbol.inorden()

    def buscar_por_nombre(self, nombre: str) -> Contacto | None:
        return self._arbol.buscar(nombre)

    def buscar(self, query: str) -> list[Contacto]:
        q = (query or "").strip().lower()
        if not q:
            return self.listar_alfabetico()

        resultados: list[Contacto] = []
        for c in self._arbol.inorden():
            if q in (c.nombre or "").lower():
                resultados.append(c)
                continue
            if q in (c.telefono or "").lower():
                resultados.append(c)
                continue
            if q in (c.correo or "").lower():
                resultados.append(c)
                continue
        return resultados

    def obtener_por_id(self, contacto_id: int) -> Contacto | None:
        nombre = self._id_a_nombre.get(contacto_id)
        if not nombre:
            return None
        return self._arbol.buscar(nombre)

    def crear(self, nombre: str, telefono: str, correo: str) -> Contacto:
        contacto = Contacto(
            nombre.strip(),
            (telefono or "").strip(),
            (correo or "").strip(),
            contacto_id=self._next_id,
        )
        if not contacto.nombre:
            raise ValueError("El nombre no puede estar vacío.")

        ok = self._arbol.insertar(contacto)
        if not ok:
            raise NombreDuplicadoError(f"Ya existe un contacto con el nombre '{contacto.nombre}'.")

        self._id_a_nombre[self._next_id] = contacto.nombre
        self._next_id += 1
        return contacto

    def actualizar(self, contacto_id: int, telefono: str, correo: str) -> Contacto:
        contacto = self.obtener_por_id(contacto_id)
        if contacto is None:
            raise ContactoNoEncontradoError("Contacto no encontrado.")

        nuevo_telefono = (telefono or "").strip()
        nuevo_correo = (correo or "").strip()

        contacto.telefono = nuevo_telefono
        contacto.correo = nuevo_correo

        return contacto

    def eliminar(self, contacto_id: int) -> None:
        contacto = self.obtener_por_id(contacto_id)
        if contacto is None:
            raise ContactoNoEncontradoError("Contacto no encontrado.")

        ok_arbol = self._arbol.eliminar(contacto.nombre)
        self._id_a_nombre.pop(contacto_id, None)

        if not ok_arbol:
            raise ContactoNoEncontradoError("Contacto no encontrado.")
