from fastapi import FastAPI
from app.api import employees

app = FastAPI()

app.include_router(employees.router, prefix="/api")
