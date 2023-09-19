import unittest
from posts import create_post_table, add_post, get_post_by_id, delete_post, update_post, drop_post_table

class TestPostFunctions(unittest.TestCase):

    def test_add_post(self):
        create_post_table()
        # Проверка успешного добавления поста
        result = add_post("Заголовок", "Содержание", 1)  # 1 - это user_id, который существует
        self.assertTrue(result)  # Проверяем, что функция возвращает True
        drop_post_table()

    def test_get_post_by_id(self):
        create_post_table()
        # Проверка получения поста по ID после добавления
        add_post("Заголовок", "Содержание", 1)
        self.assertIsNotNone(get_post_by_id(1))  # Проверяем, что данные о посте не равны None
        drop_post_table()

    def test_delete_post(self):
        create_post_table()
        # Проверка успешного удаления поста
        add_post("Заголовок", "Содержание", 1)
        self.assertTrue(delete_post(1))  # Проверяем, что функция возвращает True
        drop_post_table()

    def test_update_post(self):
        create_post_table()
        # Проверка успешного обновления поста
        add_post("Заголовок", "Содержание", 1)
        self.assertTrue(update_post(1, "Новый заголовок", "Новое содержание"))  # Проверяем, что функция возвращает True
        drop_post_table()

if __name__ == '__main__':
    unittest.main()
