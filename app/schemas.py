from pydantic import BaseModel, constr
from enum import Enum


class NameLight(str, Enum):
    light1 = "LIGHT1"
    light2 = "LIGHT2"


class NameMotor(str, Enum):
    motor1 = "MOTOR1"
    motor2 = "MOTOR2"
    motor3 = "MOTOR3"
    motor4 = "MOTOR4"
    motor5 = "MOTOR5"
    motor6 = "MOTOR6"


class NameAll(str, Enum):
    motor1 = "MOTOR1"
    motor2 = "MOTOR2"
    motor3 = "MOTOR3"
    motor4 = "MOTOR4"
    motor5 = "MOTOR5"
    motor6 = "MOTOR6"
    light1 = "LIGHT1"
    light2 = "LIGHT2"

class StatusList(BaseModel):
    name: str
    cron: constr(regex=r'\d{,2}:\d{,2}/\d{,2}:\d{,2}/[\d,]{,13}$')
    lock: int
    status: int
