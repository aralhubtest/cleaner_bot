import sqlite3

conn = sqlite3.connect("utils/database/mydatabase.db")
cursor = conn.cursor()


def add_to_user(username, email):
    cursor.execute(
        "INSERT INTO users (username, email) VALUES (?, ?)", (username, email)
    )
    conn.commit()

def get_user_by_username(username):
    cursor.execute("SELECT * FROM users WHERE username =?", (username,))
    row = cursor.fetchone()
    return row

# # Вставка одной записи
# cursor.execute(
#     "INSERT INTO users (username, email) VALUES (?, ?)", ("alice", "alice@example.com")
# )
# # Вставка нескольких записей с помощью executemany()
# users_to_insert = [("bob", "bob@example.com"), ("charlie", "charlie@example.com")]

# cursor.executemany("INSERT INTO users (username, email) VALUES (?, ?)", users_to_insert)

# conn.commit()

# print(get_user_by_username('kamall'))

# print("Данные успешно вставлены.")
# conn.close()
