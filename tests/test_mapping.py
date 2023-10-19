import sys
sys.path.append("D:/Документы/Учеба/Учеба_5к1с/ОПЗБД/SQLAlchemy")

import unittest
from sqlalchemy.inspection import inspect
from models.employee_equipment import EmployeeEquipment
from models.employee import Employee
from models.equipment import Equipment
from models.position import Position
from models.time_track import TimeTrack
from database import SessionLocal, init_db
from methods import BaseMethod

class TestTableMapping(unittest.TestCase):
    
    def setUp(self):
        init_db()
        self.session = SessionLocal()

    def test_employee_equipment_table_mapping(self):
        employee_equipment_mapper = inspect(EmployeeEquipment)
        self.assertEqual(employee_equipment_mapper.local_table.name, "employee_equipments")

    def test_employee_table_mapping(self):
        employee_mapper = inspect(Employee)
        self.assertEqual(employee_mapper.local_table.name, "employees")

    def test_equipment_table_mapping(self):
        equipment_mapper = inspect(Equipment)
        self.assertEqual(equipment_mapper.local_table.name, "equipments")

    def test_position_table_mapping(self):
        position_mapper = inspect(Position)
        self.assertEqual(position_mapper.local_table.name, "positions")

    def test_time_track_table_mapping(self):
        time_track_mapper = inspect(TimeTrack)
        self.assertEqual(time_track_mapper.local_table.name, "time_tracks")

    def tearDown(self):
        self.session.close()

if __name__ == '__main__':
    unittest.main()
