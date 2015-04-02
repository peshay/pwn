#!/usr/bin/python

import subprocess
import re
from time import sleep
import Adafruit_CharLCD as LCD

# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

# function to switch through menu items on LCD
def menuSwitcher ( menuItems ):
    indexCounter = 0
    indexEnd = len(menuItems) - 1
    lcd.clear()
    # show first entry
    lcd.message(menuItems[indexCounter][0] + "\n" + menuItems[indexCounter][1])
    while True:
        if (lcd.is_pressed(LCD.RIGHT)):
            lcd.clear()
            indexCounter += 1
            if indexCounter > indexEnd:
                indexCounter = 0
            lcd.message(menuItems[indexCounter][0] + "\n" + menuItems[indexCounter][1])	
            sleep(0.5)
        elif (lcd.is_pressed(LCD.LEFT)):
            lcd.clear()
            indexCounter -= 1
            if indexCounter == 0:
                indexCounter = indexEnd
            lcd.message(menuItems[indexCounter][0] + "\n" + menuItems[indexCounter][1])
            sleep(0.5)
        elif (lcd.is_pressed(LCD.SELECT)):
            lcd.clear()
            break
    return menuItems[indexCounter][0], menuItems[indexCounter][1]
        

# set wifi interface
wif = "wlan0"

# turn lcd back on
lcd.message("Search for  WiFis")
lcd.enable_display(True)
lcd.set_backlight(1)

# check for WiFis nearby
wifi_out = subprocess.Popen(["iwlist", wif, "scan"],stdout=subprocess.PIPE)
#wifi_out = subprocess.Popen(["cat", "iwlist"],stdout=subprocess.PIPE)
wifi_data = iter(wifi_out.stdout.readline,'')
wifi = []
# go through the list to display them
for line in wifi_data:
	searchObj = re.search( r'.* Cell [0-9][0-9] - Address: .*', line, re.M|re.I)
	if searchObj:
		word = line.split()
		nexthing = next(wifi_data).split('"')
		wifi.append((word[4],nexthing[1]))
sleep(1)

menuSwitcher(wifi)
        	

lcd.set_backlight(0)