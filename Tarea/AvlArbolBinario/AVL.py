class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1


# -------- FUNCIONES BASE --------
def altura(n):
    return n.altura if n else 0

def balance(n):
    return altura(n.izq) - altura(n.der)

def rotar_derecha(y):
    x = y.izq
    T2 = x.der
    x.der = y
    y.izq = T2
    y.altura = 1 + max(altura(y.izq), altura(y.der))
    x.altura = 1 + max(altura(x.izq), altura(x.der))
    return x

def rotar_izquierda(x):
    y = x.der
    T2 = y.izq
    y.izq = x
    x.der = T2
    x.altura = 1 + max(altura(x.izq), altura(x.der))
    y.altura = 1 + max(altura(y.izq), altura(y.der))
    return y


# -------- AVL RECURSIVO --------
def insertar_rec(nodo, valor):
    if not nodo:
        return NodoAVL(valor)

    if valor < nodo.valor:
        nodo.izq = insertar_rec(nodo.izq, valor)
    else:
        nodo.der = insertar_rec(nodo.der, valor)

    nodo.altura = 1 + max(altura(nodo.izq), altura(nodo.der))
    b = balance(nodo)

    # Rotaciones
    if b > 1 and valor < nodo.izq.valor:
        return rotar_derecha(nodo)
    if b < -1 and valor > nodo.der.valor:
        return rotar_izquierda(nodo)
    if b > 1 and valor > nodo.izq.valor:
        nodo.izq = rotar_izquierda(nodo.izq)
        return rotar_derecha(nodo)
    if b < -1 and valor < nodo.der.valor:
        nodo.der = rotar_derecha(nodo.der)
        return rotar_izquierda(nodo)

    return nodo


# -------- AVL ITERATIVO --------
def insertar_iter(raiz, valor):
    if not raiz:
        return NodoAVL(valor)

    stack = []
    nodo = raiz

    # Inserción tipo BST
    while nodo:
        stack.append(nodo)
        if valor < nodo.valor:
            if nodo.izq:
                nodo = nodo.izq
            else:
                nodo.izq = NodoAVL(valor)
                stack.append(nodo.izq)
                break
        else:
            if nodo.der:
                nodo = nodo.der
            else:
                nodo.der = NodoAVL(valor)
                stack.append(nodo.der)
                break

    # Rebalanceo
    while stack:
        nodo = stack.pop()
        nodo.altura = 1 + max(altura(nodo.izq), altura(nodo.der))
        b = balance(nodo)
        # (Aquí puedes aplicar mismas rotaciones si quieres versión completa)

    return raiz