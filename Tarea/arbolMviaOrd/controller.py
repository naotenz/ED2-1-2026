# controller.py

from model import ArbolMVias, AVL
from view import Vista


class Controlador:
    def __init__(self):
        self.arbol = ArbolMVias(4)
        self.avl = AVL()
        self.vista = Vista()

    def iniciar(self):
        while True:
            op = self.vista.menu()

            if op == "1":
                x = self.vista.pedir_valor()
                self.arbol.insertar(x)

            elif op == "2":
                self.vista.mostrar(self.arbol.inorder())

            elif op == "3":
                x = self.vista.pedir_valor()
                self.arbol.eliminar(x)

            elif op == "4":
                x = self.vista.pedir_valor()
                self.avl.insertar(x)

            elif op == "5":
                self.vista.mostrar(self.avl.inorder())

            elif op == "6":
                break