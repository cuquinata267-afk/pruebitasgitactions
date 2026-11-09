from unittest.mock import patch

from app.crud import create_categoria_db, get_categorias


def test_crear_categoria():
    db = {"categorias": [{"id": 2, "nombre": "Libros"}], "productos": []}

    with patch("app.crud._load_db", return_value=db), patch("app.crud._save_db"):
        categoria = create_categoria_db("Música")

    assert categoria == {"id": 3, "nombre": "Música"}


def test_listar_categorias():
    categorias = [{"id": 1, "nombre": "Libros"}]
    db = {"categorias": categorias, "productos": []}

    with patch("app.crud._load_db", return_value=db):
        assert get_categorias() == categorias


def test_id_inicial():
    db = {"categorias": [], "productos": []}

    with patch("app.crud._load_db", return_value=db), patch("app.crud._save_db"):
        categoria = create_categoria_db("Música")

    assert categoria["id"] == 1
