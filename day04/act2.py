# Activity 2: Easier segment control with lists

# Imports
from machine import Pin
import time

# Pin definitions
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# Create a list for our segments
segments = [seg1, seg2, seg3, seg4, seg5]

# For loop and turn on each segment in turn
for segment in segments:
    segment.value(1)
    time.sleep(0.5)

# For loop and turn off each segment in turn
for segment in segments:
    segment.value(0)
