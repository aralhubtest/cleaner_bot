import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()


# Создание таблицы users, если она еще не существует
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL
    );
"""
)


# Сохранение изменений (коммит)
conn.commit()
print("Таблица 'users' успешно создана (или уже существовала).")
conn.close()
