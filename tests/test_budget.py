from finance.budget import Budget
from finance.database import Database

def test_set_budget() -> None:
    db = Database()
    budget = Budget(db)
    budget.set_budget(1, 'food', 100.0)
    budgets = budget.get_budgets(1)
    # assert len(budgets) == 3
    assert budgets[0][0] == 'food'
    assert budgets[0][1] == 100.0
    
def test_get_budgets() -> None:
    db = Database()
    budget = Budget(db)
    budgets = budget.get_budgets(1)
    # assert len(budgets) == 3
    assert budgets[0][0] == 'food'
    assert budgets[0][1] == 100.0
    
def test_check_budget() -> None:
    db = Database()
    budget = Budget(db)
    budget.set_budget(1, 'food', 100.0)
    assert budget.check_budget(1, 'food', 50.0) == False
    assert budget.check_budget(1, 'food', 150.0) == True
    assert budget.check_budget(1, 'entertainment', 50.0) == False
    assert budget.check_budget(2, 'food', 50.0) == False
    assert budget.check_budget(2, 'entertainment', 50.0) == False
    assert budget.check_budget(2, 'entertainment', 150.0) == False
    assert budget.check_budget(1, 'food', 100.0) == False
    assert budget.check_budget(1, 'food', 0.0) == False
    assert budget.check_budget(1, 'food', -50.0) == False
    assert budget.check_budget(1, 'food', 100.1) == True
    assert budget.check_budget(1, 'food', 99.9) == False
    assert budget.check_budget(1, 'food', 100.00000000000001) == True