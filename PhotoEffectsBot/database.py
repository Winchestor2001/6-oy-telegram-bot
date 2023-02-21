import sqlite3 as sql


class MainDB:
    def __init__(self):
        self.con = sql.connect('bot.db')
        self.cur = self.con.cursor()

    def create_tables(self):
        with self.con:
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
                            user_id INT PRIMARY KEY,
                            username VARCHAR(100)
                            )""")

            self.cur.execute("""CREATE TABLE IF NOT EXISTS effects(
                            effect_name VARCHAR(50),
                            effect VARCHAR(50)
                            )""")

    def add_user(self, user_id: int, username: str):
        with self.con:
            user = self.cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
            if user is None:
                self.cur.execute("INSERT INTO users (user_id, username) VALUES (?, ?)", (user_id, username))

    def get_all_effects(self):
        with self.con:
            effects = self.cur.execute("SELECT effect_name FROM effects").fetchall()
            return effects
