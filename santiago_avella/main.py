from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

class Consulta(BaseModel):
    id: Optional[int] = None
    paciente: str
    motivo: str
    fecha: str
    realizada: bool
    notas: Optional[str] = None

consultas = []
consulta_id_counter = 1

def get_consulta_by_id(consulta_id):
    for c in consultas:
        if c['id'] == consulta_id:
            return c
    return None

@app.post("/consultas/", status_code=status.HTTP_201_CREATED)
def create_consulta(consulta: Consulta):
    global consulta_id_counter
    consulta.id = consulta_id_counter
    consulta_id_counter += 1
    consultas.append(consulta.dict())
    return consulta

@app.get("/consultas/{consulta_id}")
def get_consulta(consulta_id: int):
    consulta = get_consulta_by_id(consulta_id)
    if not consulta:
        raise HTTPException(status_code=404, detail="Consulta no encontrada")
    return consulta

@app.get("/consultas/")
def list_consultas():
    return consultas

@app.patch("/consultas/{consulta_id}")
def update_consulta(consulta_id: int, data: dict):
    consulta = get_consulta_by_id(consulta_id)
    if not consulta:
        raise HTTPException(status_code=404, detail="Consulta no encontrada")
    for key, value in data.items():
        if key not in consulta:
            raise HTTPException(status_code=422, detail="Campo inválido")
        consulta[key] = value
    return consulta

@app.delete("/consultas/{consulta_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_consulta(consulta_id: int):
    global consultas
    consulta = get_consulta_by_id(consulta_id)
    if not consulta:
        raise HTTPException(status_code=404, detail="Consulta no encontrada")
    consultas = [c for c in consultas if c['id'] != consulta_id]
    return
