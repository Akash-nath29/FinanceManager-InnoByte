from finance.user import User
from finance.database import Database

def test_user_registration() -> None:
    db = Database()
    user = User(db)
    user.register('test_user', 'test_password')
    
def test_user_login() -> None:
    db = Database()
    user = User(db)
    assert user.login('test_user', 'test_password') == True
    assert user.login('test_user', 'wrong_password') == False
    assert user.login('wrong_user', 'test_password') == False
    assert user.login('wrong_user', 'wrong_password') == False