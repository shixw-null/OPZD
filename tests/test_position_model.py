import sys
sys.path.append("D:/Документы/Учеба/Учеба_5к1с/ОПЗБД/SQLAlchemy")

import unittest
from models.position import Position
from methods import BaseMethod
from database import SessionLocal, init_db

class TestPositionModel(unittest.TestCase):

    def setUp(self):
        init_db()
        self.session = SessionLocal()
        self.position_method = BaseMethod(self.session, Position)

    def test_get_position(self):
        # Тест получения должности по ID
        position = Position(position_name="Менеджер", salary=100000)
        self.position_method.save(position)
        retrieved_position = self.position_method.get(position.id)
        self.assertEqual(retrieved_position.position_name, "Менеджер")
        self.assertEqual(retrieved_position.salary, 100000)
        self.position_method.delete(position)

    def test_find_position(self):
        # Тест поиска должности по параметрам
        position = Position(position_name="Программист", salary=150000)
        self.position_method.save(position)
        found_positions = self.position_method.find(position_name="Программист")
        self.assertEqual(len(found_positions), 1)
        self.assertEqual(found_positions[0].salary, 150000)
        self.position_method.delete(position)

    def test_get_all_positions(self):
        # Тест получения всех должностей
        position_list = [
            Position(position_name="Аналитик", salary=120000),
            Position(position_name="Дизайнер", salary=80000),
            Position(position_name="Тестировщик", salary=90000),
        ]
        for position in position_list:
            self.position_method.save(position)
        all_positions = self.position_method.get_all()
        self.assertEqual(len(all_positions), len(position_list))
        for position in position_list:
            self.position_method.delete(position)

    def test_update_position(self):
        # Тест обновления информации о должности
        position = Position(position_name="Бухгалтер", salary=110000)
        self.position_method.save(position)
        position.salary = 115000
        self.position_method.save(position)
        updated_position = self.position_method.get(position.id)
        self.assertEqual(updated_position.salary, 115000)
        self.position_method.delete(position)

    def test_delete_position(self):
        # Тест удаления должности
        position = Position(position_name="Юрист", salary=130000)
        self.position_method.save(position)
        self.position_method.delete(position)
        deleted_position = self.position_method.get(position.id)
        self.assertIsNone(deleted_position)

    def tearDown(self):
        self.session.close()

if __name__ == '__main__':
    unittest.main()
