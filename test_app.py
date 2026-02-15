import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Q1 - Tests Unitarios
def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

def test_suma_basica(client):
    response = client.post('/sum', json={'a': 2, 'b': 3})
    assert response.status_code == 200
    assert response.json['result'] == 5

def test_suma_negativos(client):
    response = client.post('/sum', json={'a': -5, 'b': 3})
    assert response.json['result'] == -2

def test_suma_decimales(client):
    response = client.post('/sum', json={'a': 2.5, 'b': 3.5})
    assert response.json['result'] == 6.0

def test_suma_error_tipo(client):
    response = client.post('/sum', json={'a': 'texto', 'b': 3})
    assert response.status_code == 400

# Q2 - Tests de Integración
def test_multiply_basico(client):
    response = client.post('/multiply', json={'a': 4, 'b': 5})
    assert response.status_code == 200
    assert response.json['result'] == 20

def test_multiply_por_cero(client):
    response = client.post('/multiply', json={'a': 5, 'b': 0})
    assert response.json['result'] == 0

def test_flujo_completo(client):
    # Test de integración: health + operaciones
    health = client.get('/health')
    assert health.status_code == 200
    
    suma = client.post('/sum', json={'a': 10, 'b': 5})
    assert suma.json['result'] == 15
    
    mult = client.post('/multiply', json={'a': 3, 'b': 4})
    assert mult.json['result'] == 12

