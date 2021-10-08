import time

import OPi.GPIO as GPIO
from yaml import Loader, load
from time import sleep
import time

# with open("./config.yaml") as f:
#     config = load(f, Loader=Loader)

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
#
# try:
#     while True:
#         if GPIO.input(21):
#             print('IO12 = HIGH')
#             GPIO.output(21, GPIO.LOW)
#         else:
#             print('IO12 = LOW')
#             GPIO.output(21, GPIO.HIGH)
#         sleep(1)
# except KeyboardInterrupt:
#     GPIO.cleanup()
#
#
# GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
# GPIO.output(12, GPIO.HIGH)
if GPIO.input(12):
    print('Input was HIGH')
else:
    print('Input was LOW')
# time.sleep(5)
# GPIO.output(12, GPIO.LOW)
# if GPIO.input(12):
#     print('Input was HIGH')
# else:
#     print('Input was LOW')