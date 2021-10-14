from settings import DB, DB_BACKUP, DB_ACTIVITY
import os
import sys
from demon.pinapi import BoardMachine

status_pin = sys.argv[1]
if status_pin:
    BoardMachine.set_config_board()
    BoardMachine.all_pin_low()
else:
    BoardMachine.set_config_board()
    BoardMachine.all_pin_high()
