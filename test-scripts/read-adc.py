#!/usr/bin/env python3

import signal
import sys
import time
import Adafruit_BBIO.ADC as ADC

pin = "P9_40"

def signal_handler(sig, frame):
    print('Caught SIGINT, stopping')

    sys.exit(0)

def read_adc(_pin):
    # According to the Adafurit documentation:
    # There is currently a bug in the ADC driver. You'll need to read the values twice in order to get the latest value.

    ADC.read(_pin)
    return ADC.read(_pin)

signal.signal(signal.SIGINT, signal_handler)
ADC.setup()

while True:
    mult = 9.2647
    raw = read_adc(pin)
    volts = raw * 1.8
    vbat = volts * mult

    print(f"mult = {mult}")
    print(f"raw = {volts}, Vbat = {vbat}")

    time.sleep(0.2)
