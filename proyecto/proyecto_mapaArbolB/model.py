class Nodo:
    def __init__(self, valor):
        self.valor = valor          # aquí guarda el valor del nodo
        self.izquierda = None       # aquí referencia al hijo izquierdo
        self.derecha = None         # aquí referencia al hijo derecho

class ArbolBinario:
    def __init__(self):
        self.raiz = None            # aquí inicializa la raíz vacía

    def insertar(self, valor):
        # aquí llama a la función recursiva para insertar
        self.raiz = self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        cmp = self._comparar(valor, nodo.valor)
        if cmp < 0:                 
            nodo.izquierda = self._insertar_rec(nodo.izquierda, valor)
        elif cmp > 0:               
            nodo.derecha = self._insertar_rec(nodo.derecha, valor)
        # si cmp == 0 → duplicado, no hace nada (se maneja antes de llamar a insertar)
        return nodo

    # ── NUEVO: busca un valor y retorna su info si existe ──────────────────────
    def buscar(self, valor):
        """
        Retorna un dict con posición y altura si el valor ya existe,
        o None si no existe.
        Posición: 'raíz' | 'izquierda' | 'derecha'
        Altura: nivel del nodo (raíz = 0)
        """
        return self._buscar_rec(self.raiz, valor, padre=None, lado=None, altura=0)

    def _buscar_rec(self, nodo, valor, padre, lado, altura):
        if nodo is None:
            return None                             # no existe
        cmp = self._comparar(valor, nodo.valor)
        if cmp == 0:                                # encontrado
            if padre is None:
                posicion = "raíz"
            else:
                posicion = f"hijo {lado} de '{padre.valor}'"
            return {
                "existe": True,
                "valor": nodo.valor,
                "posicion": posicion,
                "altura": altura
            }
        elif cmp < 0:
            return self._buscar_rec(nodo.izquierda, valor, padre=nodo, lado="izquierdo", altura=altura + 1)
        else:
            return self._buscar_rec(nodo.derecha,   valor, padre=nodo, lado="derecho",  altura=altura + 1)
    # ──────────────────────────────────────────────────────────────────────────

    def inorden(self, nodo, resultado):
        if nodo is not None:                        
            self.inorden(nodo.izquierda, resultado) 
            resultado.append(nodo.valor)            
            self.inorden(nodo.derecha, resultado)   

    def preorden(self, nodo, resultado):
        if nodo is not None:                        
            resultado.append(nodo.valor)            
            self.preorden(nodo.izquierda, resultado)
            self.preorden(nodo.derecha, resultado)  

    def postorden(self, nodo, resultado):
        if nodo is not None:                        
            self.postorden(nodo.izquierda, resultado)
            self.postorden(nodo.derecha, resultado) 
            resultado.append(nodo.valor)            

    def obtener_estructura(self, nodo):
        if nodo is None:                            # aquí verifica si el nodo está vacío
            return None
        return {
            "valor": nodo.valor,                                            
            "izquierda": self.obtener_estructura(nodo.izquierda),           
            "derecha":   self.obtener_estructura(nodo.derecha)              
        }

    def _es_numero(self, valor):
        try:
            float(valor)            # aquí intenta convertir a número
            return True
        except:                     # aquí falla → no es número
            return False

    def _comparar(self, a, b):
        # prioridad: números primero
        if self._es_numero(a) and not self._es_numero(b):
            return -1               # a es menor
        if not self._es_numero(a) and self._es_numero(b):
            return 1                # a es mayor
        # ambos números
        if self._es_numero(a) and self._es_numero(b):
            return float(a) - float(b)
        # ambos letras
        return (a > b) - (a < b)