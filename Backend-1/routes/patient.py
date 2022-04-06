from config.db import conn
from fastapi import APIRouter
from models.patient import tbl_patients, tbl_doctors, tbl_appoinment
from schemas.patient import Patient, PatientLogin, Doctor, DoctorLogin, Appointment

patient = APIRouter()

@patient.get('/')
async def fetch_users():
    return conn.execute(tbl_patients.select()).fetchall()


@patient.get('/{id}')
async def fetch_user(id: int):
    return conn.execute(tbl_patients.select().where(tbl_patients.c.id==id)).first()


@patient.post('/login-user')
async def login_user(patient: PatientLogin):
    user_name = patient.user_name
    password = patient.password
    return conn.execute(tbl_patients.select().where(tbl_patients.c.user_name==user_name and tbl_patients.c.password==password)).first()


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


@patient.post('/reg-doctor')
async def create_doctor(dcotor: Doctor):
    conn.execute(tbl_doctors.insert().values(
        name = dcotor.name,
        user_name = dcotor.user_name,
        email = dcotor.email,
        address = dcotor.email,
        password = dcotor.password,
        status = 1
    ))
    return conn.execute(tbl_doctors.select()).fetchall()


@patient.post('/login-doctor')
async def login_doctor(dcotor: DoctorLogin):
    user_name = dcotor.user_name
    password = dcotor.password
    return conn.execute(tbl_doctors.select().where(tbl_doctors.c.user_name==user_name and tbl_doctors.c.password==password)).first()

@patient.post('/appointment-doctor')
async def appointment_doctor(appiontment: Appointment):
    patients_id = appiontment.patients_id
    doctor_id = appiontment.doctor_id
    appiontment_time = appiontment.appiontment_time
    conn.execute(tbl_appoinment.insert().values(
        patients_id = patients_id,
        doctor_id = doctor_id,
        appiontment_time = appiontment_time
    ))
    return conn.execute(tbl_appoinment.select()).fetchall()
