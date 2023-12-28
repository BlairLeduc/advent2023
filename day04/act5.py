# Activity 5: Button press counter with LEDs

# Imports
from machine import Pin
import time

# Pin definitions
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)
redButton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Create a list for our segments
segments = [seg1, seg2, seg3, seg4, seg5]

count = -1 

# Turn off all segments
for segment in segments:
    segment.value(0)

# Loop forever
while True:

    time.sleep(0.1)

    if redButton.value() == 1:

        if count == 4:
            pass # Do nothing
        else:
            count = count + 1
            segments[count].value(1)
            time.sleep(0.2)

    if greenButton.value() == 1:
            
            if count == -1:
                pass # Do nothing
            else:
                segments[count].value(0)
                count = count - 1
                time.sleep(0.2)