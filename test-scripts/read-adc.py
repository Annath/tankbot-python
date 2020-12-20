#!/usr/bin/env python3

import signal
import sys
import time
import Adafruit_BBIO.ADC as ADC

pin = "P9_40"
r1 = 7.85
r2 = 0.987

def signal_handler(sig, frame):
    print('')

    sys.exit(0)

def read_adc(_pin):
    # According to the Adafurit documentation:
    # There is currently a bug in the ADC driver. You'll need to read the values twice in order to get the latest value.

    ADC.read(_pin)
    return ADC.read(_pin)

signal.signal(signal.SIGINT, signal_handler)
ADC.setup()

mult = ((r1 + r2) / r2)
raw = read_adc(pin)
volts = raw * 1.8
vbat = volts * mult

print("r1 = {:.3f} kOhm".format(r1))
print("r2 = {:.3f} kOhm".format(r2))
print("multiplier = {:.4f}\n".format(mult))
print("adc = {:.4f} V, Vbat = {:.4f} V".format(volts, vbat))

