from flask import Flask, request, jsonify, send_from_directory
from model import ArbolBinario

app = Flask(__name__)
arbol = ArbolBinario()

@app.route("/")
def inicio():
    return send_from_directory(".", "view.html")

@app.route("/insertar", methods=["POST"])
def insertar():
    data  = request.json
    valor = data["valor"]           # aquí obtiene el valor (sin convertir)

    # ── NUEVO: verificar si ya existe ────────────────────────────────────────
    info = arbol.buscar(valor)
    if info:
        return jsonify({
            "mensaje":  "duplicado",
            "detalle":  f"'{valor}' ya existe en el árbol",
            "posicion": info["posicion"],
            "altura":   info["altura"]
        }), 200
    # ─────────────────────────────────────────────────────────────────────────

    arbol.insertar(valor)           # aquí inserta solo si no existe
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
    arbol = ArbolBinario()          # aquí reinicia el árbol (borra todos los nodos)
    return jsonify({"mensaje": "Árbol reiniciado"})