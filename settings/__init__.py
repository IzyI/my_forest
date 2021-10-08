MOTOR1 = None
MOTOR2 = None
MOTOR3 = None
MOTOR4 = None
MOTOR5 = None
MOTOR6 = None
LIGHT1 = None
LIGHT2 = None
VERSION = "1.0.0"

try:
    from .local import *
except ImportError as e:
    pass
