import tkinter as tk


class ArbolMViasView:
    """
    Vista del sistema MVC para el árbol m-vías.

    Se encarga de:
    - Construcción de la interfaz gráfica (Tkinter)
    - Captura de datos del usuario
    - Visualización del árbol en canvas
    """

    def __init__(self, root):
        """
        Inicializa la ventana principal.

        Args:
            root: ventana principal de Tkinter
        """
        self.root = root
        self.root.title("Árbol m-vías")
        self.root.geometry("1350x850")
        self.root.configure(bg="#f0f0f0")

        self.crear_interfaz()

    def crear_interfaz(self):
        """
        Crea todos los componentes de la interfaz gráfica:
        - Entradas de datos
        - Botones de control
        - Canvas para dibujar el árbol
        """

        # Título principal
        tk.Label(
            self.root,
            text="🌳 Árbol m-vías",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0"
        ).pack(pady=10)

        # Panel superior de controles
        top = tk.Frame(self.root, bg="#f0f0f0")
        top.pack(pady=10)

        # Entrada del orden del árbol
        tk.Label(top, text="Orden (m):").pack(side=tk.LEFT)

        self.entry_m = tk.Entry(top, width=8)

        self.entry_m.insert(0, "3")

        self.entry_m.pack(side=tk.LEFT, padx=5)

        # Botón para definir el orden
        self.btn_definir = tk.Button(
            top,
            text="Definir Orden",
            bg="#4CAF50",
            fg="white"
        )
        self.btn_definir.pack(side=tk.LEFT, padx=10)

        # Entrada de valor a insertar/buscar/eliminar
        tk.Label(top, text="Valor:").pack(side=tk.LEFT)

        self.entry_valor = tk.Entry(top, width=10)
        self.entry_valor.pack(side=tk.LEFT, padx=5)

        # Botón insertar
        self.btn_insertar = tk.Button(
            top,
            text="Insertar",
            bg="#2196F3",
            fg="white",
            state="disabled"
        )
        self.btn_insertar.pack(side=tk.LEFT, padx=5)

        # Botón eliminar
        self.btn_eliminar = tk.Button(
            top,
            text="Eliminar",
            bg="#f44336",
            fg="white"
        )
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)

        # Botón buscar
        self.btn_buscar = tk.Button(
            top,
            text="Buscar",
            bg="#FF9800",
            fg="white"
        )
        self.btn_buscar.pack(side=tk.LEFT, padx=5)

        # Recorridos
        self.btn_inorden = tk.Button(
            top,
            text="Inorden",
            bg="#9C27B0",
            fg="white"
        )
        self.btn_inorden.pack(side=tk.LEFT, padx=5)

        self.btn_preorden = tk.Button(
            top,
            text="Preorden",
            bg="#9C27B0",
            fg="white"
        )
        self.btn_preorden.pack(side=tk.LEFT, padx=5)

        self.btn_postorden = tk.Button(
            top,
            text="Postorden",
            bg="#9C27B0",
            fg="white"
        )
        self.btn_postorden.pack(side=tk.LEFT, padx=5)

        # Canvas donde se dibuja el árbol
        self.canvas = tk.Canvas(
            self.root,
            bg="white",
            height=600
        )
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    # ---------------- DIBUJO DEL ÁRBOL ----------------
    def dibujar_arbol(self, raiz):
        """
        Dibuja el árbol completo en el canvas.

        Args:
            raiz: nodo raíz del árbol
        """
        self.canvas.delete("all")

        if raiz is None:
            self.canvas.create_text(
                650,
                300,
                text="Árbol vacío",
                font=("Arial", 16),
                fill="gray"
            )
            return

        self._dibujar_nodo(raiz, 650, 60, 1200)

    def _dibujar_nodo(self, nodo, x, y, ancho):
        """
        Dibuja recursivamente cada nodo del árbol.

        Args:
            nodo: nodo actual
            x, y: posición en canvas
            ancho: espacio horizontal disponible
        """
        if nodo is None:
            return

        # convierte claves del nodo en texto
        texto = " | ".join(map(str, nodo.claves))

        # tamaño dinámico del nodo
        w = max(120, len(texto) * 10)

        # dibuja rectángulo del nodo
        self.canvas.create_rectangle(
            x - w//2,
            y,
            x + w//2,
            y + 60,
            fill="#bbdefb",
            outline="#1565c0",
            width=3
        )

        # dibuja texto del nodo
        self.canvas.create_text(
            x,
            y + 30,
            text=texto,
            font=("Arial", 12, "bold")
        )

        # dibuja hijos si existen
        if nodo.hijos:
            spacing = ancho / len(nodo.hijos)

            for i, hijo in enumerate(nodo.hijos):
                hx = x - ancho/2 + spacing/2 + i*spacing

                # línea hacia hijo
                self.canvas.create_line(
                    x,
                    y + 60,
                    hx,
                    y + 120,
                    width=2,
                    arrow=tk.LAST
                )

                # llamada recursiva
                self._dibujar_nodo(
                    hijo,
                    hx,
                    y + 140,
                    ancho/2
                )