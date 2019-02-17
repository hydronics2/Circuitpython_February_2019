# 5 wav files for you try in the sounds folder
# uncomment out the files to play each sound file.. and/or make your own. 
#save files as 22 KHz or less because the circuitpython can't handle more data than that 
#(and also it will not sound much better) and the DAC output is 10-bit so anything over 16-bit will 
#just take up room without better quality.

# the monotonic() function is some seudo threading thing that allows the processor  to do other things while the wav file plays
# once you initiate Play the monotic while loop is TRUE for sec seconds as follows ... time.monotonic() - t < sec:

import time
import audioio
import board
import digitalio
 
button = digitalio.DigitalInOut(board.A1)
button.switch_to_input(pull=digitalio.Pull.UP)
 
wave_file = open("sounds/StreetChicken.wav", "rb") # 9 second long clip
#wave_file = open("sounds/end_of_the_world2.wav", "rb") # 3 second long clip
#wave_file = open("sounds/voice_mail.wav", "rb") # 20 second long clip lelft at 16bit
#wave_file = open("sounds/laugh.wav", "rb") # ~3 second long clip
#wave_file = open("sounds/rimshot.wav", "rb") # ~2 second long clip

wave = audioio.WaveFile(wave_file)
audio = audioio.AudioOut(board.A0)
 
while True:
    audio.play(wave)
    # This allows you to do other things while the audio plays!
    t = time.monotonic()
    while time.monotonic() - t < 10:
        pass