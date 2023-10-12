from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from .base import Base


class Position(Base):
    """
    Модель должности сотрудника.

    Описывает основную информацию о должности, включая зарплату и связанных с этой должностью сотрудников.

    Атрибуты:
    - id: Уникальный идентификатор должности.
    - position_name: Название должности (уникальное).
    - salary: Зарплата, связанная с этой должностью.
    - employees: Список сотрудников, занимающих эту должность.
    """

    __tablename__ = 'positions'
    
    id = Column(Integer, primary_key=True, index=True)
    position_name = Column(String, unique=True)
    salary = Column(Float)
    
    employees = relationship("Employee", back_populates="position")
