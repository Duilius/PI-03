from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float, Date
from config.db2 import engine, meta_data

precios = Table('precios', meta_data, 
                Column('clave', String(55), primary_key=True),
                Column('precio', Float, nullable=False ),
                Column('cod_prod', String(13), nullable=False),
                Column('cod_suc', String(25), nullable=False),
                Column('fecha_precio', Date, nullable=False),
                Column('fecha_carga', Date, nullable=False)
                )
meta_data.create_all(engine)