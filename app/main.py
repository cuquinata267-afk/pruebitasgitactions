from flask import Flask, jsonify, request

from . import crud


app = Flask(__name__)


@app.get("/categorias")
def listar_categorias():
    return jsonify(crud.get_categorias())


@app.post("/categorias")
def crear_categoria():
    nombre = request.args.get("nombre")
    if not nombre:
        return jsonify({"error": "Falta el nombre de la categoría"}), 400

    return jsonify(crud.create_categoria_db(nombre))


@app.post("/productos")
def crear_producto():
    nombre = request.args.get("nombre")
    categoria_id = request.args.get("categoria_id", type=int)
    if not nombre or categoria_id is None:
        return jsonify({"error": "Faltan datos del producto"}), 400

    producto = crud.create_producto_db(nombre, categoria_id)
    if "error" in producto:
        return jsonify(producto), 404

    return jsonify(producto)
