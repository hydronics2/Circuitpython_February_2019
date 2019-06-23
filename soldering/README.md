# Soldering

Parts list
- [Nordic Semiconductor nrf52840 bluetooth module](https://www.adafruit.com/product/4078)
- [LIS3DH Accelerometer](https://www.aliexpress.com/item/CJMCU-LIS3DSH-High-resolution-Three-axis-Accelerometer-Triaxial-Accelerometer-Module-LIS3DH/32879796761.html?)
)
- [micro USB connector](https://www.digikey.com/product-detail/en/amphenol-icc-fci/10118194-0001LF/609-4618-6-ND/2785383)




[Here's the schematic](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/eagle_design_files/PCB_schematic.pdf)


![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/1.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/2.JPG)
Solder on pins should look concave. NOT BALLS. Use your solding iron to wick away excess solder.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/3.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/4.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/5.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/6.JPG)
Your cap maybe 47uF cause that's what I had although the adafruit tutorial recomends 100uF 16V.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/7.JPG)
[](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/8.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/9.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/10.JPG)
The resistor color band for 10K is brown-black-orange. The last color (gold in this picture) indicates tollerance (1%, 5%, etc).
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/11.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/12.JPG)
Soldering the accelerometer board ~1/8" above the PCB keeps the pins looking nice on the bottom. 
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/13.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/14.JPG)
These 5.08mm screw terminals slide together.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/15.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/16.JPG)
Solder all those Pins!
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/17.JPG)
Choose wichever color LEDs you like. The longer lead is positive.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/18.JPG)
The notch in the LED is negative and matches the notch in the silkscreen.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/19.JPG)
The current limiting resistors for the LEDs is 220ohms. The color band for 220 is red-red-black.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/20.JPG)
Solder all those Pins!
Break the male headers into 14 pins to match the length of the uController and solder the pins to the uController.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/21.JPG)
Solder all those Pins!
Break 2 pins off the 16pin male headers to get 14 pins is all you need. You're Done.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/chip_soldered.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/ws2812.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/22.jpg)

Solder 3 wires onto the potentiometer.

That's it. We're all finished! We're leaving a few footprints unpopulated for this class.
