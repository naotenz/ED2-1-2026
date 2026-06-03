"""
MAIN
Ejecuta la aplicación
"""

import tkinter as tk
from view import Vista
from controller import Controlador


root = tk.Tk()

vista = Vista(root)
controlador = Controlador(vista)

root.mainloop()