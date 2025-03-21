import sqlite3


class Database:
    def __init__(self, db_name='database.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS todoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Унікальний ID для кожного запису
            user_id INTEGER NOT NULL,              -- ID користувача
            name TEXT NOT NULL UNIQUE              -- Назва завдання (унікальна)
        )
        """)
        self.conn.commit()

    def add_todo(self, user_id, name):
        self.cursor.execute("INSERT INTO todoes (user_id, name) VALUES (?, ?) ON CONFLICT(name) DO NOTHING", (user_id, name))
        self.conn.commit()

    def get_todoes(self, user_id):
        self.cursor.execute("SELECT name FROM todoes WHERE user_id = ?", (user_id, ))
        todos = [row[0] for row in self.cursor.fetchall()]  # Список назв завдань
        return "Ваші завдання:\n" + ",\n".join(todos) if todos else "Завдань поки що немає"

    def close(self):
        self.conn.close()