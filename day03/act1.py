# Imports
from machine import Pin
import time

# Pin definitions
redButton = Pin(2, Pin.IN, Pin.PULL_DOWN) # GPIO 2 is the red button input

while True: # Loop forever

    time.sleep(0.1) # Wait 0.1 seconds
    
    if redButton.value() == 1: # If the red button is pressed
        print('Red button pressed!')