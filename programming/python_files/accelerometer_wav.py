# when the accelerometer reaches some threshold (x > 0.3) a wav file plays 

import time
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import busio
import lis3d_sh
import audioio

i2c = busio.I2C(board.SCL, board.SDA)
int1 = digitalio.DigitalInOut(board.D6)  # Set to correct pin for interrupt!
accelerometer = lis3d_sh.LIS3DH_I2C(i2c, address=0x1D, int1=int1)
accelerometer.range = lis3d_sh.RANGE_2_G

wave_file = open("sounds/StreetChicken.wav", "rb") # 9 second long clip
wave = audioio.WaveFile(wave_file)
audio = audioio.AudioOut(board.A0)

redLed = DigitalInOut(board.D13)
redLed.direction = Direction.OUTPUT
greenLed = DigitalInOut(board.A2)
greenLed.direction = Direction.OUTPUT
yellowLed = DigitalInOut(board.A1)
yellowLed.direction = Direction.OUTPUT

while True:
    audio.play(wave)
    audio.pause()
    t = time.monotonic()
    while time.monotonic() - t < 2:  #plays for 2 seconds once x is above the threshold below
        x, y, z = [value / lis3d_sh.STANDARD_GRAVITY for value in accelerometer.acceleration]
        print("x = %0.3f G, y = %0.3f G, z = %0.3f G" % (x, y, z))
        if x > 0.1:
            redLed.value = True
        else:
            redLed.value = False
        if x > 0.2:
            greenLed.value = True
        else:
            greenLed.value = False
        if x > 0.3:
            yellowLed.value = True
            audio.resume()
        else:
            yellowLed.value = False  
            audio.pause
    