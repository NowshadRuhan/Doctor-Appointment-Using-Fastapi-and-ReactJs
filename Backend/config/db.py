from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('mysql+pymysql://root:password@localhost:3005/doctors_appoinment')

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/doctors_appoinment"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

meta = MetaData()

conn = engine.connect()

Base = declarative_base()




