from token import OP
from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"data": {"name": "Nowshad", "job_position": "Lead Software Engineer"}}
