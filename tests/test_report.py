import unittest
from report import Report
from database import Database
from user import User
from transaction import Transaction

class TestReport(unittest.TestCase):
    def setUp(self):
        self.db = Database(':memory:')
        self.user_manager = User(self.db)
        self.user_manager.register('testuser', 'password123')
        self.user_manager.login('testuser', 'password123')
        self.transaction_manager = Transaction(self.db)
        self.report_manager = Report(self.db)

    def tearDown(self):
        self.db.close()

    def test_generate_report(self):
        self.transaction_manager.add_transaction('testuser', 'Income', 1000)
        self.transaction_manager.add_transaction('testuser', 'Groceries', -200)
        report = self.report_manager.generate_report('testuser')
        self.assertEqual(report['total_income'], 1000)
        self.assertEqual(report['total_expense'], -200)
        self.assertEqual(report['balance'], 800)

if __name__ == '__main__':
    unittest.main()
