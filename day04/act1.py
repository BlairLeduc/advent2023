# Activity 1: Segment test

# Imports
from machine import Pin
import time

# Pin definitions
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# Turn on each segment in turn
seg1.value(1)
time.sleep(0.5)

seg2.value(1)
time.sleep(0.5)

seg3.value(1)
time.sleep(0.5)

seg4.value(1)
time.sleep(0.5)

seg5.value(1)
time.sleep(0.5)

# Turn off all segments
seg1.value(0)
seg2.value(0)
seg3.value(0)
seg4.value(0)
seg5.value(0)


