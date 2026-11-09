import time

from app.main import app


cliente = app.test_client()


def test_ciclo_categoria():
    nombre = f"Prueba {time.time_ns()}"
    respuesta = cliente.post("/categorias", query_string={"nombre": nombre})
    categorias = cliente.get("/categorias").json

    assert respuesta.status_code == 200
    assert any(categoria["nombre"] == nombre for categoria in categorias)


def test_listar_categorias():
    respuesta = cliente.get("/categorias")

    assert respuesta.status_code == 200
    assert isinstance(respuesta.json, list)


def test_crear_producto():
    categoria = cliente.post(
        "/categorias", query_string={"nombre": f"Prueba {time.time_ns()}"}
    ).json
    producto = cliente.post(
        "/productos",
        query_string={"nombre": "Cuaderno", "categoria_id": categoria["id"]},
    )

    assert producto.status_code == 200
    assert producto.json["categoria_id"] == categoria["id"]
