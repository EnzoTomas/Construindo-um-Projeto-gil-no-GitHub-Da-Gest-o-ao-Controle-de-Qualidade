import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_task(client):
    """
    Testa se a criação de uma tarefa retorna o status 201 e o ID correto.
    """
    response = client.post('/tasks', json={'title': 'Tarefa de Teste', 'description': 'Descrição'})
    data = response.get_json()

    assert response.status_code == 201
    assert data['title'] == 'Tarefa de Teste'
    assert data['id'] is not None