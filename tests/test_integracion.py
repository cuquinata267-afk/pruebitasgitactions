from fastapi.testclient import TestClient
from app import crud
from app.main import app
import pytest


cliente = TestClient(app)


@pytest.fixture(autouse=True)
def preparar_datos():
    crud._save_db(
        {
            "categorias": [{"id": 1, "nombre": "Libros"}],
            "productos": [{"id": 101, "nombre": "Novela", "categoria_id": 1}],
        }
    )


def test_crear_categoria_y_producto():
    respuesta = cliente.post("/categorias", params={"nombre": "Música"})
    categoria_id = respuesta.json()["id"]

    producto = cliente.post(
        "/productos", params={"nombre": "Guitarra", "categoria_id": categoria_id}
    )

    assert respuesta.status_code == 200
    assert producto.status_code == 200
    assert producto.json()["categoria_id"] == categoria_id


def test_respuesta_categoria():
    respuesta = cliente.post("/categorias", params={"nombre": "Juegos"})

    assert respuesta.status_code == 200
    assert respuesta.json()["nombre"] == "Juegos"


def test_producto_sin_categoria():
    respuesta = cliente.post(
        "/productos", params={"nombre": "Cuaderno", "categoria_id": 999}
    )

    assert respuesta.status_code == 404
