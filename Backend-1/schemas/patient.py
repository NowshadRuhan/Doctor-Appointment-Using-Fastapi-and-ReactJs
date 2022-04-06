from pydantic import BaseModel


class Patient(BaseModel):
    name: str
    user_name: str
    email: str
    password: str
    status: int


class PatientLogin(BaseModel):
    user_name: str
    password: str


class Doctor(BaseModel):
    name: str
    user_name: str
    email: str
    address: str
    password: str
    status: int

class DoctorLogin(BaseModel):
    user_name: str
    password: str