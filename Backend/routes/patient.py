from config.db import conn
from fastapi import APIRouter
from models.patient import tbl_patients
from schemas.patient import Patient

patient = APIRouter()

@patient.get('/')
async def fetch_users():
    return conn.execute(tbl_patients.select()).fetchall()


@patient.get('/{id}')
async def fetch_user(id: int):
    return conn.execute(tbl_patients.select().where(tbl_patients.c.id==id)).first()


@patient.post('/')
async def create_user(patient: Patient):
    conn.execute(tbl_patients.insert().values(
        name = patient.name,
        user_name = patient.user_name,
        email = patient.email,
        password = patient.password,
        status = 1
    ))
    return conn.execute(tbl_patients.select()).fetchall()


@patient.put('/{id}')
async def update_user(id: int, patient: Patient):
    conn.execute(tbl_patients.update().values(
        name = patient.name,
        user_name = patient.user_name,
        email = patient.email,
        password = patient.password,
        status = 1
    ).where(tbl_patients.c.id==id))
    return conn.execute(tbl_patients.select()).fetchall()


@patient.delete('/{id}')
async def delete_user(id: int):
    conn.execute(tbl_patients.delete().where(tbl_patients.c.id==id))
    return conn.execute(tbl_patients.select()).fetchall()
