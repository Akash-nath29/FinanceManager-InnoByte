from datetime import datetime

class Report:
    def __init__(self, db):
        self.db = db

    def generate_monthly_report(self, user_id, year, month):
        start_date = f"{year}-{month:02d}-01"
        end_date = f"{year}-{month:02d}-31"
        
        self.db.cursor.execute('''
            SELECT type, SUM(amount) as total
            FROM transactions
            WHERE user_id = ? AND date BETWEEN ? AND ?
            GROUP BY type
        ''', (user_id, start_date, end_date))
        
        results = self.db.cursor.fetchall()
        income = next((r[1] for r in results if r[0] == 'income'), 0)
        expenses = next((r[1] for r in results if r[0] == 'expense'), 0)
        savings = income - expenses
        
        return {
            'income': income,
            'expenses': expenses,
            'savings': savings
        }

    def generate_yearly_report(self, user_id, year):
        start_date = f"{year}-01-01"
        end_date = f"{year}-12-31"
        
        self.db.cursor.execute('''
            SELECT type, SUM(amount) as total
            FROM transactions
            WHERE user_id = ? AND date BETWEEN ? AND ?
            GROUP BY type
        ''', (user_id, start_date, end_date))
        
        results = self.db.cursor.fetchall()
        income = next((r[1] for r in results if r[0] == 'income'), 0)
        expenses = next((r[1] for r in results if r[0] == 'expense'), 0)
        savings = income - expenses
        
        return {
            'income': income,
            'expenses': expenses,
            'savings': savings
        }