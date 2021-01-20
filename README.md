# LCD-Poetry-Clock

Full tutorial: https://create.arduino.cc/projecthub/kzra/lcd-poetry-clock-c732d4

The LCD functions as a clock, displaying the time and the date. Every fifteen minutes it displays the daily poem, which is chosen randomly each day from the SD card. You can also press a red button to display a random poem from the SD card. Whenever a poem is displayed the screen also changes to a random colour. Two other push buttons allow you to change the time and date. 

## Choosing the poems

To start this project the first stage is to get the poems onto the SD card. It is probably a good idea to first format the SD card to FAT32 format. 
I downloaded over 500 poems using the poetryDB API and this python script. I also added a few of my own choice by Robert Frost, Ted Hughes and Sylvia Plath. 
The full collection of poems I used is available here.  Transfer the text files (not in a parent directory) directly onto the SD card. To add additional poems, you just need to write them in a.txt file using a program like notepad.

## Building the breadboard
The next step is to put the project together using a breadboard. Follow the circuit diagram shown in the schematic (apologies in advance for the number of connections). To understand what the connections are doing, here is a good guide for wiring the SD card reader, and another one for the 20* 4 RGB LCD. Finally, upload the poetryClock.ino code to your Arduino. Once you have done that, the clock should function like the one in the video above. The red button displays a random poem, the blue button changes a time parameter, the green button selects which time parameter to change (Minute (T), Hour (H), Day (D), Month (M) or Year (Y). 

## Casing the project

I used a tuperware from my kitchen and cut a rectangle from the lid using a stanley knife for the LCD screen. I drilled 7mm holes in the lid for the push buttons and drilled a 10mm hole in the body of the tuperware to provide space for a USB connection to the Arduino. 
To solder the LCD screen I removed the header pins and directly soldered wires to it. The other end of the wires I pushed into the Arduino ports (with no solder). I used perma-proto boards to house the SD card reader and secured all the boards and peripherals with nuts and bolts.  It took a while (and several frustrating revisions) to get the design right, but felt pretty sturdy once it was finished. 

![poetryclockimage](https://github.com/Kzra/LCD-Poetry-Clock/blob/main/Poetry%20Clock%20cover%20image.png)


