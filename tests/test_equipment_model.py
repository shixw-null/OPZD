### Для корректного импорта ###
import sys
sys.path.append("D:/Документы/Учеба/Учеба_5к1с/ОПЗБД/SQLAlchemy")

import unittest
from models.equipment import Equipment
from methods import BaseMethod
from database import SessionLocal, init_db

class TestEquipmentModel(unittest.TestCase):

    def setUp(self):
        init_db()
        self.session = SessionLocal()
        self.equipment_method = BaseMethod(self.session, Equipment)

    def test_get_existing_equipment(self):
        # Тест получения существующего оборудования по ID
        equipment = Equipment(equipment_name="Компьютер")
        self.equipment_method.save(equipment)
        retrieved_equipment = self.equipment_method.get(equipment.id)
        self.assertEqual(retrieved_equipment.equipment_name, "Компьютер")
        self.equipment_method.delete(equipment)

    def test_find_existing_equipment(self):
        # Тест поиска существующего оборудования по названию
        equipment = Equipment(equipment_name="Проектор")
        self.equipment_method.save(equipment)
        found_equipment = self.equipment_method.find(equipment_name="Проектор")
        self.assertEqual(len(found_equipment), 1)
        self.assertEqual(found_equipment[0].equipment_name, "Проектор")
        self.equipment_method.delete(equipment)

    def test_get_all_equipment(self):
        # Тест получения всех оборудования
        equipment_list = [
            Equipment(equipment_name="Монитор"),
            Equipment(equipment_name="Принтер"),
            Equipment(equipment_name="Сканер"),
        ]
        for equipment in equipment_list:
            self.equipment_method.save(equipment)
        all_equipment = self.equipment_method.get_all()
        self.assertEqual(len(all_equipment), len(equipment_list))
        for equipment in equipment_list:
            self.equipment_method.delete(equipment)

    def test_update_equipment(self):
        # Тест обновления информации об оборудовании
        equipment = Equipment(equipment_name="Ноутбук")
        self.equipment_method.save(equipment)
        equipment.equipment_name = "Планшет"
        self.equipment_method.save(equipment)
        updated_equipment = self.equipment_method.get(equipment.id)
        self.assertEqual(updated_equipment.equipment_name, "Планшет")
        self.equipment_method.delete(equipment)

    def test_delete_existing_equipment(self):
        # Тест удаления существующего оборудования
        equipment = Equipment(equipment_name="Мышь")
        self.equipment_method.save(equipment)
        self.equipment_method.delete(equipment)
        deleted_equipment = self.equipment_method.get(equipment.id)
        self.assertIsNone(deleted_equipment)

    def tearDown(self):
        self.session.close()

if __name__ == '__main__':
    unittest.main()
