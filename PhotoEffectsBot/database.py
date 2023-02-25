import datetime
import sqlite3 as sql


class MainDB:
    def __init__(self):
        self.con = sql.connect('bot.db')
        self.cur = self.con.cursor()

    def create_tables(self):
        with self.con:
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
                            user_id INT PRIMARY KEY,
                            username VARCHAR(100),
                            date VARCHAR(30)
                            )""")

            self.cur.execute("""CREATE TABLE IF NOT EXISTS effects(
                            effect_name VARCHAR(50),
                            effect VARCHAR(50)
                            )""")

    def add_user(self, user_id: int, username: str):
        today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        with self.con:
            user = self.cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
            if user is None:
                self.cur.execute("INSERT INTO users (user_id, username, date) VALUES (?, ?, ?)", (user_id, username, today))

    def get_all_effects(self):
        with self.con:
            effects = self.cur.execute("SELECT effect_name FROM effects").fetchall()
            return effects

    def get_effect(self, effect_name: str):
        with self.con:
            effect = self.cur.execute("SELECT effect FROM effects WHERE effect_name =?", (effect_name,)).fetchone()
            return effect

    def count_all_users(self):
        with self.con:
            total_users = self.cur.execute("SELECT count(*) FROM users").fetchone()
            return total_users[0]

    def count_users_date(self):
        with self.con:
            all_date = self.cur.execute("SELECT date FROM users").fetchall()
            hours = 0
            days = 0
            for date in all_date:
                now_date = datetime.datetime.now()
                date = datetime.datetime.strptime(date[0], "%Y-%m-%d %H:%M")
                now_time = datetime.datetime.now().strftime("%H")
                user_time = date.strftime("%H")
                date3_days = now_date - datetime.timedelta(days=3)
                if date > date3_days:
                    days += 1
                    if now_time == user_time:
                        hours += 1
            return days, hours
