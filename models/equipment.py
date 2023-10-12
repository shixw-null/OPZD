from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .base import Base


class Equipment(Base):
    """
    Модель оборудования.

    Описывает основную информацию о единице оборудования и связь с сотрудниками, которым это оборудование выдано.

    Атрибуты:
    - id: Уникальный идентификатор оборудования.
    - equipment_name: Название оборудования.
    - employees: Список сотрудников, которым выдано данное оборудование.
    """

    __tablename__ = 'equipments'
    
    id = Column(Integer, primary_key=True)
    equipment_name = Column(String)
    
    employees = relationship("EmployeeEquipment", back_populates="equipment")
