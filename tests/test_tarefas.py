import pytest
from src.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_criar_tarefa(client):
    response = client.post('/tarefas', json={'titulo':'Teste','descricao':'Descrição'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['titulo'] == 'Teste'

def test_listar_tarefas(client):
    client.post('/tarefas', json={'titulo':'Teste2','descricao':'Desc2'})
    response = client.get('/tarefas')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) >= 1

def test_atualizar_tarefa(client):
    client.post('/tarefas', json={'titulo':'Atualizar','descricao':'Desc'})
    response = client.put('/tarefas/1', json={'status':'Concluído'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'Concluído'

def test_deletar_tarefa(client):
    client.post('/tarefas', json={'titulo':'Deletar','descricao':'Desc'})
    response = client.delete('/tarefas/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['msg'] == 'Tarefa deletada'
