#!/usr/bin/env python

import signal
import sys
import time
import Adafruit_BBIO.PWM as PWM

m1a = "P8_19"
m1b = "P8_13"

m2a = "P9_14"
m2b = "P9_16"

motor_pins = [ m1a, m1b, m2a, m2b ]

def set_motors(left, right):
    if left > 0:
        PWM.set_duty_cycle(m1a, left)
        PWM.set_duty_cycle(m1b, 0)
    elif left < 0:
        PWM.set_duty_cycle(m1a, 0)
        PWM.set_duty_cycle(m1b, -left)
    else:
        PWM.set_duty_cycle(m1a, 0)
        PWM.set_duty_cycle(m1b, 0)

    if right > 0:
        PWM.set_duty_cycle(m2a, right)
        PWM.set_duty_cycle(m2b, 0)
    elif right < 0:
        PWM.set_duty_cycle(m2a, 0)
        PWM.set_duty_cycle(m2b, -right)
    else:
        PWM.set_duty_cycle(m2a, 0)
        PWM.set_duty_cycle(m2b, 0)

def finish():
    for pin in motor_pins:
        PWM.stop(pin)

    PWM.cleanup()

    sys.exit(0)

def signal_handler(sig, frame):
    print('\nCaught SIGINT, stopping motors')

    finish()

def setup():
    signal.signal(signal.SIGINT, signal_handler)

    for pin in motor_pins:
        PWM.start(pin, 0)
