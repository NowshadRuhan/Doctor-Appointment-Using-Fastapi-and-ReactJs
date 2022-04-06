from config.db import engine, meta, Base
from sqlalchemy import Column, Table, ForeignKey, DateTime
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.sql import func
from datetime import datetime

tbl_patients = Table('tbl_patients', meta, 
    Column('id', Integer, primary_key = True),
    Column('name', String(255)),
    Column('user_name',  String(255)),
    Column('email',  String(255)),
    Column('password',  String(255)),
    Column('status',  String(255)),
)


tbl_doctors = Table('tbl_doctors', meta, 
    Column('id', Integer, primary_key = True),
    Column('name', String(255)),
    Column('user_name',  String(255)),
    Column('email',  String(255)),
    Column('address',  String(255)),
    Column('password',  String(255)),
    Column('status',  String(255)),
)

# class Appoinment(Base):
#     __tablename__ = 'tbl_appoinment'
#     id = Column(Integer, primary_key=True)
#     patients_id = Column(Integer, ForeignKey('tbl_patients.id'))
#     doctor_id = Column(Integer, ForeignKey('tbl_doctors.id'))
#     appiontment_time = Column(DateTime)
#     time_created = Column(DateTime(timezone=True), server_default=func.now())

tbl_appoinment = Table('tbl_appoinment', meta, 
    Column('id', Integer, primary_key = True),
    Column('patients_id', Integer, ForeignKey('tbl_patients.id')),
    Column('doctor_id', Integer, ForeignKey('tbl_patients.id')),
    Column('appiontment_time', DateTime),
    Column('time_created', DateTime(timezone=True), server_default=func.now())
    
)

meta.create_all(engine)

