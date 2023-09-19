import unittest
from users import create_user_table, add_user, delete_user, get_all_users, get_user_by_id, update_user, drop_user_table, get_user_id_by_username

class TestUserFunctions(unittest.TestCase):

    def test_add_user(self):
        result = add_user("TestUser", "test@example.com", "2000-01-01")
        self.assertIsNotNone(result)  # Пользователь был успешно добавлен
        
        delete_user(get_user_id_by_username("TestUser"))
        
    def test_delete_user(self):
        # Проверяем, что удаление пользователя работает корректно
        # Предварительно добавляем пользователя для удаления
        add_user("TestUser", "test@example.com", "2000-01-01")
        result = delete_user(1)  # Удаляем пользователя с ID=1
        self.assertTrue(result)  # Пользователь был успешно удален
        
        delete_user(get_user_id_by_username("TestUser"))

    def test_get_all_users(self):
        # Проверяем, что получение всех пользователей работает корректно
        # Предварительно добавляем несколько пользователей
        add_user("User1", "user1@example.com", "2000-01-01")
        add_user("User2", "user2@example.com", "2000-01-02")
        users = get_all_users()
        self.assertEqual(len(users), 2)  # Должно быть два пользователя в списке
        
        delete_user(get_user_id_by_username("User1"))
        delete_user(get_user_id_by_username("User2"))

    def test_get_user_by_id(self):
        # Проверяем, что получение пользователя по ID работает корректно
        # Предварительно добавляем пользователя
        add_user("TestUser", "test@example.com", "2000-01-01")
        user = get_user_by_id(get_user_id_by_username("TestUser"))
        self.assertIsNotNone(user)  # Пользователь был найден
        self.assertEqual(user[1], "TestUser")  # Имя пользователя соответствует ожиданиям
        
        delete_user(get_user_id_by_username("TestUser"))
        
    def test_update_user(self):
        # Проверяем, что обновление информации о пользователе работает корректно
        # Предварительно добавляем пользователя
        add_user("TestUser", "test@example.com", "2000-01-01")
        result = update_user(1, "UpdatedUser", "updated@example.com", "2001-01-01")
        self.assertIsNotNone(result)  # Пользователь был успешно обновлен
        
        delete_user(get_user_id_by_username("TestUser"))
        
if __name__ == '__main__':
    unittest.main()
