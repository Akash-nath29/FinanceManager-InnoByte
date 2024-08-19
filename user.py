import hashlib
import sqlite3

class User:
    def __init__(self, db):
        self.db = db

    def register(self, username, password):
        hashed_password = self._hash_password(password)
        try:
            self.db.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            self.db.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def login(self, username, password):
        hashed_password = self._hash_password(password)
        self.db.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
        user = self.db.cursor.fetchone()
        return user is not None

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()