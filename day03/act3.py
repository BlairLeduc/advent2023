# Imports
from machine import Pin
import time

# Pin definitions
redButton = Pin(2, Pin.IN, Pin.PULL_DOWN) # GPIO 2 is the red button input
greenButton = Pin(3, Pin.IN, Pin.PULL_DOWN) # GPIO 3 is the green button input
redLed = Pin(14, Pin.OUT) # GPIO 14 is the red LED output

while True: # Loop forever

    time.sleep(0.2) # Wait 0.2 seconds

    if redButton.value() == 1:
        print('Light off!')
        redLed.value(0) # LED pin LOW
    
    if greenButton.value() == 1:
        print('Light on!')
        redLed.value(1) # LED pin HIGH