import pytest
import json
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_first_three(client):
    response = client.get('/members')
    members = json.loads(response.data)
    assert len(members) == 3  # Verifico que haya 3 miembros al inicio

def test_get_members_returns_list_of_five(client):
    # Añado dos miembros
    client.post('/member', json={
        "first_name": "David",
        "id": 4,
        "age": 30,
        "lucky_numbers": [12, 34, 56]
    })
    client.post('/member', json={
        "first_name": "Emily",
        "id": 5,
        "age": 28,
        "lucky_numbers": [7, 13, 21]
    })
    # Verifico que la lista de miembros tiene 5 miembros
    response = client.get('/members')
    members = json.loads(response.data)
    assert len(members) == 5

def test_get_single_member_implemented(client):
    # Primero, me aseguro de que el miembro con ID 3443 esté creado
    client.post('/member', json={
        "first_name": "Tommy",
        "id": 3443,
        "age": 23,
        "lucky_numbers": [34, 65, 23, 4, 6]
    })
    
    # Ahora, hago la solicitud GET para obtener el miembro con ID 3443
    response = client.get('/member/3443')
    assert response.status_code == 200  # Verifico que la ruta GET /member/<id> esté implementada

def test_get_single_member_has_keys(client):
    response = client.get('/member/1')
    data = json.loads(response.data)
    assert "first_name" in data
    assert "id" in data
    assert "age" in data
    assert "lucky_numbers" in data

def test_get_first_member_tommy(client):
    response = client.get('/member/1')
    data = json.loads(response.data)
    assert "first_name" in data
    assert data["first_name"] == "Tommy"  # Verifico que el primer miembro sea Tommy

def test_delete_member(client):
    response = client.delete('/member/1')
    assert response.status_code == 200  # Verifico que la eliminación retorne 200 OK

def test_delete_response(client):
    # Añado un miembro antes de eliminarlo
    client.post('/member', json={
        "first_name": "Tommy",
        "id": 3443,
        "age": 23,
        "lucky_numbers": [34, 65, 23, 4, 6]
    })
    # Elimino al miembro que acabo de añadir
    response = client.delete('/member/3443')
    data = json.loads(response.data)
    assert "done" in data  # Verifico que la respuesta contenga la clave 'done'
    assert data["done"] == True  # Verifico que el valor de 'done' sea True

def test_get_members_returns_list_of_four(client):
    # Elimino un miembro
    client.delete('/member/3443')
    response = client.get('/members')
    members = json.loads(response.data)
    assert len(members) == 4  # Verifico que después de la eliminación haya 4 miembros


