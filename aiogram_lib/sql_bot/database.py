import sqlite3 as sql


class Database:
    def __init__(self):
        self.con = sql.connect('bot.db')
        self.cur = self.con.cursor()

    def create_tables(self):
        with self.con:
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
                            user_id INT,
                            username TEXT,
                            language TEXT DEFAULT 'uz')""")

    def add_user(self, user_id, username):
        with self.con:
            self.cur.execute(
                "INSERT INTO users (user_id, username) VALUES (?, ?)", (user_id, username))


