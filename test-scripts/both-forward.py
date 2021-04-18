#!/usr/bin/env python

import common
import time

common.setup()

common.set_motors(100, 100)

while True:
    time.sleep(0.1)

common.finish()
