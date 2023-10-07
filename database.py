from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Employee, Position, TimeTrack, Equipment, EmployeeEquipment

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/test"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Пытаемся подключиться к БД и создать таблицы
    Base.metadata.create_all(bind=engine)