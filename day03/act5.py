# Imports
from machine import Pin
import time

# Pin definitions
redButton = Pin(2, Pin.IN, Pin.PULL_DOWN) # GPIO 2 is the red button input
greenButton = Pin(3, Pin.IN, Pin.PULL_DOWN) # GPIO 3 is the green button input

count = 0

while True: # Loop forever

    time.sleep(0.2) # Wait 0.2 seconds

    if redButton.value() == 1:
        count = count + 1
        print('Red button pressed! Count is now', count)

    if greenButton.value() == 1:
        count = count - 1
        print('Green button pressed! Count is now', count)