import sqlite3 as sql


class MainDB:
    def __init__(self):
        self.con = sql.connect('fsm.db')
        self.cur = self.con.cursor()

    def create_tables(self):
        with self.con:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY,
                            first_name VARCHAR(50),
                            gander VARCHAR(20),
                            phone_number VARCHAR(20),
                            avatar TEXT
                            )''')

