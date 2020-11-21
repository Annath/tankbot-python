#!/usr/bin/env python

import signal
import sys
import time
import Adafruit_BBIO.PWM as PWM

m1a = "P8_13"
m1b = "P8_19"

m2a = "P9_14"
m2b = "P9_16"

motor_pins = [ m1a, m1b, m2a, m2b ]

def signal_handler(sig, frame):
    print('\nCaught SIGINT, stopping motors')

    for pin in motor_pins:
        PWM.stop(pin)

    PWM.cleanup()

    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for pin in motor_pins:
    PWM.start(pin, 0)

print("Starting both motors at 100%")
PWM.set_duty_cycle(m1b, 100)
PWM.set_duty_cycle(m2b, 100)

while True:
    time.sleep(0.2)
