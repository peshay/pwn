#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from Adafruit_MCP230xx import MCP230XX_GPIO
from Adafruit_CharLCD import Adafruit_CharLCD

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

# prepare next message and set LED red
led.clear()
led.message("ahutest")
led.backlight(led.RED)

# turn lcd back on
lcd.noDisplay()
sleep(3)

# change lcd mesasge
led.clear()
led.autoscroll()
led.message("Daniel ist doof! super doof! mega doof! hyper doof!")
led.autoscroll()
sleep(3)
led.backlight(led.GREEN)
sleep(3)

# turn lcd and led off
led.backlight(led.OFF)
lcd.display()
sleep(3)
