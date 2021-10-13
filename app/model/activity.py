from db_sqlite.database import Table


class Activity(Table):

    def __init__(self, db):
        super().__init__(
            db,
            'Activity',
            [
                'name TEXT',
                'info TEXT',
                'date DATE'
            ])
