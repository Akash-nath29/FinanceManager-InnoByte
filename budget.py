class Budget:
    def __init__(self, db):
        self.db = db

    def set_budget(self, user_id, category, amount):
        self.db.cursor.execute('''
            INSERT OR REPLACE INTO budgets (user_id, category, amount)
            VALUES (?, ?, ?)
        ''', (user_id, category, amount))
        self.db.conn.commit()

    def get_budgets(self, user_id):
        self.db.cursor.execute("SELECT category, amount FROM budgets WHERE user_id = ?", (user_id,))
        return self.db.cursor.fetchall()

    def check_budget(self, user_id, category, amount):
        self.db.cursor.execute('''
            SELECT amount FROM budgets
            WHERE user_id = ? AND category = ?
        ''', (user_id, category))
        budget = self.db.cursor.fetchone()
        
        if budget:
            return amount > budget[0]
        return False