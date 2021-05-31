#!/usr/bin/env python3

#
# Grow light module control.
# Work in progress
#

import datetime
import RPi.GPIO as GPIO
from board import SCL, SDA
from busio import I2C
from pimoroni_circuitpython_ltr559 import Pimoroni_LTR559


I2C_BUS = I2C(SCL, SDA)
LTR559 = Pimoroni_LTR559(I2C_BUS)
light_value = 200 # Random number, need to test that

def main():
    now = datetime.datetime.now()
    
    while True:
        LTR559.lux < light_value  # while Lux value from light sensor is bellow the requested light value 
        if 6 <= now.hour >= 20:   # only turn on light between 06h00 and 20h00.
            print("light on")     # Turn on light code (need to find a relay)
        else
            print("light off")

if __name__ == "__main__":
    main()
