"""
CONTROLLER
Conecta VIEW con MODEL
"""

from model import ArbolMVias, Archivo


class Controlador:
    def __init__(self, vista):
        self.modelo = ArbolMVias()
        self.vista = vista

        self.vista.btn_agregar.config(command=self.agregar)
        self.vista.btn_buscar.config(command=self.buscar)
        self.vista.btn_eliminar.config(command=self.eliminar)
        self.vista.btn_mostrar.config(command=self.mostrar)

    def agregar(self):
        archivo = Archivo(
            int(self.vista.codigo.get()),
            self.vista.nombre.get(),
            self.vista.tipo.get(),
            self.vista.tamano.get()
        )
        self.modelo.insertar(archivo)
        self.vista.resultado.insert("end", "Archivo agregado\n")

    def buscar(self):
        codigo = int(self.vista.codigo.get())
        a = self.modelo.buscar(codigo)

        self.vista.resultado.delete("1.0", "end")
        if a:
            self.vista.resultado.insert("end", f"{a.codigo} - {a.nombre}\n")
        else:
            self.vista.resultado.insert("end", "No encontrado\n")

    def eliminar(self):
        codigo = int(self.vista.codigo.get())
        self.modelo.eliminar(codigo)
        self.vista.resultado.insert("end", "Eliminado\n")

    def mostrar(self):
        self.vista.resultado.delete("1.0", "end")
        for a in self.modelo.inorden():
            self.vista.resultado.insert("end", f"{a.codigo} - {a.nombre}\n")