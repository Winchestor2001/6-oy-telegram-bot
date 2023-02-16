import sqlite3 as sql


class MainDB:
    def __init__(self):
        self.con = sql.connect('fsm.db')
        self.cur = self.con.cursor()

    def create_tables(self):
        with self.con:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY,
                            first_name VARCHAR(50) NULL,
                            gander VARCHAR(20) NULL,
                            phone_number VARCHAR(20) NULL,
                            avatar TEXT NULL
                            )''')

    def save_user(self, user_id):
        with self.con:
            if not self.con.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone():
                self.cur.execute('''INSERT INTO users (user_id) VALUES (?)''', (user_id,))

    def save_user_data(self, user_id, data, img):
        with self.con:
            self.cur.execute("""
            UPDATE users 
            SET first_name = ?, gander = ?, phone_number = ?, avatar = ? 
            WHERE user_id = ?
            """, (data['ism'], data['gander'], data['phone'], img, user_id))

