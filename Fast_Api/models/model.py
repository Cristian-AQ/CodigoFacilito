#necesario para hacer consultas a la base de datos
from sqlalchemy import Table,Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DECIMAL, Date, Integer, String
from config.db import meta

countries = Table('countries',meta,Column(
    'country_id',String(2),primary_key=True),
    Column('country_name',String(40)),
    Column('region_id',Integer,ForeignKey('regions.region_id'))
)
departments = Table('departments',meta,Column(
    'department_id',Integer,primary_key=True),
    Column('department_name',String(30)),
    Column('manager_id',Integer,ForeignKey('employees.manager_id')),
    Column('location_id',Integer,ForeignKey('locations.location_id'))
)
employees = Table('employees',meta,Column(
    'employee_id',Integer,primary_key=True),
    Column('first_name',String(20)),
    Column('last_name',String(25)),
    Column('email',String(25)),
    Column('phone_number',String(20)),
    Column('hire_date',Date),
    Column('job_id',String(10),ForeignKey('jobs.job_id')),
    Column('salary',DECIMAL(8,2)),
    Column('commission_pct',DECIMAL(2,2)),
    Column('manager_id',Integer,ForeignKey('employees.employee_id')),
    Column('department_id',Integer,ForeignKey('departments.department_id'))
)
job_history = Table('job_history',meta,Column(
    'employee_id',Integer,primary_key=True),
    Column('start_date',Date,primary_key=True),
    Column('end_date',Date),
    Column('job_id',String(10)),
    Column('department_id',Integer,ForeignKey('departments.department_id'))
)
jobs = Table('jobs',meta,Column(
    'job_id',String(10),primary_key=True),
    Column('job_title',String(35)),
    Column('min_salary',Integer),
    Column('max_salary',Integer)
)
locations = Table('locations',meta,Column(
    'location_id',Integer,primary_key=True),
    Column('street_address',String(40)),
    Column('postal_code',String(12)),
    Column('city',String(30)),
    Column('state_province',String(30)),
    Column('country_id',String(2),ForeignKey('countries.country_id'))
)
regions = Table('regions',meta,Column(
    'region_id',Integer,primary_key=True),
    Column('region_name',String(25))
)