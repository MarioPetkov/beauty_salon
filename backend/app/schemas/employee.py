from pydantic import BaseModel
from datetime import date
from typing import Optional

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    birth_date: Optional[date] = None
    category_id: Optional[int] = None

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    birth_date: Optional[date] = None
    category_id: Optional[int] = None
    is_active: Optional[bool] = None 