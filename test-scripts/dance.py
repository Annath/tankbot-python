#!/usr/bin/env python

import common
import time

common.setup()

print("Moving forward 5 seconds")

common.set_motors(100, 100)

time.sleep(5)

print("Spinning left 3 seconds")

common.set_motors(-100, 100)

time.sleep(3)

print("Spinning right 3 seconds")

common.set_motors(100, -100)

time.sleep(3)

print("Reversing 3 second")

common.set_motors(-100, -100)

time.sleep(3)

print("Wide right arc for 10 seconds")

common.set_motors(100, 90)

time.sleep(10)

common.finish()
