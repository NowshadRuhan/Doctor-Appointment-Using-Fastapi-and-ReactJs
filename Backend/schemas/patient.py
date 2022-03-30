from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    user_name: str
    email: str
    password: str
    status: int