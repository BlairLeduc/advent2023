# Activity 3: LED scanner

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

while True:

    # For loop to turn on each segment in turn then off
    for segment in segments:
        segment.value(1)
        time.sleep(0.8)
        segment.value(0)

    # Loop in reverse to turn on each segment in turn then off
    for segment in reversed(segments):
        segment.value(1)
        time.sleep(0.8)
        segment.value(0)