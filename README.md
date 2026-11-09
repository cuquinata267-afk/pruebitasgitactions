# pruebitasgitactions

API de categorías y productos con Flask y persistencia JSON.

## Ejecutar localmente

```bash
python -m pip install -r requirements.txt
python -m flask --app app.main run --debug --port 8005
```

La API queda disponible en http://127.0.0.1:8005.

## Pruebas

```bash
python -m pytest -q
```

GitHub Actions ejecuta las pruebas al hacer push o abrir un pull request hacia `main` o `dev`. También puede iniciarse manualmente desde la pestaña **Actions**.
