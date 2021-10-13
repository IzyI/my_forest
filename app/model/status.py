from db_sqlite.database import Table


class Status(Table):

    def __init__(self, db):
        super().__init__(
            db,
            'Status',
            [
                'name TEXT',
                'num_pin INTEGER',
                'status INTEGER',
                'cron TEXT',
                'lock INTEGER',
            ])

    def insert_pin_api(self, pin_api):
        for i in pin_api:
            self.insert(
                i['name'],
                i['num_pin'],
                0,
                i['cron'],
                0
            )

    def select_name(self, name):
        return self.select("*", name=name)
