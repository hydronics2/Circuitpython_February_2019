# CircuitPython

I uploaded the above python scripts onto your Adafruit M0 board. When you plug the unit into your board it appears as a flash drive.

Download and install the [MU editor](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor) if you have not done so already.


## code.py
LOAD the code.py script. Code.py determines which scripts run. Uncomment the files you would like to run.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/programming/pics/code2.py.jpg)


## a1_blink_digital_out_example
LOAD the "a1_blink_digital_out_example.py" script that's currently running. It blinks the LED on pin 13. An internal LED also blinks. Try blinking the other LEDs on pins A1 and A2. In my case I labeled them greenLed and yellowLed. Hit the SERIAL button to see the print statements.

![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/programming/pics/a1_blink.JPG)


## a2_accelerometer_led
Modify the code.py script and uncomment a2_accelerometer_led.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/programming/pics/a2_accelerometer_code.JPG)
The script lights up an LED with increasing tilt.
When you use a print statement with double prethensis it allows the data to the plotter; such as, print((x,y,z)).
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/programming/pics/accel_plotter.JPG)

## a3_play_wav_file
Modify the code.py script and unomment a3_play_wav_file
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/programming/pics/play_wav.JPG)

5 wav files for you try. They are in the sounds folder. Uncomment the files to play each one.. and/or make your own. 
Save files as 22 KHz or less because the circuitpython can't handle more data than that and the DAC(digital-to-analog-converter) output is 10-bit so anything over 16-bit will just take up room without better quality.

![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/programming/pics/play_wav2.JPG)


## a4_ws2812_example
Modify the code.py script and unomment a4_ws2812_example
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/programming/pics/ws2812_1.JPG)
solder three leads onto your LED strip on the correct side (start of the arrow). Insert the LEDs into the screw headers.
LOAD the sketch and modify the "num_leds" variable to the number of LEDs in your strip.
The red, green, and blue LEDs can have values from 0 to 255.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/programming/pics/ws2812_2.JPG)

## analog_in_example
Modify the code.py script and unomment analog_in_example.
Try plugging in both the potentiometer and photocell to see how the analog-to-digital converter(ADC) on pin A3 interprets the signals.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/programming/pics/pot1.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/programming/pics/pot2.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/programming/pics/photocell.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/programming/pics/photocell2.JPG)









