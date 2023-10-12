from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class EmployeeEquipment(Base):
    """
    Модель для связи между сотрудниками и оборудованием.

    Отражает, какое оборудование выдано каждому сотруднику.

    Атрибуты:
    - id: Уникальный идентификатор записи.
    - employee_id: Идентификатор сотрудника.
    - equipment_id: Идентификатор оборудования.
    - employee: Связь с моделью сотрудника.
    - equipment: Связь с моделью оборудования.
    """

    __tablename__ = 'employee_equipments'
    
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    equipment_id = Column(Integer, ForeignKey('equipments.id'))
    
    employee = relationship("Employee", back_populates="equipments")
    equipment = relationship("Equipment", back_populates="employees")
