from ..transaction import Transaction
from ..database import Database as TestDataBase
def transaction():
    # Create a Transaction object with a mock database
    db = TestDataBase()
    return Transaction(db)

def test_add_transaction(transaction):
    # Test adding a transaction
    transaction.add_transaction(1, "expense", "food", 10.99, "2022-01-01")
    assert len(transaction.get_transactions(1)) == 1

def test_get_transactions(transaction):
    # Test getting transactions for a user
    transaction.add_transaction(1, "income", "salary", 1000.0, "2022-01-01")
    transaction.add_transaction(1, "expense", "rent", 500.0, "2022-01-02")
    transactions = transaction.get_transactions(1)
    assert len(transactions) == 2
    assert transactions[0]["type"] == "income"
    assert transactions[1]["type"] == "expense"

def test_update_transaction(transaction):
    # Test updating a transaction
    transaction.add_transaction(1, "expense", "food", 10.99, "2022-01-01")
    transactions = transaction.get_transactions(1)
    transaction_id = transactions[0]["id"]
    transaction.update_transaction(transaction_id, "expense", "shopping", 20.0, "2022-01-03")
    updated_transaction = transaction.get_transactions(1)[0]
    assert updated_transaction["category"] == "shopping"
    assert updated_transaction["amount"] == 20.0

def test_delete_transaction(transaction):
    # Test deleting a transaction
    transaction.add_transaction(1, "expense", "food", 10.99, "2022-01-01")
    transactions = transaction.get_transactions(1)
    transaction_id = transactions[0]["id"]
    transaction.delete_transaction(transaction_id)
    assert len(transaction.get_transactions(1)) == 0