import sqlite3 as sql


class Database:
    def __init__(self):
        self.con = sql.connect('bot.db')
        self.cur = self.con.cursor()

    def create_tables(self):
        with self.con:
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
                            user_id INT PRIMARY KEY,
                            username TEXT,
                            language TEXT DEFAULT 'uz')""")

    def add_user(self, user_id, username):
        with self.con:
            if not self.cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone():
                self.cur.execute(
                    "INSERT INTO users (user_id, username) VALUES (?, ?)", (user_id, username))

    def get_all_users(self):
        with self.con:
            users = self.cur.execute("SELECT * FROM users").fetchall()
            return users

    def update_user_lang(self, user_id, lang):
        with self.con:
            self.cur.execute("UPDATE users SET language = ? WHERE user_id = ?", (lang, user_id))

    def get_user_info(self, user_id):
        with self.con:
            user = self.cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
            return user



