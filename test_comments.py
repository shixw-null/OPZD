import unittest
from comments import create_comment_table, validate_comment_data, add_comment, delete_comment, get_all_comments, get_comment_by_id, update_comment, get_comments_for_post, get_comment_id_by_text_title_user
import users
import posts

class TestCommentsFunctions(unittest.TestCase):

    def test_add_comment(self):
        users.add_user("john_doe", "john@example.com", "1990-01-15")
        user_id = users.get_user_id_by_username("john_doe")
        
        posts.add_post("Заголовок", "Содержание", user_id)
        post_id = posts.get_post_id_by_content_title_user_id("Заголовок", "Содержание", user_id)
        
        # Проверяем добавление с невалидными данными
        invalid_text = ""
        self.assertFalse(add_comment(invalid_text, user_id, post_id))
        
        # Проверяем добавление с валидными данными
        text = "Test Comment"
        
        self.assertTrue(add_comment(text, user_id, post_id))
        
        comment_id = get_comment_id_by_text_title_user(text, "Заголовок", user_id)
        
        delete_comment(comment_id)
        posts.delete_post(post_id)
        users.delete_user(user_id)


    def test_delete_comment(self):
        users.add_user("john_doe", "john@example.com", "1990-01-15")
        user_id = users.get_user_id_by_username("john_doe")
        
        posts.add_post("Заголовок", "Содержание", user_id)
        post_id = posts.get_post_id_by_content_title_user_id("Заголовок", "Содержание", user_id)
        
        text = "Test Comment"
        add_comment(text, user_id, post_id)
        
        comment_id = get_comment_id_by_text_title_user(text, "Заголовок", user_id)
        
        self.assertTrue(delete_comment(comment_id))
        
        delete_comment(comment_id)
        posts.delete_post(post_id)
        users.delete_user(user_id)

    def test_get_all_comments(self):
        # Проверяем, что функция получения всех комментариев не вызывает ошибок
        self.assertIsNotNone(get_all_comments())

    def test_get_comment_by_id(self):
        users.add_user("john_doe", "john@example.com", "1990-01-15")
        user_id = users.get_user_id_by_username("john_doe")
        
        posts.add_post("Заголовок", "Содержание", user_id)
        post_id = posts.get_post_id_by_content_title_user_id("Заголовок", "Содержание", user_id)
        
        text = "Test Comment"
        add_comment(text, user_id, post_id)
        
        comment_id = get_comment_id_by_text_title_user(text, "Заголовок", user_id)
        
        self.assertIsNotNone(get_comment_by_id(comment_id))
        
        delete_comment(comment_id)
        posts.delete_post(post_id)
        users.delete_user(user_id)

    def test_update_comment(self):
        users.add_user("john_doe", "john@example.com", "1990-01-15")
        user_id = users.get_user_id_by_username("john_doe")
        
        posts.add_post("Заголовок", "Содержание", user_id)
        post_id = posts.get_post_id_by_content_title_user_id("Заголовок", "Содержание", user_id)
        
        text = "Test Comment"
        add_comment(text, user_id, post_id)
        
        comment_id = get_comment_id_by_text_title_user(text, "Заголовок", user_id)
        
        new_text = "Updated Comment Text"
        self.assertTrue(update_comment(comment_id, new_text))
        
        delete_comment(comment_id)
        posts.delete_post(post_id)
        users.delete_user(user_id)

    def test_get_comments_for_post(self):
        users.add_user("john_doe", "john@example.com", "1990-01-15")
        user_id = users.get_user_id_by_username("john_doe")
        
        posts.add_post("Заголовок", "Содержание", user_id)
        post_id = posts.get_post_id_by_content_title_user_id("Заголовок", "Содержание", user_id)
        
        text = "Test Comment"
        add_comment(text, user_id, post_id)
        
        comment_id = get_comment_id_by_text_title_user(text, "Заголовок", user_id)
        
        # Проверяем, что функция получения комментариев для поста не вызывает ошибок
        self.assertIsNotNone(get_comments_for_post(post_id))
        
        delete_comment(comment_id)
        posts.delete_post(post_id)
        users.delete_user(user_id)

if __name__ == '__main__':
    unittest.main()
