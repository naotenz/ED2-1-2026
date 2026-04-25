from flask import Flask, request, jsonify, send_from_directory
from model import ArbolBinario   # 👈 cambia importación

app = Flask(__name__)
arbol = ArbolBinario()

@app.route("/")
def inicio():
    # aquí carga la vista
    return send_from_directory(".", "view.html")

@app.route("/insertar", methods=["POST"])
def insertar():
    data = request.json
    valor = data["valor"]
    # ya NO usar int()
    # aquí obtiene valor

    arbol.insertar(valor)
    # aquí inserta

    return jsonify({"mensaje": "ok"})

@app.route("/recorrido/<tipo>")
def recorrido(tipo):
    resultado = []

    if tipo == "inorden":
        arbol.inorden(arbol.raiz, resultado)

    elif tipo == "preorden":
        arbol.preorden(arbol.raiz, resultado)

    elif tipo == "postorden":
        arbol.postorden(arbol.raiz, resultado)

    return jsonify(resultado)

@app.route("/arbol")
def obtener_arbol():
    return jsonify(arbol.obtener_estructura(arbol.raiz))

@app.route("/limpiar", methods=["POST"])
def limpiar():
    global arbol
    arbol = ArbolBinario()
    # aquí reinicia el árbol (borra todos los nodos)

    return jsonify({"mensaje": "Árbol reiniciado"})

if __name__ == "__main__":
    app.run(debug=True)