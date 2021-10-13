from db_sqlite.database import Table
from settings import PIN_API

class User(Table):

    def __init__(self, db):
        super().__init__(db, 'users',
                         ['username TEXT', 'password TEXT'])


