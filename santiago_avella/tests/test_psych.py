import pytest
from fastapi import status

class TestPsicologia:
    """Suite de tests personalizada para el dominio Psicología (consulta)"""

    def test_psych_create_consulta_success(self, client):
        data = {
            "paciente": "Juan Pérez",
            "motivo": "Ansiedad",
            "fecha": "2025-10-01",
            "realizada": False
        }
        response = client.post("/consultas/", json=data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["paciente"] == data["paciente"]

    def test_psych_create_consulta_missing_field(self, client):
        data = {
            # "paciente": "Ana Torres",
            "motivo": "Depresión",
            "fecha": "2025-10-02",
            "realizada": False
        }
        response = client.post("/consultas/", json=data)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_psych_get_consulta_by_id_success(self, client):
        data = {
            "paciente": "Carlos Ruiz",
            "motivo": "Estrés laboral",
            "fecha": "2025-10-03",
            "realizada": False
        }
        create_resp = client.post("/consultas/", json=data)
        consulta_id = create_resp.json()["id"]
        response = client.get(f"/consultas/{consulta_id}")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["paciente"] == data["paciente"]

    def test_psych_consulta_not_found(self, client):
        response = client.get("/consultas/99999")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_psych_update_consulta_success(self, client):
        data = {
            "paciente": "Laura Gómez",
            "motivo": "Insomnio",
            "fecha": "2025-10-04",
            "realizada": False
        }
        create_resp = client.post("/consultas/", json=data)
        consulta_id = create_resp.json()["id"]
        update_data = {"realizada": True}
        response = client.patch(f"/consultas/{consulta_id}", json=update_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["realizada"] is True

    def test_psych_delete_consulta_success(self, client):
        data = {
            "paciente": "Miguel Ángel",
            "motivo": "Fobias",
            "fecha": "2025-10-05",
            "realizada": False
        }
        create_resp = client.post("/consultas/", json=data)
        consulta_id = create_resp.json()["id"]
        response = client.delete(f"/consultas/{consulta_id}")
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_psych_update_invalid_field(self, client):
        data = {
            "paciente": "Sofía Herrera",
            "motivo": "Autoestima",
            "fecha": "2025-10-06",
            "realizada": False
        }
        create_resp = client.post("/consultas/", json=data)
        consulta_id = create_resp.json()["id"]
        update_data = {"campo_inexistente": "valor"}
        response = client.patch(f"/consultas/{consulta_id}", json=update_data)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_psych_list_all_consultas(self, client):
        response = client.get("/consultas/")
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), list)
