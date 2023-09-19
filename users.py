from database import connect_to_database
import re
import psycopg2

# Функция для создания таблицы пользователей
def create_user_table():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id serial PRIMARY KEY,
                username VARCHAR (50) UNIQUE NOT NULL,
                email VARCHAR (100) UNIQUE NOT NULL,
                birthdate DATE
            )
            """
            cursor.execute(create_table_query)
            conn.commit()
            cursor.close()
            conn.close()
    except psycopg2.Error as e:
        print("Ошибка при создании таблицы пользователей:", e)
        
# Функция для валидации данных пользователя перед добавлением
def validate_user_data(username, email, birthdate):
    if not username or not email or not birthdate:
        return False  # Если хотя бы одно из полей пусто, возвращаем False

    # Проверка формата email
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_pattern, email):
        return False

    # Проверка формата даты рождения (пример: "YYYY-MM-DD")
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(date_pattern, birthdate):
        return False

    return True  # Если данные прошли все проверки, возвращаем True

# Функция для добавления пользователя
def add_user(username, email, birthdate):
    # Проверяем валидность данных перед добавлением
    if not validate_user_data(username, email, birthdate):
        return False  # Данные не прошли валидацию, не выполняем добавление

    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            insert_query = """
            INSERT INTO users (username, email, birthdate)
            VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (username, email, birthdate))
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except psycopg2.Error as e:
        print("Ошибка при добавлении пользователя:", e)
        return False  # Ошибка при добавлении

def delete_user(user_id):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            delete_query = "DELETE FROM users WHERE id = %s"
            cursor.execute(delete_query, (user_id,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except psycopg2.Error as e:
        print("Ошибка при удалении пользователя:", e)

def get_all_users():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            select_query = "SELECT * FROM users"
            cursor.execute(select_query)
            users = cursor.fetchall()
            cursor.close()
            conn.close()
            return users
    except psycopg2.Error as e:
        print("Ошибка при получении всех пользователей:", e)

def get_user_by_id(user_id, fields=("id", "username")):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            select_query = "SELECT {} FROM users WHERE id = %s".format(", ".join(fields))
            cursor.execute(select_query, (user_id,))
            user_data = cursor.fetchone()
            cursor.close()
            conn.close()
            return user_data
    except psycopg2.Error as e:
        print("Ошибка при получении пользователя по ID:", e)

def update_user(user_id, new_username, new_email, new_birthdate):
    # Проверяем валидность данных перед обновлением
    if not validate_user_data(new_username, new_email, new_birthdate):
        return False  # Данные не прошли валидацию, не выполняем обновление

    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            update_query = """
            UPDATE users
            SET username = %s, email = %s, birthdate = %s
            WHERE id = %s
            """
            cursor.execute(update_query, (new_username, new_email, new_birthdate, user_id))
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except psycopg2.Error as e:
        print("Ошибка при обновлении информации о пользователе:", e)
        return False  # Ошибка при обновлении

        
# Функция для получения всех пользователей с сортировкой по имени (по умолчанию по возрастанию)
def get_all_users_sort(order_by="username ASC"):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            select_query = f"SELECT * FROM users ORDER BY {order_by}"
            cursor.execute(select_query)
            users = cursor.fetchall()
            cursor.close()
            conn.close()
            return users
    except psycopg2.Error as e:
        print("Ошибка при получении пользователей:", e)     

def drop_user_table():
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            drop_table_query = "DROP TABLE IF EXISTS users CASCADE"
            cursor.execute(drop_table_query)
            conn.commit()
            cursor.close()
            conn.close()
            return True
    except psycopg2.Error as e:
        print("Ошибка при удалении таблицы пользователей:", e)
  
def get_user_id_by_username(username):
    try:
        conn = connect_to_database()
        if conn:
            cursor = conn.cursor()
            select_query = "SELECT id FROM users WHERE username = %s"
            cursor.execute(select_query, (username,))
            user_id = cursor.fetchone()
            cursor.close()
            conn.close()
            return user_id[0] if user_id else None
    except psycopg2.Error as e:
        print("Ошибка при получении ID пользователя по имени:", e)
