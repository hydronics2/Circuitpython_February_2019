# CircuitPython IO demo #1 - General Purpose I/O

# blink and hello world in one. Press the serial button above to see the serial output

import time
import board
from digitalio import DigitalInOut, Direction, Pull

redLed = DigitalInOut(board.D13)
redLed.direction = Direction.OUTPUT
greenLed = DigitalInOut(board.A2)
greenLed.direction = Direction.OUTPUT
yellowLed = DigitalInOut(board.A1)
yellowLed.direction = Direction.OUTPUT
 
while True:
    redLed.value = True
    print("hello world")
    time.sleep(1)  # debounce delay
    redLed.value = False
    time.sleep(1)