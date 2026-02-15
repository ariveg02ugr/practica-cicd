# Calculadora API - CI/CD

API REST simple con pipeline CI/CD automatizado.

## Instalación
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar
```bash
python app.py
```

## Tests
```bash
pytest -v test_app.py
```

## Endpoints

- `GET /health` - Health check
- `POST /sum` - Sumar dos números
- `POST /multiply` - Multiplicar dos números
