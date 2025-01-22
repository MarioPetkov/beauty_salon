from fastapi import FastAPI
from app.api import employees
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
import json

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

app = FastAPI()

# Use the custom JSON encoder
app.json_encoder = CustomJSONEncoder

app.include_router(employees.router, prefix="/api")
