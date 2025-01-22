from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from app.services.employee_service import create_employee, get_employee, update_employee, delete_employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate

router = APIRouter()

@router.post("/employees/", response_model=dict)
def create_employee_endpoint(employee: EmployeeCreate):
    result = create_employee(employee)
    return jsonable_encoder(result)

@router.get("/employees/{employee_id}", response_model=dict)
def get_employee_endpoint(employee_id: int):
    employee = get_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return jsonable_encoder(employee)

@router.put("/employees/{employee_id}", response_model=dict)
def update_employee_endpoint(employee_id: int, employee: EmployeeUpdate):
    return jsonable_encoder(update_employee(employee_id, employee))

@router.delete("/employees/{employee_id}", response_model=dict)
def delete_employee_endpoint(employee_id: int):
    return jsonable_encoder(delete_employee(employee_id)) 