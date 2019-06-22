# pin A0 is an analog out pin connected to the R/L channel of the 1/8" jack
# Same pin used to play wav files

import time
import array
import math
import audioio
import board
import digitalio

frequency = 40  # Set this to the Hz of the tone you want to generate.
#frequency = 2440
length = 8000 // frequency
sine_wave = array.array("H", [0] * length)
for i in range(length):
    sine_wave[i] = int((1 + math.sin(math.pi * 2 * i / length))  * (2 ** 15 - 1))

audio = audioio.AudioOut(board.A0)
sine_wave_sample = audioio.RawSample(sine_wave)


audio.play(sine_wave_sample, loop=True)
time.sleep(2) #plays for 2 seconds
audio.stop()
