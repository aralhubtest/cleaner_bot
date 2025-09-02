import sqlite3

from .schema import User, Chat, Message


class SqlLite:
    def __init__(self):
        self.conn = sqlite3.connect("data/mydatabase.db")
        self.cursor = self.conn.cursor()

    def create_db(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,              
                first_name TEXT NOT NULL,
                last_name TEXT,
                username TEXT
            );"""
        )
        self.cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY,              
                title TEXT NOT NULL,
                type TEXT,                           
                username TEXT,
                is_forum BOOLEAN
            );"""
        )

        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY,             
                user_id INTEGER NOT NULL,            
                group_id INTEGER,                    
                text TEXT,
                is_file BOOLEAN,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (group_id) REFERENCES groups (id)
            );"""
        )

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message_id INTEGER NOT NULL,        
                type TEXT,                           
                file_id TEXT,                        
                FOREIGN KEY (message_id) REFERENCES messages (id)
            );
        """
        )
        self.conn.commit()

    def add_to_user(self, user: User):
        self.cursor.execute(
            "INSERT INTO users (id, first_name, last_name, username) VALUES (?, ?, ?, ?)",
            (user.id, user.first_name, user.last_name, user.username),
        )
        self.conn.commit()

    def add_to_chat(self, chat: Chat):
        self.cursor.execute(
            "INSERT INTO groups (id, type, title, username, is_forum) VALUES (?, ?, ?, ?, ?)",
            (chat.id, chat.type, chat.title, chat.username, False),
        )
        self.conn.commit()

    def create_message(self, message: Message):
        self.cursor.execute(
            "INSERT INTO messages (id, user_id, group_id, text, is_file) VALUES (?, ?, ?, ?, ?)",
            (message.id, message.user_id, message.group_id, message.text, message.is_file),
        )
        self.conn.commit()


    def check_group(self, id: int):
        self.cursor.execute("SELECT id FROM groups WHERE id =?", (id,))
        row = self.cursor.fetchone()
        return row

    def get_messages(self):
        self.cursor.execute("SELECT id, group_id, text FROM messages ")
        row = self.cursor.fetchall()
        return row

    def get_user_by_id(self, user_id):
        self.cursor.execute("SELECT id FROM users WHERE id =?", (user_id,))
        row = self.cursor.fetchone()
        return row

    def get_user_by_username(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username =?", (username,))
        row = self.cursor.fetchone()
        return row

    def down(self):
        self.conn.close()
