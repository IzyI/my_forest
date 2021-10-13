import sqlite3

queries = {
    'SELECT': 'SELECT %s FROM %s WHERE %s',
    'SELECT_ALL': 'SELECT %s FROM %s',
    'INSERT': 'INSERT INTO %s VALUES(%s)',
    'UPDATE': 'UPDATE %s SET %s WHERE %s',
    'DELETE': 'DELETE FROM %s where %s',
    'DELETE_ALL': 'DELETE FROM %s',
    'CREATE_TABLE': 'CREATE TABLE IF NOT EXISTS %s(%s)',
    'DROP_TABLE': 'DROP TABLE %s'}


class DatabaseObject(object):

    def __init__(self, db_name):
        self.db = sqlite3.connect(db_name, check_same_thread=False, timeout=10)
        self.db_name = db_name

    def backup(self, dest):
        self.db.backup(dest.db)

    @classmethod
    def free(cls, cursor):
        cursor.close()

    def write(self, query, values=None):
        cursor = self.db.cursor()
        if values is not None:
            cursor.execute(query, list(values))
        else:
            cursor.execute(query)
        self.db.commit()
        return cursor

    def read(self, query, values=None):
        cursor = self.db.cursor()
        if values is not None:
            cursor.execute(query, list(values))
        else:
            cursor.execute(query)
        return cursor

    def select(self, tables, *args, **kwargs):
        vals = ','.join([l for l in args])
        locs = ','.join(tables)
        conds = ' and '.join(['%s=?' % k for k in kwargs])
        subs = [kwargs[k] for k in kwargs]
        query = queries['SELECT'] % (vals, locs, conds)
        return self.read(query, subs)

    def select_all(self, tables, *args):
        vals = ','.join([l for l in args])
        locs = ','.join(tables)
        query = queries['SELECT_ALL'] % (vals, locs)
        return self.read(query)

    def insert(self, table_name, *args):
        values = ','.join(['?' for l in args])
        query = queries['INSERT'] % (table_name, values)
        return self.write(query, args)

    def update(self, table_name, set_args, **kwargs):
        updates = ','.join(['%s=?' % k for k in set_args])
        conds = ' and '.join(['%s=?' % k for k in kwargs])
        vals = [set_args[k] for k in set_args]
        subs = [kwargs[k] for k in kwargs]
        query = queries['UPDATE'] % (table_name, updates, conds)
        return self.write(query, vals + subs)

    def delete(self, table_name, **kwargs):
        conds = ' and '.join(['%s=?' % k for k in kwargs])
        subs = [kwargs[k] for k in kwargs]
        query = queries['DELETE'] % (table_name, conds)
        return self.write(query, subs)

    def delete_all(self, table_name):
        query = queries['DELETE_ALL'] % table_name
        return self.write(query)

    def create_table(self, table_name, values):
        query = queries['CREATE_TABLE'] % (table_name, ','.join(values))
        return self.write(query)

    def drop_table(self, table_name):
        query = queries['DROP_TABLE'] % table_name
        return self.write(query)

    def disconnect(self):
        self.db.close()

    def reconnect(self):
        self.free()
        self.db.close()


class Table:
    def __init__(self, db, table_name, values):
        self.db = db
        self.table_name = table_name
        self.values = values

    def create_table(self):
        self.db.free(self.db.create_table(self.table_name, self.values))

    def select(self, *args, **kwargs):
        cursor = self.db.select([self.table_name], *args, **kwargs)
        results = cursor.fetchall()
        cursor.close()
        return results

    def select_all(self, *args):
        cursor = self.db.select_all([self.table_name], *args)
        results = cursor.fetchall()
        cursor.close()
        return results

    def insert(self, *args):
        self.db.free(self.db.insert(self.table_name, *args))

    def update(self, set_args, **kwargs):
        self.db.free(self.db.update(self.table_name, set_args, **kwargs))

    def delete(self, **kwargs):
        self.db.free(self.db.delete(self.table_name, **kwargs))

    def delete_all(self, **kwargs):
        self.db.free(self.db.delete_all(self.table_name))

    def drop(self):
        self.db.free(self.db.drop_table(self.table_name))
