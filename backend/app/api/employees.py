from fastapi import APIRouter, HTTPException
from app.services.employee_service import create_employee, get_employee, update_employee, delete_employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate

router = APIRouter()

@router.post("/employees/", response_model=dict)
def create_employee_endpoint(employee: EmployeeCreate):
    return create_employee(employee)

@router.get("/employees/{employee_id}", response_model=dict)
def get_employee_endpoint(employee_id: int):
    employee = get_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.put("/employees/{employee_id}", response_model=dict)
def update_employee_endpoint(employee_id: int, employee: EmployeeUpdate):
    return update_employee(employee_id, employee)

@router.delete("/employees/{employee_id}", response_model=dict)
def delete_employee_endpoint(employee_id: int):
    return delete_employee(employee_id) 