#necesario para ingresar datos a la base de datos
from datetime import date
from pydantic import BaseModel
from decimal import Decimal

class countries(BaseModel):
    country_id:str
    country_name:str
    region_id:int

class departments(BaseModel):
    department_id:int
    department_name:str
    manager_id:int
    location_id:int

class employees(BaseModel):
    employee_id:int
    first_name:str
    last_name:str
    email:str
    phone_number:str
    hire_date:date
    job_id:str
    salary:Decimal
    commission_pct:Decimal
    manager_id:int
    department_id:int

class job_history(BaseModel):
    employee_id:int
    start_date:date
    end_date:date
    job_id:str
    department_id:int

class jobs(BaseModel):
    job_id:str
    job_title:str
    min_salary:int
    max_salary:int

class locations(BaseModel):
    location_id:int
    street_address:str
    postal_code:str
    city:str
    state_province:str
    country_id:str

class regions(BaseModel):
    region_id:int
    region_name:str
