from fastapi import FastAPI
from token import OP
from typing import Optional

import uvicorn
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

from routes.patient import patient

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = "http://localhost:3000/",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patient)

# @app.get("/")
# def read_root():
#     return {"data": {"name": "Nowshad", "job_position": "Lead Software Engineer"}}
