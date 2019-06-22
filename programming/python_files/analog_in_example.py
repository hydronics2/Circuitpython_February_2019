# CircuitPython AnalogIn Demo

# use a potentiometer or a light sensor across 3V, A3, and ground (GND)
# turn an LED on when it gets light or dark
# see pictures

# the A3 analog value is printed. It has a 12bit ADC...
# 12bit outputs 0-4096 between the values of 0V to 3.3V

import time
import board
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction
 
analog_in = AnalogIn(board.A3)

yellowLed = DigitalInOut(board.A1) #A1 is the yellow LED that doesn't do PWM
yellowLed.direction = Direction.OUTPUT
 
 
def get_voltage(pin):
    return (pin.value * 3.3) / 65536
 
 
while True:
    analogValue = get_voltage(analog_in)
    print((analogValue,))
    if analogValue < 2.5:
        yellowLed.value = True
    else:
        yellowLed.value = False
    time.sleep(0.1)