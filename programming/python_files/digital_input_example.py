# button input example
# touch pin D9 to Ground and the LED turns on

import time
import board
from digitalio import DigitalInOut, Direction, Pull
 
yellowLed = DigitalInOut(board.A1) #A1 is the yellow LED that doesn't do PWM
yellowLed.direction = Direction.OUTPUT
 
button = DigitalInOut(board.D9)
button.direction = Direction.INPUT
button.pull = Pull.UP
 
while True:
    if button.value: #if D9 isn't connected to ground
        yellowLed.value = False
    else:
        yellowLed.value = True
 
    #time.sleep(0.01)  # debounce delay