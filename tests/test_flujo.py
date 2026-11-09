import time

from fastapi.testclient import TestClient
from app.main import app


cliente = TestClient(app)


def test_ciclo_categoria():
    nombre = f"Prueba {time.time_ns()}"
    respuesta = cliente.post("/categorias", params={"nombre": nombre})
    categorias = cliente.get("/categorias").json()

    assert respuesta.status_code == 200
    assert any(categoria["nombre"] == nombre for categoria in categorias)


def test_listar_categorias():
    respuesta = cliente.get("/categorias")

    assert respuesta.status_code == 200
    assert isinstance(respuesta.json(), list)


def test_crear_producto():
    categoria = cliente.post(
        "/categorias", params={"nombre": f"Prueba {time.time_ns()}"}
    ).json()
    producto = cliente.post(
        "/productos",
        params={"nombre": "Cuaderno", "categoria_id": categoria["id"]},
    )

    assert producto.status_code == 200
    assert producto.json()["categoria_id"] == categoria["id"]
