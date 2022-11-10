from os.path import isfile, join
import os
from typing import Optional, List
import re
from unittest import result
from fastapi import FastAPI, File, Form, UploadFile, Request, Header
from fastapi import APIRouter, Response, Form
from fastapi.responses import HTMLResponse
from pandas import DataFrame
from pyparsing import And         #Permite dividir las rutas de la app
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from schema.user_schema import UserSchema, DataUser
from config.db3 import engine                    #conn
from model.users import users
#from werkzeug.security import generate_password_hash, check_password_hash
#import panel as pn
from datetime import date
from fastapi.templating import Jinja2Templates


volar = FastAPI()
#carga = APIRouter()
templates = Jinja2Templates(directory="templates")

"""producto		IdProducto	Producto	Precio		IdTipoProducto
sucursal		IdSucursal	Sucursal	Domicilio	IdLocalidad	Latitud		Longitud
venta			IdVenta		Fecha		Fecha_Entrega	IdSucursal	IdProducto	Precio
"""


preg1 = "SELECT Sucursal, Domicilio, IdSucursal, Latitud, Longitud FROM sucursal order by Sucursal desc"
preg2 = "SELECT Producto, Precio FROM producto order by Producto desc"
#preg2 = "select r.driverId, count(r.driverId) as total, d.driverName, d.driverSurName from results as r, drivers as d where r.points=10 and r.driverId = d.driverId group by r.driverId order by 2 desc"
#preg3 = "SELECT Sucursal, Producto FROM venta WHERE order by Sucursal desc"
#preg3 = "select c.circuitName, count(r.circuitId) as total  from circuitos as c, races as r where c.circuitId = r.circuitId group by c.circuitName order by 2 desc"
preg4 = "select d.driverName, d.driverSurName, sum(r.points) as total, c.constructorNat, c.constructorName from drivers as d, results as r, constructors as c where d.driverId = r.driverId and r.constructorId = c.constructorId and c.constructorNat in ('British','American') group by d.driverName, d.driverSurName, c.constructorNat, c.constructorName order by 3 desc"

@volar.get("/")
def root():
    #print(dir(request))
    #return "Hola, soy DUILIO RESTUCCIA. Para probar mi trabajo DEBES ADICIONAR a la url -en la barra de direcciones - lo siguiente ===> '/api/pregN' (donde N =[1,2,3,4]) Ejm: 'https://35c5-190-234-57-194.sa.ngrok.io/api/preg4' "

        return templates.TemplateResponse("otro.html")


@volar.get("/dashboard/", response_class=HTMLResponse)
async def root(request:Request, hx_request:Optional[str] = Header(None) ):    
    with engine.connect() as conn:
        
        total_sumas= "SELECT sum(tot_people) as tot_pers, sum(tot_pass) as tot_pas, sum(tot_crew) as tot_crew, sum(tot_fat) as tot_fat, sum(pass_fat) as pas_fat, sum(crew_fat) as cre_fat FROM accidents "
        result_tipo_operador= "SELECT type_oper, count(type_oper) as tot_acc_operador FROM accidents group by type_oper "

        resulta = conn.execute(total_sumas).fetchall()
        tipo_operador = conn.execute(result_tipo_operador).fetchall()

    context = {'request':request,'suma_todo':resulta, 'tot_acc_operador':tipo_operador }
    if hx_request:
        
        return templates.TemplateResponse("estadisticas.html",context)
    
    return templates.TemplateResponse("dashboard.html", context)


@volar.get("/dataframes/")
#def dataframes(request:Request, files: list[UploadFile] ):
async def dataframes(request:Request, hx_request:Optional[str] = Header(None) ):    
    #dict_param_files =paramFiles()

    context = {'request':request}

    if hx_request:
        return templates.TemplateResponse("tbody-data-frames.html", context )
    return templates.TemplateResponse("ver_dataframes.html", context) #, 'data_Frames':dict_param_files

@volar.get("/productos/{IdSucursal}")
def pide(request:Request, IdSucursal):
    with engine.connect() as conn:
        duda= "SELECT s.Sucursal, s.Domicilio, p.Producto, p.IdTipoProducto, v.Precio FROM producto p, sucursal as s, venta as v WHERE p.IdProducto = v.IdProducto AND s.IdSucursal = v.IdSucursal AND v.IdSucursal = " + IdSucursal 
        
        resultado = conn.execute(duda).fetchall()
                
        return templates.TemplateResponse("ver_ventas_sucursal.html", {'request':request, 'produs':resultado})


@volar.get("/tdataframes")
def tdataframes(request:Request):

    context = {'request':request}
    return templates.TemplateResponse("tbody-data-frames.html", context ) #, 'data_Frames':dict_param_files

@volar.post("/subir")
async def create_upload_file( files: List[UploadFile] = File()):
    for file in files:
        try:
            [file.filename for file in files]
        except Exception:
            return {"message": "There was an error uploading the file(s)"}
        

        #context = {'request':request}
    return templates.TemplateResponse("ver_data-frames.html", {"filename": file.filename})


@volar.get("/selectFile")
def carga_data(request:Request):

    return templates.TemplateResponse("transform_df.html", {'request':request})

@volar.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile] ):
    return {"filenames": [file.filename for file in files]}

#@carga.get("/cesitar")
async def main(request:Request):

    context = {'request':request}
    
    return templates.TemplateResponse("ver_dataframes.html", context) #, 'data_Frames':dict_param_files


