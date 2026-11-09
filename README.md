# pruebitasgitactions

API de categorías y productos con FastAPI y persistencia JSON.

## Ejecutar localmente

```bash
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8005
```

Documentación interactiva: http://127.0.0.1:8005/docs

## Pruebas

```bash
python -m pytest -q
```

GitHub Actions ejecuta las pruebas al hacer push o abrir un pull request hacia `main` o `dev`. También puede iniciarse manualmente desde la pestaña **Actions**.
