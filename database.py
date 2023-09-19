import psycopg2

# Параметры подключения к базе данных PostgreSQL
db_params = {
    'dbname': 'test',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432',  # Порт PostgreSQL
}

# Функция для установления соединения с базой данных
def connect_to_database():
    try:
        conn = psycopg2.connect(**db_params)
        return conn
    except psycopg2.Error as e:
        print("Ошибка подключения к базе данных:", e)
        return None