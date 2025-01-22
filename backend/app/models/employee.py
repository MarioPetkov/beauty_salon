from pydantic import BaseModel
from datetime import date
from typing import Optional

class Employee(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone_number: str
    birth_date: Optional[date] = None
    hire_date: Optional[date] = None
    category_id: Optional[int] = None
    is_active: bool = True
    created_at: Optional[date] = None
    updated_at: Optional[date] = None 