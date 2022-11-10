from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float, Date
from config.db2 import engine, meta_data

sucursal = Table('sucursal', meta_data, 
                Column('suc_id', String(15), primary_key=True),
                Column('comercio_id', String(5), nullable=False ),
                Column('bandera_id', String(5), nullable=False),
                Column('bandera_descr', String(55), nullable=False),
                Column('comercio_raz_soc', String(155), nullable=False),
                Column('provincia', String(15), nullable=False),
                Column('suc_localidad', String(55), nullable=False),
                Column('suc_direcc', String(155), nullable=False),
                Column('suc_latitud', String(15), nullable=False),
                Column('suc_longitud', String(15), nullable=False),
                Column('suc_nombre', String(155), nullable=False),
                Column('suc_tipo', String(25), nullable=False),
                Column('fecha_carga', Date, nullable=False)
                )
meta_data.create_all(engine)