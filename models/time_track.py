from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class TimeTrack(Base):
    """
    Модель учета рабочего времени сотрудника.

    Описывает количество отработанных часов конкретным сотрудником.

    Атрибуты:
    - id: Уникальный идентификатор записи.
    - employee_id: Идентификатор сотрудника.
    - worked_hours: Количество отработанных часов.
    - employee: Связь с моделью сотрудника.
    """

    __tablename__ = 'time_tracks'
    
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    worked_hours = Column(Integer)
    
    employee = relationship("Employee", back_populates="time_tracks")
