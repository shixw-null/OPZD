from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/test"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Инициализация базы данных.
    
    Подключается к базе данных и создает таблицы на основе определенных моделей.
    Если таблицы уже существуют, то они не будут пересозданы.
    """
    Base.metadata.create_all(bind=engine)