from fastapi.encoders import jsonable_encoder
from app.core.database import get_supabase_client
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate

supabase = get_supabase_client()

def create_employee(employee_data: EmployeeCreate):
    # Convert the Pydantic model to JSON-compatible dict
    json_data = jsonable_encoder(employee_data)
    response = supabase.table('employees').insert(json_data).execute()
    # Return the first item since insert returns a list with one item
    return response.data[0] if response.data else None

def get_employee(employee_id: int):
    response = supabase.table('employees').select('*').eq('id', employee_id).execute()
    # Return the first item since we're querying by ID
    return response.data[0] if response.data else None

def update_employee(employee_id: int, employee_data: EmployeeUpdate):
    # Convert the Pydantic model to JSON-compatible dict
    json_data = jsonable_encoder(employee_data)
    response = supabase.table('employees').update(json_data).eq('id', employee_id).execute()
    # Return the first item since update returns a list with one item
    return response.data[0] if response.data else None

def delete_employee(employee_id: int):
    response = supabase.table('employees').delete().eq('id', employee_id).execute()
    # Return the first item since delete returns a list with one item
    return response.data[0] if response.data else None 