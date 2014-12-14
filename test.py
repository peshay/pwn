#! /usr/bin/env python
# ______                           ______ __
# |   __ \.-----.-----.--.--.-----.|   __ \__|
# |      <|  _  |  _  |  |  |  -__||    __/  |
# |___|__||_____|___  |_____|_____||___|  |__|
#               |_____|              v1.0
#
# Author:	Kalen Wessel
# Date: 	February 16th, 2013
 
from time import sleep
from Adafruit_I2C import Adafruit_I2C
from Adafruit_MCP230xx import Adafruit_MCP230XX
from Adafruit_MCP230xx import MCP230XX_GPIO
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import call
from sys import exit
from ConfigParser import SafeConfigParser

import smbus
import subprocess
import re
import socket
import fcntl
import struct
import paramiko
import socket
import signal


bus = 1         # Note you need to change the bus number to 0 if running on a revision 1 Raspberry Pi.
address = 0x20  # I2C address of the MCP230xx chip.
gpio_count = 8  # Number of GPIOs exposed by the MCP230xx chip, should be 8 or 16 depending on chip.

# Create MCP230xx GPIO adapter.
print "set mcp"
mcp = MCP230XX_GPIO(bus, address, gpio_count)
sleep(2)

# Create LCD, passing in MCP GPIO adapter.
print "set lcd"
lcd = Adafruit_CharLCD(pin_rs=1, pin_e=2, pins_db=[3,4,5,6], GPIO=mcp)
sleep(2)

# lampe leuchten lassen
#lcd.backlight(lcd.RED)
#sleep(1)
#lcd.backlight(lcd.BLUE)
#sleep(1)
#lcd.backlight(lcd.GREEN)
#sleep(1)
#lcd.backlight(lcd.VIOLET)
#sleep(1)
#lcd.backlight(lcd.ON)
#sleep(1)
#lcd.backlight(lcd.YELLOW)
#sleep(1)
#lcd.backlight(lcd.TEAL)
#sleep(1)
#lcd.backlight(lcd.OFF)
#sleep(1)


# Commented out to speed up overal test time
# Starting On Board System Check
print "lcd message"
lcd.message('ahutest \n tohack')
sleep(2)
print "autoscroll"
lcd.autoscroll()
sleep(2)
print "display"
lcd.display()
sleep(10)
