from fastapi import FastAPI
from database import supabase

app = FastAPI()

@app.get("/")
async def read_data():
    try:
        # Example query - adjust table name and columns as needed
        response = supabase.table('appointments').select("*").execute()
        return {"data": response.data}
    except Exception as e:
        return {"error": str(e)}
