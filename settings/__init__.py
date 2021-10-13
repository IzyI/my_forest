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

DB = "./db"
DB_ACTIVITY = "./db_activity"
DB_BACKUP = "./db_backup"
COLOR_CONSOLE = True
LEVEL_LOG = logging.INFO

try:
    from .local import *
except ImportError as e:
    pass

PIN_API = [
    {"name": "MOTOR1", "num_pin": MOTOR1, "cron": '20:34/23:33/2,1,3'},
    {"name": "MOTOR2", "num_pin": MOTOR2, "cron": '20:34/22:30/2,1,3'},
    {"name": "MOTOR3", "num_pin": MOTOR3, "cron": '20:34/23:33/2,1,3'},
    {"name": "MOTOR4", "num_pin": MOTOR4, "cron": '20:34/22:30/2,1,3'},
    {"name": "MOTOR5", "num_pin": MOTOR5, "cron": '20:34/23:33/2,1,3'},
    {"name": "MOTOR6", "num_pin": MOTOR6, "cron": '20:34/23:59/2,1,3'},
    {"name": "LIGHT1", "num_pin": LIGHT1, "cron": '20:34/23:59/1,2,3,4,5,6,7'},
    {"name": "LIGHT2", "num_pin": LIGHT2, "cron": '20:34/23:59/0'}
]
