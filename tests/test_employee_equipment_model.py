import unittest
from models.employee_equipment import EmployeeEquipment
from models.employee import Employee
from models.equipment import Equipment
from methods import BaseMethod
from database import SessionLocal, init_db

class TestEmployeeEquipmentMethods(unittest.TestCase):

    def setUp(self):
        init_db()
        self.session = SessionLocal()
        self.emp_equip_method = BaseMethod(self.session, EmployeeEquipment)
        self.employee_method = BaseMethod(self.session, Employee)
        self.equipment_method = BaseMethod(self.session, Equipment)

    def test_get(self):
        employee = Employee(first_name="John Doe")
        equipment = Equipment(equipment_name="Компьютер")
        self.session.add(employee)
        self.session.add(equipment)
        self.session.commit()

        emp_equip = EmployeeEquipment(employee_id=employee.id, equipment_id=equipment.id)
        self.emp_equip_method.save(emp_equip)
        
        retrieved = self.emp_equip_method.get(emp_equip.id)
        self.assertEqual(emp_equip, retrieved)

    def test_find(self):
        employee = Employee(first_name="John Doe")
        equipment = Equipment(equipment_name="Мышь")
        self.session.add(employee)
        self.session.add(equipment)
        self.session.commit()

        emp_equip = EmployeeEquipment(employee_id=employee.id, equipment_id=equipment.id)
        self.emp_equip_method.save(emp_equip)

        results = self.emp_equip_method.find(employee_id=employee.id)
        self.assertIn(emp_equip, results)

    def test_get_all(self):
        employee = Employee(first_name="Jane Doe")
        equipment = Equipment(equipment_name="Монитор")
        self.session.add(employee)
        self.session.add(equipment)
        self.session.commit()

        emp_equip = EmployeeEquipment(employee_id=employee.id, equipment_id=equipment.id)
        self.emp_equip_method.save(emp_equip)
        
        all_records = self.emp_equip_method.get_all()
        self.assertIn(emp_equip, all_records)

    def test_save(self):
        employee = Employee(first_name="Jane Smith")
        equipment = Equipment(equipment_name="Клавиатура")
        self.session.add(employee)
        self.session.add(equipment)
        self.session.commit()

        emp_equip = EmployeeEquipment(employee_id=employee.id, equipment_id=equipment.id)
        self.emp_equip_method.save(emp_equip)
        
        saved_record = self.emp_equip_method.get(emp_equip.id)
        self.assertEqual(saved_record, emp_equip)

    def test_delete(self):
        employee = Employee(first_name="Mike Johnson")
        equipment = Equipment(equipment_name="Наушники")
        self.session.add(employee)
        self.session.add(equipment)
        self.session.commit()

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
