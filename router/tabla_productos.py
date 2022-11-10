from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float, Date
from traitlets import default
from config.db2 import engine, meta_data

productos = Table('productos', meta_data, 
                Column('cod_prod', String(13), primary_key=True, nullable=False),
                Column('marca_prod', String(55), nullable=False, default='sin marca' ),
                Column('nombre_prod', String(155), nullable=False),
                Column('presentac_prod', String(15), nullable=False),
                Column('categ1_prod', String(55)),
                Column('categ2_prod', String(55)),
                Column('categ3_prod', String(55)),
                Column('fecha_carga', Date, nullable=False)
                )
meta_data.create_all(engine)