from app.core.database import get_supabase_client
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate

supabase = get_supabase_client()

def create_employee(employee_data: EmployeeCreate):
    response = supabase.table('employees').insert(employee_data.dict()).execute()
    return response.data

def get_employee(employee_id: int):
    response = supabase.table('employees').select('*').eq('id', employee_id).execute()
    return response.data

def update_employee(employee_id: int, employee_data: EmployeeUpdate):
    response = supabase.table('employees').update(employee_data.dict(exclude_unset=True)).eq('id', employee_id).execute()
    return response.data

def delete_employee(employee_id: int):
    response = supabase.table('employees').delete().eq('id', employee_id).execute()
    return response.data 