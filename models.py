from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True, index=True)  # Добавлен столбец id как первичный ключ
    position_name = Column(String, unique=True)  # Уникальное название должности
    salary = Column(Float)
    employees = relationship("Employee", back_populates="position")

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String)
    phone = Column(String)
    position_id = Column(Integer, ForeignKey('positions.id'))  # Изменено на position_id
    position = relationship("Position", back_populates="employees")
    
    time_tracks = relationship("TimeTrack", back_populates="employee")
    
    equipments = relationship("EmployeeEquipment", back_populates="employee")


class TimeTrack(Base):
    __tablename__ = 'time_tracks'
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    worked_hours = Column(Integer)
    
    employee = relationship("Employee", back_populates="time_tracks")

class Equipment(Base):
    __tablename__ = 'equipments'
    id = Column(Integer, primary_key=True)
    equipment_name = Column(String)
    
    employees = relationship("EmployeeEquipment", back_populates="equipment")

class EmployeeEquipment(Base):
    __tablename__ = 'employee_equipments'
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    equipment_id = Column(Integer, ForeignKey('equipments.id'))

    employee = relationship("Employee", back_populates="equipments")
    equipment = relationship("Equipment", back_populates="employees")
