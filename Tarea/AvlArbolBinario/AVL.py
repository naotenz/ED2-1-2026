class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1


# Calcula la altura del nodo
def altura(n):
    return n.altura if n else 0


# Calcula el factor de equilibrio
def balance(n):
    return altura(n.izq) - altura(n.der)


# Rotación simple a la derecha
def rotar_derecha(y):
    x = y.izq
    T2 = x.der

    # Rotación
    x.der = y
    y.izq = T2

    # Actualizar alturas
    y.altura = 1 + max(altura(y.izq), altura(y.der))
    x.altura = 1 + max(altura(x.izq), altura(x.der))

    return x


# Rotación simple a la izquierda
def rotar_izquierda(x):
    y = x.der
    T2 = y.izq

    y.izq = x
    x.der = T2

    x.altura = 1 + max(altura(x.izq), altura(x.der))
    y.altura = 1 + max(altura(y.izq), altura(y.der))

    return y


# Inserción recursiva
def insertar_rec(nodo, valor):
    # Paso 1: insertar como BST
    if not nodo:
        return NodoAVL(valor)

    if valor < nodo.valor:
        nodo.izq = insertar_rec(nodo.izq, valor)
    else:
        nodo.der = insertar_rec(nodo.der, valor)

    # Paso 2: actualizar altura
    nodo.altura = 1 + max(altura(nodo.izq), altura(nodo.der))

    # Paso 3: verificar balance
    b = balance(nodo)

    # Paso 4: rotaciones
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