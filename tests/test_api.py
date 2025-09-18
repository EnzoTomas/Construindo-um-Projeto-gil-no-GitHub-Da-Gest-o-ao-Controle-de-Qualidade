import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))


import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_task_with_priority(client):
    """
    Testa se a criação de uma tarefa com prioridade funciona corretamente.
    """
    data = {'title': 'Tarefa com Prioridade', 'description': 'Testando a prioridade', 'priority': 'Alta'}
    response = client.post('/tasks', json=data)
    response_data = response.get_json()

    assert response.status_code == 201
    assert response_data['title'] == 'Tarefa com Prioridade'
    assert response_data['priority'] == 'Alta'
    assert response_data['id'] is not None

def test_update_task_priority(client):
    """
    Testa se a prioridade de uma tarefa pode ser atualizada.
    """
    
    create_response = client.post('/tasks', json={'title': 'Tarefa para Atualizar'})
    task_id = create_response.get_json()['id']

    
    update_data = {'priority': 'Baixa'}
    update_response = client.put(f'/tasks/{task_id}', json=update_data)
    update_response_data = update_response.get_json()

    assert update_response.status_code == 200
    assert update_response_data['priority'] == 'Baixa'