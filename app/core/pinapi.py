import time


class PinMachine:

    def __init__(self, num: int):
        self.pin = num

    def time_pin(self, t: int):
        print(f"time_pin  {t}")
        self.on_pin()
        time.sleep(t)
        self.off_pin()

    def off_pin(self):
        print(f"off_pin  {self.pin}")

    def on_pin(self):
        print(f"on_pin  {self.pin}")


if __name__ == "__main__":
    pm = PinMachine(1)
    pm.on_pin()
    pm.time_pin(2)
