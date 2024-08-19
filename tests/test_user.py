from ..database import Database
from ..user import User

def test_user_register():
    db = Database(':memory:')
    user_manager = User(db)
    user_manager.register('testuser', 'password123')
    assert user_manager.register('testuser', 'password123') == True
    db.close()
    
def test_user_login():
    db = Database(':memory:')
    user_manager = User(db)
    user_manager.register('testuser', 'password123')
    assert user_manager.login('testuser', 'password123') == True
    db.close()