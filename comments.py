from database import connect_to_database
import psycopg2

# Функция для создания таблицы комментариев
def create_comment_table():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS comments (
                id serial PRIMARY KEY,
                text TEXT,
                user_id INTEGER REFERENCES users(id),
                post_id INTEGER REFERENCES posts(id)
            )
            """
            cursor.execute(create_table_query)
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except psycopg2.Error as e:
        print("Ошибка при создании таблицы комментариев:", e)

# Функция для валидации данных комментария перед добавлением или обновлением
def validate_comment_data(text):
    if not text:
        return False  # Если текст комментария пустой, возвращаем False
    return True  # Если данные прошли все проверки, возвращаем True

# Функция для добавления комментария
def add_comment(text, user_id, post_id):
    # Проверяем валидность данных перед добавлением
    if not validate_comment_data(text):
        return False  # Данные не прошли валидацию, не выполняем добавление

    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            insert_query = """
            INSERT INTO comments (text, user_id, post_id)
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (text, user_id, post_id))
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except psycopg2.Error as e:
        print("Ошибка при добавлении комментария:", e)
        return False  # Ошибка при добавлении

def delete_comment(comment_id):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            delete_query = "DELETE FROM comments WHERE id = %s"
            cursor.execute(delete_query, (comment_id,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except psycopg2.Error as e:
        print("Ошибка при удалении комментария:", e)

def get_all_comments():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            select_query = "SELECT * FROM comments"
            cursor.execute(select_query)
            comments = cursor.fetchall()
            cursor.close()
            conn.close()
            return comments
    except psycopg2.Error as e:
        print("Ошибка при получении всех комментариев:", e)

def get_comment_by_id(comment_id, fields=("id", "text")):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            select_query = "SELECT {} FROM comments WHERE id = %s".format(", ".join(fields))
            cursor.execute(select_query, (comment_id,))
            comment_data = cursor.fetchone()
            cursor.close()
            conn.close()
            return comment_data
    except psycopg2.Error as e:
        print("Ошибка при получении комментария по ID:", e)

def update_comment(comment_id, new_text):
    # Проверяем валидность данных перед обновлением
    if not validate_comment_data(new_text):
        return False  # Данные не прошли валидацию, не выполняем обновление

    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            update_query = """
            UPDATE comments
            SET text = %s
            WHERE id = %s
            """
            cursor.execute(update_query, (new_text, comment_id))
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except psycopg2.Error as e:
        print("Ошибка при обновлении информации о комментарями:", e)
        return False  # Ошибка при обновлении
        
# Функция для получения всех комментариев к посту 
def get_comments_for_post(post_id):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            select_query = f"SELECT * FROM comments WHERE post_id = %s"
            cursor.execute(select_query, (post_id,))
            comments = cursor.fetchall()
            cursor.close()
            conn.close()
            return comments
    except psycopg2.Error as e:
        print("Ошибка при получении комментариев:", e)
        
def get_comment_id_by_text_title_user(text, title, user_id):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            select_query = """
            SELECT c.id
            FROM comments c
            INNER JOIN posts p ON c.post_id = p.id
            INNER JOIN users u ON c.user_id = u.id
            WHERE c.text = %s AND p.title = %s AND u.id = %s
            """
            cursor.execute(select_query, (text, title, user_id))
            comment_id = cursor.fetchone()
            cursor.close()
            conn.close()
            return comment_id[0] if comment_id else None
    except psycopg2.Error as e:
        print("Ошибка при получении ID комментария:", e)
