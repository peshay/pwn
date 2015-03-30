#!/usr/bin/python

import subprocess
import re
from time import sleep
import Adafruit_CharLCD as LCD

# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

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

i = 0
j = len(wifi) - 1
lcd.clear()

lcd.set_color(0.0, 0.0, 1.0)
lcd.message(wifi[i][0] + "\n" + wifi[i][1])	
while 1:
    if (lcd.is_pressed(LCD.RIGHT)):
        lcd.clear()
        i += 1
        if i > j:
            i = 0
        lcd.message(wifi[i][0] + "\n" + wifi[i][1])	
        sleep(0.5)
    elif (lcd.is_pressed(LCD.LEFT)):
        lcd.clear()
        i -= 1
        if i == 0:
            i = j
        lcd.message(wifi[i][0] + "\n" + wifi[i][1])
        sleep(0.5)
    elif (lcd.is_pressed(LCD.SELECT)):
        lcd.clear()
        print 'Go For It!' 
        break
    
        	
print "hack " + wifi[i][1] + "\t" + wifi[i][1]

lcd.set_backlight(0)