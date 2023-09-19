import unittest
from posts import create_post_table, add_post, get_post_by_id, delete_post, update_post, drop_post_table, get_post_id_by_content_title_user_id
import users

class TestPostFunctions(unittest.TestCase):

    def test_add_post(self):
        # Проверка успешного добавления поста
        users.add_user("john_doe", "john@example.com", "1990-01-15")
        user_id = users.get_user_id_by_username("john_doe")
        result = add_post("Заголовок", "Содержание", user_id)
        self.assertTrue(result)  # Проверяем, что функция возвращает True
        
        delete_post(get_post_id_by_content_title_user_id("Заголовок", "Содержание", user_id))
        users.delete_user(user_id)

    def test_get_post_by_id(self):
        # Проверка получения поста по ID после добавления
        users.add_user("john_doe", "john@example.com", "1990-01-15")
        user_id = users.get_user_id_by_username("john_doe")
        add_post("Заголовок", "Содержание", user_id)
        self.assertIsNotNone(get_post_id_by_content_title_user_id("Заголовок", "Содержание", user_id))  # Проверяем, что данные о посте не равны None
        
        delete_post(get_post_id_by_content_title_user_id("Заголовок", "Содержание", user_id))
        users.delete_user(user_id)

    def test_delete_post(self):
        # Проверка успешного удаления поста
        users.add_user("john_doe", "john@example.com", "1990-01-15")
        user_id = users.get_user_id_by_username("john_doe")
        add_post("Заголовок", "Содержание", user_id)
        self.assertTrue(delete_post(get_post_id_by_content_title_user_id("Заголовок", "Содержание", user_id)))  # Проверяем, что функция возвращает True
        
        delete_post(get_post_id_by_content_title_user_id("Заголовок", "Содержание", user_id))
        users.delete_user(user_id)
        
    def test_update_post(self):
        # Проверка успешного обновления поста
        users.add_user("john_doe", "john@example.com", "1990-01-15")
        user_id = users.get_user_id_by_username("john_doe")
        add_post("Заголовок", "Содержание", user_id)
        post_id = get_post_id_by_content_title_user_id("Заголовок", "Содержание", user_id)
        
        self.assertTrue(update_post(post_id, "Новый заголовок", "Новое содержание"))  # Проверяем, что функция возвращает True
        
        delete_post(get_post_id_by_content_title_user_id("Новый заголовок", "Новое содержание", user_id))
        users.delete_user(user_id)
        
if __name__ == '__main__':
    unittest.main()
