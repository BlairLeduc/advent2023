# Imports
from machine import Pin
import time

# Pin definitions
red = Pin(14, Pin.OUT) # GPIO 14 is the red LED output

## Main Loop
for i in range(10):
    red.value(1)
    time.sleep(0.5)
    red.value(0)
    time.sleep(0.5)

print('Done!')
