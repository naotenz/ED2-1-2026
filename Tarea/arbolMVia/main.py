import tkinter as tk
from view import ArbolMViasView
from controller import ArbolMViasController


def main():
    root = tk.Tk()

    view = ArbolMViasView(root)

    controller = ArbolMViasController(view)

    root.mainloop()


if __name__ == "__main__":
    main()