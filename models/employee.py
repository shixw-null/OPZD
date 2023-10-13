from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Employee(Base):
    """
    Модель сотрудника.

    Описывает основную информацию о сотруднике, его должность и связь с другими сущностями.

    Атрибуты:
    - id: Уникальный идентификатор сотрудника.
    - first_name: Имя сотрудника.
    - last_name: Фамилия сотрудника.
    - middle_name: Отчество сотрудника.
    - phone: Номер телефона сотрудника.
    - position_id: Идентификатор должности сотрудника.
    - position: Связь с моделью должности.
    - time_tracks: Список отметок времени сотрудника.
    - equipments: Список оборудования, выданного сотруднику.
    """

    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String)
    phone = Column(String)
    position_id = Column(Integer, ForeignKey('positions.id'))
    position = relationship("Position", back_populates="employees")
    
    time_tracks = relationship("TimeTrack", back_populates="employee")
    equipments = relationship("EmployeeEquipment", back_populates="employee")
