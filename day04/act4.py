# Activity 4: Randon LEDs

# Imports
from machine import Pin
import time
import random

# Pin definitions
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# Create a list for our segments
segments = [seg1, seg2, seg3, seg4, seg5]

# Loop forever
while True:

    # Set a random number between 0 and 4
    randomSegment = random.randint(0,4)

    # Turn on the random segment
    segments[randomSegment].value(1)

    # Wait 0.5 seconds
    time.sleep(0.5)

    # Turn off the random segment
    segments[randomSegment].value(0)