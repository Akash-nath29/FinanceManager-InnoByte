class Transaction:
    def __init__(self, db):
        self.db = db

    def add_transaction(self, user_id, type, category, amount, date):
        self.db.cursor.execute('''
            INSERT INTO transactions (user_id, type, category, amount, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, type, category, amount, date))
        self.db.conn.commit()

    def get_transactions(self, user_id):
        self.db.cursor.execute("SELECT * FROM transactions WHERE user_id = ?", (user_id,))
        return self.db.cursor.fetchall()

    def update_transaction(self, transaction_id, type, category, amount, date):
        self.db.cursor.execute('''
            UPDATE transactions
            SET type = ?, category = ?, amount = ?, date = ?
            WHERE id = ?
        ''', (type, category, amount, date, transaction_id))
        self.db.conn.commit()

    def delete_transaction(self, transaction_id):
        self.db.cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
        self.db.conn.commit()