import unittest
from comments import create_comment_table, validate_comment_data, add_comment, delete_comment, get_all_comments, get_comment_by_id, update_comment, get_comments_for_post

class TestCommentsFunctions(unittest.TestCase):

    def test_create_comment_table(self):
        # Проверяем, что функция создания таблицы не вызывает ошибок
        self.assertIsNone(create_comment_table())

    def test_validate_comment_data(self):
        # Проверяем валидные данные
        valid_text = "This is a valid comment."
        self.assertTrue(validate_comment_data(valid_text))

        # Проверяем невалидные данные
        invalid_text = ""
        self.assertFalse(validate_comment_data(invalid_text))

    def test_add_comment(self):
        # Предполагаем, что у нас есть пользователь с ID 1 и пост с ID 1
        text = "Test Comment"
        user_id = 1
        post_id = 1
        self.assertTrue(add_comment(text, user_id, post_id))

        # Проверяем добавление с невалидными данными
        invalid_text = ""
        self.assertFalse(add_comment(invalid_text, user_id, post_id))

    def test_delete_comment(self):
        # Предполагаем, что у нас есть комментарий с ID 1
        comment_id = 1
        self.assertIsNone(delete_comment(comment_id))

    def test_get_all_comments(self):
        # Проверяем, что функция получения всех комментариев не вызывает ошибок
        self.assertIsNotNone(get_all_comments())

    def test_get_comment_by_id(self):
        # Предполагаем, что у нас есть комментарий с ID 1
        comment_id = 1
        self.assertIsNotNone(get_comment_by_id(comment_id))

    def test_update_comment(self):
        # Предполагаем, что у нас есть комментарий с ID 1
        comment_id = 1
        new_text = "Updated Comment Text"
        self.assertTrue(update_comment(comment_id, new_text))

    def test_get_comments_for_post(self):
        # Предполагаем, что у нас есть пост с ID 1
        post_id = 1
        # Проверяем, что функция получения комментариев для поста не вызывает ошибок
        self.assertIsNotNone(get_comments_for_post(post_id))

if __name__ == '__main__':
    unittest.main()
