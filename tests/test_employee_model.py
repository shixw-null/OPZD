import sys
sys.path.append("D:/Документы/Учеба/Учеба_5к1с/ОПЗБД/SQLAlchemy")

import unittest
from models.employee import Employee
from methods import BaseMethod
from database import SessionLocal, init_db

class TestEmployeeModel(unittest.TestCase):

    def setUp(self):
        init_db()
        self.session = SessionLocal()
        self.employee_method = BaseMethod(self.session, Employee)

    def test_get_existing_employee(self):
        # Тест получения существующего сотрудника по ID
        employee = Employee(first_name="Иван", last_name="Иванов", phone="+79123456789")
        self.employee_method.save(employee)
        retrieved_employee = self.employee_method.get(employee.id)
        self.assertEqual(retrieved_employee.first_name, "Иван")

    def test_find_existing_employee(self):
        # Тест поиска существующего сотрудника по имени
        employee = Employee(first_name="Анна", last_name="Сергеева", phone="+79123456789")
        self.employee_method.save(employee)
        employees = self.employee_method.find(first_name="Анна")
        self.assertEqual(len(employees), 1)
        self.assertEqual(employees[0].last_name, "Сергеева")

    def test_get_all_employees(self):
        # Тест получения всех сотрудников
        employees = [
            Employee(first_name="Иван", last_name="Иванов", phone="+79123456789"),
            Employee(first_name="Петр", last_name="Петров", phone="+79123456789"),
            Employee(first_name="Анна", last_name="Сергеева", phone="+79123456789"),
        ]
        for employee in employees:
            self.employee_method.save(employee)
        all_employees = self.employee_method.get_all()
        self.assertEqual(len(all_employees), 3)

    def test_update_employee(self):
        # Тест обновления сотрудника
        employee = Employee(first_name="Олег", last_name="Олегов", phone="+79123456789")
        self.employee_method.save(employee)
        employee.first_name = "Новое имя"
        self.employee_method.save(employee)
        updated_employee = self.employee_method.get(employee.id)
        self.assertEqual(updated_employee.first_name, "Новое имя")

    def test_delete_existing_employee(self):
        # Тест удаления существующего сотрудника
        employee = Employee(first_name="Иван", last_name="Иванов", phone="+79123456789")
        self.employee_method.save(employee)
        self.employee_method.delete(employee)
        deleted_employee = self.employee_method.get(employee.id)
        self.assertIsNone(deleted_employee)

    def tearDown(self):
        self.session.query(Employee).delete()
        self.session.commit()
        self.session.close()

if __name__ == '__main__':
    unittest.main()
