import logging

MOTOR1 = None
MOTOR2 = None
MOTOR3 = None
MOTOR4 = None
MOTOR5 = None
MOTOR6 = None
LIGHT1 = None
LIGHT2 = None
VERSION = "1.0.0"

DB = "/dev/shm/db"
DB_ACTIVITY = "./db_activity"
DB_BACKUP = "./db_backup"

COLOR_CONSOLE = True
LEVEL_LOG = logging.INFO
PATH_LOG = "logs/alog.log"

USERNAME = "natasha"
PASSWORD = "ob8y8n9&F*&%Dpf[b09899&^%FD7v[b98hb6705E($976yb[9"
try:
    from .local import *
except ImportError as e:
    pass

PIN_API = [
    {"name": "MOTOR1", "num_pin": MOTOR1, "cron": '20:00/23:00/1,2,3,4,5,6,7'},
    {"name": "MOTOR2", "num_pin": MOTOR2, "cron": '20:00/23:00/1,2,3,4,5,6,7'},
    {"name": "MOTOR3", "num_pin": MOTOR3, "cron": '20:00/23:00/1,2,3,4,5,6,7'},
    {"name": "MOTOR4", "num_pin": MOTOR4, "cron": '20:00/23:00/1,2,3,4,5,6,7'},
    {"name": "MOTOR5", "num_pin": MOTOR5, "cron": '20:00/23:00/1,2,3,4,5,6,7'},
    {"name": "MOTOR6", "num_pin": MOTOR6, "cron": '20:00/23:00/1,2,3,4,5,6,7'},
    {"name": "LIGHT1", "num_pin": LIGHT1, "cron": '20:00/23:00/1,2,3,4,5,6,7'},
    {"name": "LIGHT2", "num_pin": LIGHT2, "cron": '20:00/23:00/1,2,3,4,5,6,7'}
]
