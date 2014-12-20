#!/usr/bin/python

import subprocess
import re
from time import sleep

# set wifi interface
wif = "wlan0"

# Initiate CharLCDPlate
#led = Adafruit_CharLCDPlate()
# clear screen
#led.clear()
# turn LED off
#led.backlight(led.OFF)

# Initiate Display
#bus = 1         # Note you need to change the bus number to 0 if running on a revision 1 Raspberry Pi.
#address = 0x20  # I2C address of the MCP230xx chip.
#gpio_count = 8  # Number of GPIOs exposed by the MCP230xx chip, should be 8 or 16 depending on chip.
#mcp = MCP230XX_GPIO(bus, address, gpio_count)

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
#lcd = Adafruit_CharLCD(pin_rs=1, pin_e=2, pins_db=[3,4,5,6], GPIO=mcp)

# turn lcd off
#lcd.display()

# turn lcd back on
#lcd.noDisplay()
#led.message("Search for  WiFis")
#sleep(3)

# check for WiFis nearby
wifi_out = subprocess.Popen(["cat", "iwlist"],stdout=subprocess.PIPE)
wifi_data = iter(wifi_out.stdout.readline,'')
wifi = []
# go through the list to display them
i = 0 	# pointer
for line in wifi_data:
	searchObj = re.search( r'.* Cell [0-9][0-9] - Address: .*', line, re.M|re.I)
	if searchObj:
		word = line.split()
		nexthing = next(wifi_data).split('"')
		wifi.append((word[4],nexthing[1]))
### button example code
# Poll buttons, display message & set backlight accordingly
#btn = ((lcd.LEFT  , 'Red Red Wine'              , lcd.RED),
#       (lcd.UP    , 'Sita sings\nthe blues'     , lcd.BLUE),
#       (lcd.DOWN  , 'I see fields\nof green'    , lcd.GREEN),
#       (lcd.RIGHT , 'Purple mountain\nmajesties', lcd.VIOLET),
#       (lcd.SELECT, ''                          , lcd.ON))
#prev = -1
#while True:
#    for b in btn:
#        if lcd.buttonPressed(b[0]):
#            if b is not prev:
#                lcd.clear()
#                lcd.message(b[1])
#                lcd.backlight(b[2])
#                prev = b
#            break
i = 0 	# pointer
print len(wifi)
print wifi[0][1]



#lcd.display()

