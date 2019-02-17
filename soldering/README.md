# Soldering

Parts list
- [itsybitsy M0](https://www.adafruit.com/product/3727)
- [LIS3DSH Accelerometer](https://www.aliexpress.com/item/CJMCU-LIS3DSH-High-resolution-Three-axis-Accelerometer-Triaxial-Accelerometer-Module-LIS3DH/32879796761.html?)
- [14 pin double row headers](https://www.aliexpress.com/item/100-pcs-2-54-mm-0-100-Pitch-2x14-28-Pin-Dual-Row-PCB-Female-Header/32807834427.html?)
- [2-pin terminal blocks](https://www.aliexpress.com/item/50PCS-PCB-Screw-Terminal-Block-Connector-KF127-2P-pitch-5-08MM-0-2inch-Green-5mm-KF127/32791211110.html?)
- [WS2812 LED Strip](https://www.aliexpress.com/item/5m-DC5V-WS2812B-led-pixel-srip-non-waterproof-74pcs-WS2812B-M-with-60pixels-BLACK-PCB-only/1667439010.html?)
- [FQP30N06 Power Mosfet TO-220](https://www.aliexpress.com/item/Free-shipping-100pcs-lot-FQP30N06-30N06-TO-220-IC/32863833006.html?)
- [3.5 mm (1/8") jack](https://www.aliexpress.com/item/Free-shipping-100pcs-lot-FQP30N06-30N06-TO-220-IC/32863833006.html?)
- [trim pot ~1K](https://www.aliexpress.com/item/Free-shipping-100PCS-3296W-1-103LF-3296W-3296-10K-OHM-Trimpot-Trimmer-Potentiometer/32285032567.html?)
- 100uF 16V Capacitor
- 10k pullup resistors
- 220 ohm current limiting LED resistors
- [2ohm, 1/2watt Power Sensing Resistor](https://www.digikey.com/product-detail/en/stackpole-electronics-inc/CFM12JT2R00/S2HCT-ND/2617415)
- [PN2222A Transistor](https://www.aliexpress.com/item/100pcs-PN2222A-TO-92-PN2222-TO-92/32888878276.html?)
- [micro USB connector](https://www.digikey.com/product-detail/en/amphenol-icc-fci/10118194-0001LF/609-4618-6-ND/2785383)


![Here's the schematic](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/eagle_design_files/PCB_schematic.pdf)


![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/1.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/2.JPG)
Solder on pins should look concave. NOT BALLS. Use your solding iron to wick away excess solder.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/3.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/4.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/5.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/6.JPG)
Your cap maybe 47uF cause that's what I had although the adafruit tutorial recomends 100uF 16V.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/7.JPG)
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/8.JPG)
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
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/17.JPG)
Choose wichever color LEDs you like. The longer lead is positive.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/18.JPG)
The notch in the LED is negative and matches the notch in the silkscreen.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/19.JPG)
The current limiting resistors for the LEDs is 220ohms. The color band for 220 is red-red-black.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/20.JPG)
Break the male headers into 14 pins to match the length of the uController and solder the pins to the uController.
![](https://github.com/hydronics2/Circuitpython_February_2019/blob/master/soldering/pics/21.JPG)
Break 2 pins off the 16pin male headers to get 14 pins is all you need. You're Done.

We're not going to solder the rest of the parts unless we have more time or you want to do extra.
