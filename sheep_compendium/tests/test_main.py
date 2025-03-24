import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_update_sheep():
    updated_sheep_data = {
        "id": 1,
        "name": "Daisy",
        "breed": "F1",
        "sex": "ewe"
    }

    sheep_id = 1    
    response = client.put(f"/sheep/{sheep_id}", json=updated_sheep_data)
    assert response.status_code == 200

    updated_sheep = response.json()
    assert updated_sheep["id"] == sheep_id
    assert updated_sheep["name"] == "Daisy"
    assert updated_sheep["breed"] == "F1"
    assert updated_sheep["sex"] == "ewe"

    response = client.get(f"/sheep/{sheep_id}")
    assert response.status_code == 200
    assert response.json() == updated_sheep_data