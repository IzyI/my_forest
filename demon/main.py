import os

import settings
from logger.main import alog
import time
from .pinapi import PinMachine, BoardMachine
from app.model.user import User
from app.model.status import Status
from app.model.activity import Activity
from db_sqlite import db, db_activity, DatabaseObject
from settings import DB_BACKUP
import datetime

class Demon:

    def __init__(self):
        self.db_backup = None

    @classmethod
    def set_activity(cls, name, result):
        act = Activity(db_activity)
        act.create_table()
        r1 = "HIGH" if result[1] else "LOW"
        r2 = "HIGH" if result[2] else "LOW"
        result = f"Произошла смена {r1}({result[1]})  на {r2}({result[2]})"
        act.insert(name, result, datetime.datetime.now())

    @classmethod
    def check_status(cls):
        s = Status(db)
        list_status = s.select_all("*")
        for i in list_status:
            pin = PinMachine(i[0])
            if i[-1]:  # lock
                result = pin.check_pin(i[2])
            else:
                result = pin.check_cron(i[3])
            if result[0]:
                cls.set_activity(i[0], result)

    def backup_reset_fill(self):
        """Сбрасываем бекап бд"""
        if os.path.exists(DB_BACKUP):
            os.remove(DB_BACKUP)
        self.db_backup = DatabaseObject(DB_BACKUP)
        s = Status(self.db_backup)
        s.create_table()
        s.insert_pin_api(settings.PIN_API)

    def db_backup_db(self):
        """Делаем бекап из db_backup в db"""
        self.db_backup.backup(db)
        self.db_backup.disconnect()
        self.db_backup = None

    def db_fill_from_backup(self):
        """Заполняем бд  из -> бекапа или из -> настроек -> бекап"""
        if os.path.exists(DB_BACKUP):
            self.db_backup = DatabaseObject(DB_BACKUP)
        else:
            self.backup_reset_fill()
        self.db_backup_db()

    def run(self):
        BoardMachine.set_config_board()
        BoardMachine.all_pin_low()
        self.db_fill_from_backup()
        while True:
            self.check_status()
            time.sleep(2)
            # try:
            #     self.check_status()
            #     time.sleep(2)
            # except Exception:
            #     import traceback
            #     alog.critical(f"Exception {traceback.format_exc()}")
            #     exit()
