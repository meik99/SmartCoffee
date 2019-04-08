import RPi.GPIO as IO
import time as time

RELAY_GPIO = 18

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(RELAY_GPIO, IO.OUT)


class Tassimo:
    def make_coffee(self):
        IO.output(RELAY_GPIO, IO.HIGH)
        time.sleep(0.5)
        IO.output(RELAY_GPIO, IO.LOW)
        time.sleep(0.5)
