# PWM can be used on the following pins: D0, RX, D1, TX, D2, D3, D4, D5, D6, 
# ......D7, D8, D9, D10, D11, D12, D13, L, A2, A3, A4, MOSI, MISO, SCK, SCL, 
#.......SDA, APA102_MOSI, APA102_SCK.

# the dorkbot board has LEDs on A2, D13, and power mosfets on D11 and D10.

import time 
import board
import pulseio
 
redLed = pulseio.PWMOut(board.D13, frequency=5000, duty_cycle=0)
greenLed = pulseio.PWMOut(board.A2, frequency=5000, duty_cycle=0)
# mosfetLed1 = pulseio.PWMOut(board.D10, frequency=5000, duty_cycle=0)
# mosfetLed2 = pulseio.PWMOut(board.D10, frequency=5000, duty_cycle=0)
 
while True:
    for i in range(100):
        # PWM LED up and down
        if i < 50:
            redLed.duty_cycle = int(i * 2 * 65535 / 100)  # Up
        else:
            redLed.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # Down
        time.sleep(0.01)