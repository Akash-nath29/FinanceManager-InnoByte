import unittest
from budget import Budget
from user import User
from database import Database

class TestBudget(unittest.TestCase):
    def setUp(self):
        self.db = Database(':memory:')  # Use in-memory SQLite database for testing
        self.user_manager = User(self.db)
        self.user_manager.register('testuser', 'password123')
        self.user_manager.login('testuser', 'password123')
        self.budget_manager = Budget(self.db)

    def tearDown(self):
        self.db.close()  # Ensure the database is closed after each test

    def test_set_budget(self):
        self.budget_manager.set_budget('testuser', 'Groceries', 200)
        budgets = self.budget_manager.get_budgets('testuser')
        self.assertEqual(len(budgets), 1)
        self.assertEqual(budgets[0][0], 'Groceries')
        self.assertEqual(budgets[0][1], 200)

    def test_check_budget(self):
        self.budget_manager.set_budget('testuser', 'Groceries', 200)
        self.assertFalse(self.budget_manager.check_budget('testuser', 'Groceries', 150))
        self.assertTrue(self.budget_manager.check_budget('testuser', 'Groceries', 250))

if __name__ == '__main__':
    unittest.main()
