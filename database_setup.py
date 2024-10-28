from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import postgresql
from datetime import datetime
from config import DB_HOST, DB_NAME, DB_USER, DB_PASS, DB_PORT

# Define the PostgreSQL connection details
# To Do: Setup md5 authentication on the Postgresql Server. The below URI will then work
#DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
DATABASE_URI = f'postgresql+psycopg2://postgres@{DB_HOST}:{DB_PORT}/{DB_NAME}' #Works when pg_hba.conf is set to trust 

# Define a base class for declarative class definitions
# Any class that inherits from Base will automatically gain SQLAlchemy’s ORM  (Object-Relational Mapping) 
# capabilities and will be linked to the database schema.
Base = declarative_base()

# Define the new table as a Python class
class TestTable(Base):
    __tablename__ = 'test_table'
    __table_args__ = {'schema': 'public'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    event_datetime = Column(DateTime, nullable=False)
    zone = Column(String(50), nullable=False)
    carbonIntensity = Column(Float, nullable=False)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    createdAt = Column(DateTime, default=datetime.utcnow)
    emissionFactoryType = Column(String(50), nullable=True)
    isEstimated = Column(Boolean, nullable=False)
    estimationMethod = Column(String(100), nullable=True)

# Create the SQLAlchemy engine
try:
    engine = create_engine(DATABASE_URI)
except Exception as e:
    print("Error: ", e)
   

# Create the table in the database
Base.metadata.create_all(engine)

print("Table created successfully.")