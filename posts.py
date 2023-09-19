from database import connect_to_database
import psycopg2

# Функция для создания таблицы постов
def create_post_table():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS posts (
                id serial PRIMARY KEY,
                title VARCHAR (100),
                content TEXT,
                user_id INTEGER REFERENCES users(id)
            )
            """
            cursor.execute(create_table_query)
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except psycopg2.Error as e:
        print("Ошибка при создании таблицы постов:", e)
        
# Функция для валидации данных поста перед добавлением
def validate_post_data(title, content):
    if not title or not content:
        return False  # Если хотя бы одно из полей пусто, возвращаем False
    return True  # Если данные прошли все проверки, возвращаем True

# Функция для добавления поста
def add_post(title, content, user_id):
    # Проверяем валидность данных перед добавлением
    if not validate_post_data(title, content):
        return False  # Данные не прошли валидацию, не выполняем добавление

    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            insert_query = """
            INSERT INTO posts (title, content, user_id)
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (title, content, user_id))
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except psycopg2.Error as e:
        print("Ошибка при добавлении поста:", e)
        return False  # Ошибка при добавлении


def delete_post(post_id):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            delete_query = "DELETE FROM posts WHERE id = %s"
            cursor.execute(delete_query, (post_id,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except psycopg2.Error as e:
        print("Ошибка при удалении поста:", e)

def get_all_posts():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            select_query = "SELECT * FROM posts"
            cursor.execute(select_query)
            posts = cursor.fetchall()
            cursor.close()
            conn.close()
            return posts
    except psycopg2.Error as e:
        print("Ошибка при получении всех постов:", e)

def get_post_by_id(post_id, fields=("id", "title")):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            select_query = "SELECT {} FROM posts WHERE id = %s".format(", ".join(fields))
            cursor.execute(select_query, (post_id,))
            post_data = cursor.fetchone()
            cursor.close()
            conn.close()
            return post_data
    except psycopg2.Error as e:
        print("Ошибка при получении поста по ID:", e)

def update_post(post_id, new_title, new_content):
    # Проверяем валидность данных перед обновлением
    if not validate_post_data(new_title, new_content):
        return False  # Данные не прошли валидацию, не выполняем обновление

    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            update_query = """
            UPDATE posts
            SET title = %s, content = %s
            WHERE id = %s
            """
            cursor.execute(update_query, (new_title, new_content, post_id))
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except psycopg2.Error as e:
        print("Ошибка при обновлении информации о посте:", e)
        return False  # Ошибка при обновлении
        
# Функция для получения всех постов с сортировкой по дате публикации (по умолчанию по возрастанию)
def get_all_posts_sort(order_by="ASC"):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            select_query = f"SELECT * FROM posts ORDER BY {order_by}"
            cursor.execute(select_query)
            posts = cursor.fetchall()
            cursor.close()
            conn.close()
            return posts
    except psycopg2.Error as e:
        print("Ошибка при получении постов:", e)
        
def drop_post_table():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            drop_table_query = "DROP TABLE IF EXISTS posts CASCADE"
            cursor.execute(drop_table_query)
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except psycopg2.Error as e:
        print("Ошибка при удалении таблицы постов:", e)
        
def get_post_id_by_content_title_user_id(title, content, user_id):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            select_query = """
            SELECT id FROM posts
            WHERE content = %s AND title = %s AND user_id = %s
            """
            cursor.execute(select_query, (content, title, user_id))
            post_id = cursor.fetchone()
            cursor.close()
            conn.close()
            return post_id[0] if post_id else None
    except psycopg2.Error as e:
        print("Ошибка при получении ID поста:", e)

