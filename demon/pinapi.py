import OPi.GPIO as GPIO
from settings import PIN_API
from logger.main import alog
import datetime as dt


class BoardMachine:

    @classmethod
    def set_config_board(cls):
        GPIO.setmode(GPIO.BOARD)
        for i in PIN_API:
            GPIO.setup(i["num_pin"], GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)

    @classmethod
    def all_pin_high(cls):
        for i in PIN_API:
            GPIO.output(i["num_pin"], GPIO.HIGH)
            alog.info(f'Pin high {i["name"]} ')

    @classmethod
    def all_pin_low(cls):
        for i in PIN_API:
            GPIO.output(i["num_pin"], GPIO.LOW)
            alog.info(f'Pin low {i["name"]} ')

    @classmethod
    def all_status_pin(self):
        result = PIN_API.copy()
        for i in result:
            GPIO.output(i["num_pin"], GPIO.LOW)
            if GPIO.input(12):
                alog.info(f'Pin status {i["name"]} HIGH')
                i['status'] = True
            else:
                alog.info(f'Pin status {i["name"]} LOW')
                i['status'] = False
        return result


class PinMachine:

    def __init__(self, name: str):
        self.num_pin = None
        self.name = name
        self.get_pin()
        if not self.name:
            return

    def __str__(self):
        return f"Pin {self.name} num_pin {self.num_pin}"

    def off_pin(self):
        GPIO.output(self.num_pin, GPIO.LOW)
        if GPIO.input(self.num_pin):
            return False
        else:
            return True

    def on_pin(self):
        GPIO.output(self.num_pin, GPIO.HIGH)
        if GPIO.input(self.num_pin):
            return True
        else:
            return False

    def get_status(self):
        if GPIO.input(self.num_pin):
            return 1
        else:
            return 0

    def set_status(self, status):
        if status == 1:
            self.on_pin()
        else:
            self.off_pin()

    def check_pin(self, status):
        old_status = self.get_status()
        if not status == old_status:
            self.set_status(status)
            return True, old_status, status
        return False, old_status, status,

    @classmethod
    def cron_parser(cls, c):
        print(c)
        tim1, tim2, week_list = c.split('/')
        week_list = [int(i) for i in week_list.split(",")]
        if 0 in week_list:
            return False
        hour1, min1 = tim1.split(":")
        tim1 = dt.datetime.now().replace(hour=int(hour1), minute=int(min1), second=0, microsecond=0)
        hour2, min2 = tim2.split(":")
        tim2 = dt.datetime.now().replace(hour=int(hour2), minute=int(min2), second=0, microsecond=0)

        if tim1 <= dt.datetime.now() <= tim2:
            if dt.datetime.now().isoweekday() in week_list:
                return True
            else:
                return False
        else:
            return False

    def check_cron(self, cron):
        old_status = self.get_status()
        if self.cron_parser(cron):
            if old_status == 0:
                self.set_status(1)
                return True, old_status, 1
        else:
            if old_status == 1:
                self.set_status(0)
                return True, old_status, 0
        return False, 0, 0

    def get_pin(self):
        for i in PIN_API:
            if self.name == i['name']:
                self.num_pin = i['num_pin']
                return True
        self.name = None
        return False


if __name__ == "__main__":
    ...
