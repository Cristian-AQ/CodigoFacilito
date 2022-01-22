from fastapi import FastAPI
from config.db import conn
from models.model import countries,departments,employees,job_history,jobs,locations,regions
from schemas.schema import regions as reg
from schemas.schema import countries as cnt
app = FastAPI()

@app.get('/countries')
def get_countries():
    return conn.execute(countries.select()).fetchall()

@app.get('/departments')
def get_departments():
    return conn.execute(departments.select()).fetchall()

@app.get('/employees')
def get_employees():
    return conn.execute(employees.select()).fetchall()

@app.get('/jobhistory')
def get_jobhistory():
    return conn.execute(job_history.select()).fetchall()

@app.get('/jobs')
def get_jobs():
    return conn.execute(jobs.select()).fetchall()

@app.get('/locations')
def get_locations():
    return conn.execute(locations.select()).fetchall()

@app.get('/regions')
def get_regions():
    return conn.execute(regions.select()).fetchall()

@app.get('/regions/{id}')
def get_regions_id(id:int):
    dato = conn.execute(regions.select().where(regions.c.region_id==id)).first()
    return dato

@app.get('/employees/orden')
def get_orden():
    dato = conn.execute(employees.select().order_by(employees.c.first_name)).fetchall()
    return dato

@app.get('/locations/where')
def get_where():
    dato = conn.execute(locations.select().where(locations.c.country_id==countries.c.country_id)).fetchall()
    a = []
    for x in range(len(dato)):
        if int(dato[x].location_id)>1500:
            a.append(dato[x].postal_code)
    return a

@app.get('/countries/name')
def get_name():
    a = []
    dato = conn.execute(countries.select().where(locations.c.country_id==countries.c.country_id)).fetchall()
    for x in range(len(dato)):
        if int(dato[x].region_id) == 1:
            a.append([dato[x].country_name,dato[x].country_id])
    return a

@app.post('/regions/add')
def post_new(regi:reg):
    new = {"region_id":regi.region_id,"region_name":regi.region_name}
    conn.execute(regions.insert().values(new))
    return 'registrado'

@app.delete('/regions/delete/{id}')
def delete_regions(id:int):
    dato = conn.execute(regions.delete().where(regions.c.region_id==id))
    return f"Eliminando {id}"

@app.put('/regions/update/{id}')
def update_regions(id:int,regi:reg):
    dato = conn.execute(regions.update().values(region_name=regi.region_name).where(regions.c.region_id==id))
    return f'actualizado {id}'

@app.post('/countries/add')
def post_countries(coun:cnt):
    new = {"country_id":coun.country_id,"country_name":coun.country_name,"region_id":coun.region_id}
    conn.execute(countries.insert().values(new))
    return 'registrado'

@app.delete('/countries/delete/{id}')
def delete_countries(id:str):
    dato = conn.execute(countries.delete().where(countries.c.country_id==id))
    return f"Eliminando {id}"

@app.get('/employees/limit{l}offset{o}')
def get_limit(l:int,o:int):
    dato = conn.execute(employees.select().limit(l).offset(o)).fetchall()
    return dato

