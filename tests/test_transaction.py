from finance.transaction import Transaction
from finance.database import Database

def test_add_transaction() -> None:
    db = Database()
    transaction = Transaction(db)
    transaction.add_transaction(1, 'expense', 'food', 10.0, '2021-01-01')
    transactions = transaction.get_transactions(1)
    assert len(transactions) == 1
    
def test_get_transactions() -> None:
    db = Database()
    transaction = Transaction(db)
    transactions = transaction.get_transactions(1)
    assert len(transactions) == 1
    
def test_update_transaction() -> None:
    db = Database()
    transaction = Transaction(db)
    transaction.update_transaction(1, 'expense', 'food', 10.0, '2021-01-01')
    transactions = transaction.get_transactions(1)
    assert transactions[0][2] == 'expense'
    assert transactions[0][4] == 10.0
    assert transactions[0][5] == '2021-01-01'
    
def test_delete_transaction() -> None:
    db = Database()
    transaction = Transaction(db)
    transaction.delete_transaction(1)
    transactions = transaction.get_transactions(1)
    assert len(transactions) == 0
    