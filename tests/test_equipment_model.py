import sys
sys.path.append("D:/Документы/Учеба/Учеба_5к1с/ОПЗБД/SQLAlchemy")

import unittest
from models.employee_equipment import EmployeeEquipment
from models.employee import Employee
from models.equipment import Equipment
from methods import BaseMethod
from database import SessionLocal, init_db

class TestEmployeeEquipmentModel(unittest.TestCase):

    def setUp(self):
        init_db()
        self.session = SessionLocal()
        self.emp_equip_method = BaseMethod(self.session, EmployeeEquipment)
        self.employee_method = BaseMethod(self.session, Employee)
        self.equipment_method = BaseMethod(self.session, Equipment)

    def test_get_existing_emp_equip(self):
        # Тест получения существующей связи сотрудника и оборудования по ID
        employee = Employee(first_name="John Doe")
        equipment = Equipment(equipment_name="Компьютер")
        self.employee_method.save(employee)
        self.equipment_method.save(equipment)
        emp_equip = EmployeeEquipment(employee_id=employee.id, equipment_id=equipment.id)
        self.emp_equip_method.save(emp_equip)

        retrieved = self.emp_equip_method.get(emp_equip.id)
        self.assertEqual(retrieved, emp_equip)

    def test_find_existing_emp_equip(self):
        # Тест поиска существующей связи сотрудника и оборудования по ID сотрудника
        employee = Employee(first_name="John Doe")
        equipment = Equipment(equipment_name="Мышь")
        self.employee_method.save(employee)
        self.equipment_method.save(equipment)

        emp_equip = EmployeeEquipment(employee_id=employee.id, equipment_id=equipment.id)
        self.emp_equip_method.save(emp_equip)

        results = self.emp_equip_method.find(employee_id=employee.id)
        self.assertIn(emp_equip, results)

    def test_get_all_emp_equip(self):
        # Тест получения всех связей сотрудника и оборудования
        employee = Employee(first_name="Jane Doe")
        equipment = Equipment(equipment_name="Монитор")
        self.employee_method.save(employee)
        self.equipment_method.save(equipment)

        emp_equip = EmployeeEquipment(employee_id=employee.id, equipment_id=equipment.id)
        self.emp_equip_method.save(emp_equip)

        all_records = self.emp_equip_method.get_all()
        self.assertIn(emp_equip, all_records)

    def test_update_emp_equip(self):
        # Тест обновления связи сотрудника и оборудования
        employee1 = Employee(first_name="Jane Smith")
        employee2 = Employee(first_name="Mike Johnson")
        equipment = Equipment(equipment_name="Клавиатура")
        self.employee_method.save(employee1)
        self.employee_method.save(employee2)
        self.equipment_method.save(equipment)

        emp_equip = EmployeeEquipment(employee_id=employee1.id, equipment_id=equipment.id)
        self.emp_equip_method.save(emp_equip)

        emp_equip.employee_id = employee2.id
        self.emp_equip_method.save(emp_equip)
        updated_record = self.emp_equip_method.get(emp_equip.id)
        self.assertEqual(updated_record.employee_id, employee2.id)

    def test_delete_existing_emp_equip(self):
        # Тест удаления существующей связи сотрудника и оборудования
        employee = Employee(first_name="Mike Johnson")
        equipment = Equipment(equipment_name="Наушники")
        self.employee_method.save(employee)
        self.equipment_method.save(equipment)

        emp_equip = EmployeeEquipment(employee_id=employee.id, equipment_id=equipment.id)
        self.emp_equip_method.save(emp_equip)

        self.emp_equip_method.delete(emp_equip)
        self.assertIsNone(self.emp_equip_method.get(emp_equip.id))

    def tearDown(self):
        self.session.query(EmployeeEquipment).delete()
        self.session.query(Employee).delete()
        self.session.query(Equipment).delete()
        self.session.commit()
        self.session.close()

if __name__ == '__main__':
    unittest.main()
