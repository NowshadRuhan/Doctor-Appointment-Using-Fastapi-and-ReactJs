from config.db import conn
from fastapi import APIRouter
from models.patient import tbl_patients

patient = APIRouter()

@patient.get('/')
async def fetch_user():
    return conn.execute(tbl_patients.select()).fetchall()
