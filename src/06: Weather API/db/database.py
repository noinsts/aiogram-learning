import sqlite3


class Database:
    def __init__(self, db_name='database.db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()


    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cities (
                user_id INTEGER PRIMARY KEY, 
                city TEXT NOT NULL
            )"""
        )

        self.conn.commit()


    def get_city(self, user_id):
        self.cursor.execute("SELECT city FROM cities WHERE user_id = ?", (user_id, ))
        results = self.cursor.fetchone()
        return results


    def add_city(self, user_id, name):
        if self.get_city(user_id):
            self.cursor.execute("INSERT INTO cities (user_id, city) VALUES (?, ?)", (user_id, name))
            self.conn.commit()
            return True
        else:
            return False


    def close(self):
        self.conn.close()
