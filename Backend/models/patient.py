from config.db import engine, meta
from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String

tbl_patients = Table('tbl_patients', meta, 
    Column('id', Integer, primary_key = True),
    Column('name', String(255)),
    Column('user_name',  String(255)),
    Column('email',  String(255)),
    Column('password',  String(255)),
    Column('status',  String(255)),
)

meta.create_all(engine)

