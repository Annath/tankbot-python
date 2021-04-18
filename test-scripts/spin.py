#!/usr/bin/env python

import common
import time

common.setup()

common.set_motors(100, -100)

time.sleep(3)

common.finish()
