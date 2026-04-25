# Gestor de Contactos Alfabetico
# Estructura de Datos II | BST + MVC | Python en VS Code

## ESTRUCTURA DEL PROYECTO

GestorContactos/
    model/
        __init__.py
        contacto.py       <-- Datos del contacto (nombre, telefono, correo)
        nodo.py           <-- Nodo del arbol BST
        arbol_bst.py      <-- Logica completa del arbol (recursiva)
    view/
        __init__.py
        vista.py          <-- Menu e interfaz de usuario en consola
    controller/
        __init__.py
        controlador.py    <-- Coordina Model y View
    main.py               <-- Punto de entrada
    README.md


## COMO EJECUTAR EN VS CODE

1. Instala Python 3.10 o superior desde https://python.org

2. Abre la carpeta GestorContactos en VS Code:
       File --> Open Folder --> selecciona GestorContactos

3. Abre una terminal en VS Code:
       Terminal --> New Terminal

4. Crea y activa el entorno virtual:

   En Windows:
       python -m venv venv
       venv\Scripts\activate

   En Mac/Linux:
       python3 -m venv venv
       source venv/bin/activate

5. Ejecuta el programa:
       python main.py


## COMO FUNCIONA EL BST

El BST ordena contactos ALFABETICAMENTE por nombre:

        [Carlos]          <-- Raiz (primer insertado)
       /         \
    [Ana]       [Luis]    <-- Ana < Carlos | Luis > Carlos
       \        /    \
     [Bruno] [Diana] [Mario]

Recorrido INORDEN (Izq --> Raiz --> Der) = ORDEN ALFABETICO:
    Ana --> Bruno --> Carlos --> Diana --> Luis --> Mario


## ARQUITECTURA MVC

Model      : contacto.py, nodo.py, arbol_bst.py  --> logica del arbol y datos
View       : vista.py                             --> muestra menus y resultados
Controller : controlador.py                       --> conecta Model y View


## FUNCIONALIDADES

  1 - Insertar contacto         (metodo insertarRec, recursivo)
  2 - Buscar contacto           (metodo buscar_nodo, recursivo)
  3 - Editar contacto           (modifica telefono/correo)
  4 - Eliminar contacto         (3 casos del BST, recursivo)
  5 - Listar alfabeticamente    (inorden recursivo)
  6 - Ver arbol visual          (dibuja el BST en consola)
  7 - Recorrido Preorden        (raiz, izq, der)
  8 - Recorrido Postorden       (izq, der, raiz)
  0 - Salir
