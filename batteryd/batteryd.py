#!/usr/bin/env python3

import os
import syslog
import signal
import sys
import time
import Adafruit_BBIO.ADC as ADC
from daemonize import Daemonize

def signal_handler(sig, frame):
    daemon.exit()

def send_alarm():
    # TODO send alarm to mqtt
    pass

def power_down():
    # TODO: pulse power pin?
    pass

def read_adc(pin):
    # According to the Adafurit documentation:
    # There is currently a bug in the ADC driver. You'll need to read the values twice in order to get the latest value.
    ADC.read(pin)
    return ADC.read(pin)

def read_battery_voltage(pin, multiplier):
    raw = read_adc(pin)
    volts = raw * 1.8
    return volts * multiplier

def main():
    # TODO: move all this into a config file
    sleep_time = 5 * 60
    low_battery_threshold = 12.3
    critical_battery_threshold = 12.2 # 3 * 3.85 # we're using a 3s battery, looking for a cell voltage of less than 3.85
    pin = "P9_40"
    r1 = 7.85
    r2 = 0.987
    multiplier = ((r1 + r2) / r2)

    ADC.setup()

    while True:
        v = read_battery_voltage(pin, multiplier)
        print(v)
        syslog.syslog(syslog.LOG_INFO, f'Battery voltage = {v:.2f}')

        if v <= low_battery_threshold:
            syslog.syslog(syslog.LOG_WARN, f'Battery voltage is below alarm threshold ({low_battery_threshold:.2f}), sending alarm')
            send_alarm()

        if v <= critical_battery_threshold:
            syslog.syslog(syslog.LOG_ERR, f'Battery voltage is below shutdown threshold ({critical_battery_threshold:.2f}), shutting down')
            power_down()
            break
        
        time.sleep(sleep_time)

    daemon.exit()

pid = "/var/run/tankbot-batteryd.pid"
daemon = Daemonize(app="tankbot-batteryd", pid=pid, action=main)
daemon.start()