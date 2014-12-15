#!/usr/bin/python

import subprocess
import re
from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from Adafruit_MCP230xx import MCP230XX_GPIO
from Adafruit_CharLCD import Adafruit_CharLCD

# set wifi interface
wif = "wlan0"

# Initiate CharLCDPlate
led = Adafruit_CharLCDPlate()
# clear screen
led.clear()
# turn LED off
led.backlight(led.OFF)

# Initiate Display
bus = 1         # Note you need to change the bus number to 0 if running on a revision 1 Raspberry Pi.
address = 0x20  # I2C address of the MCP230xx chip.
gpio_count = 8  # Number of GPIOs exposed by the MCP230xx chip, should be 8 or 16 depending on chip.
mcp = MCP230XX_GPIO(bus, address, gpio_count)

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCD(pin_rs=1, pin_e=2, pins_db=[3,4,5,6], GPIO=mcp)

# turn lcd off
lcd.display()

# turn lcd back on
lcd.noDisplay()
led.message("Search for  WiFis")
sleep(3)

# check for WiFis nearby
# check for WiFis nearby
wifi_out = subprocess.Popen(["iwlist", wif, "scan"],stdout=subprocess.PIPE)
wifi_data = iter(wifi_out.stdout.readline,'')

# go through the list to display them
for line in wifi_data:
	searchObj = re.search( r'.* Cell [0-9][0-9] - Address: .*', line, re.M|re.I)
	if searchObj:
		word = line.split()
		nexthing = next(wifi_data).split('"')
		wifi = [word[4],nexthing[1]]
		led.clear()
		led.message(wifi[0] + "\n" + wifi[1])
		sleep(3)



lcd.display()

