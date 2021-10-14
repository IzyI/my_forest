import time
from typing import Any
from demon.pinapi import PinMachine
from fastapi import APIRouter
from db_sqlite import db, db_activity, DatabaseObject
from .model.status import Status
from .model.activity import Activity
from settings import DB_BACKUP
import datetime
from .schemas import NameLight, NameMotor, StatusList, NameAll
import asyncio

router = APIRouter()


def set_status(name, status):
    s = Status(db)
    s.update_status_name(name, status)
    s = Status(DatabaseObject(DB_BACKUP))
    s.update_status_name(name, status)


def set_activity(db, name, activ_string):
    act = Activity(db)
    act.create_table()
    act.insert(name, activ_string, datetime.datetime.now())


def set_lock(name, lock):
    s = Status(db)
    s.update_lock_name(name, lock)
    s = Status(DatabaseObject(DB_BACKUP))
    s.update_lock_name(name, lock)


@router.get("/on_lock")
def on_lock(name: NameAll) -> Any:
    set_lock(name, 1)
    set_activity(db_activity, name, f"Событие on_lock {name}")
    return {'result': True}


@router.get("/off_lock")
def on_lock(name: NameAll) -> Any:
    set_lock(name, 0)
    set_activity(db_activity, name, f"Событие on_lock {name}")
    return {'result': True}


@router.get("/on_light")
def on_light(name: NameLight) -> Any:
    set_status(name, 1)
    set_activity(db_activity, name, f"Событие on_light {name} 1, 1")
    return {'result': True}


@router.get("/off_light")
def off_light(name: NameLight) -> Any:
    set_status(name, 0)
    set_activity(db_activity, name, f"Событие off_light {name} 0, 0")
    return {'result': True}


@router.get("/on_motor")
def on_motor(name: NameMotor) -> Any:
    set_status(name, 1)
    set_activity(db_activity, name, f"Событие on_motor {name} 1, 1")
    return {'result': True}


@router.get("/off_motor")
def off_motor(name: NameMotor) -> Any:
    set_status(name, 0)
    set_activity(db_activity, name, f"Событие off_motor {name} 1, 1")
    return {'result': True}


@router.get("/on_time_motor")
def water_time_pin(name: NameMotor, tim: int) -> Any:
    set_status(name, 1)
    time.sleep(tim)
    set_status(name, 0)
    set_activity(db_activity, name, f"Событие on_time_motor {name} на время {tim}")
    return {'result': True}


@router.get("/status")
def status() -> Any:
    s = Status(db)
    status_list = s.select_all("*")
    status = []
    for i in status_list:
        status.append({
            "name": i[0],
            "status": i[2],
            "cron": i[3],
            "lock": i[4],
        })
    return {'result': True, "status": status}


@router.put("/status")
def status(st: StatusList) -> Any:
    s = Status(db)
    s.update_cron_name(st.name, st.cron, st.lock, st.status)
    s = Status(DatabaseObject(DB_BACKUP))
    s.update_cron_name(st.name, st.cron, st.lock, st.status)
    set_activity(db_activity, st.name, f"Событие put status {st.cron}")
    return {'result': True}
