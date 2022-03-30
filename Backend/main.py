from token import OP
from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from routes.patient import patient

app = FastAPI()


app.include_router(patient)

# @app.get("/")
# def read_root():
#     return {"data": {"name": "Nowshad", "job_position": "Lead Software Engineer"}}
