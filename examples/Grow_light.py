#!/usr/bin/env python3

#
# Grow light module control.
# Work in progress
#

import datetime
import RPi.GPIO as GPIO
from ltr559 import LTR559

## Variables
ltr559 = LTR559() # Calling the light sensor
light_value = 200 # Random number, need to test that


## Main function
def main():
    now = datetime.datetime.now()
    while True:
        ltr559.update_sensor()
        lux = ltr559.get_lux()
        lux < light_value         # while Lux value from light sensor is bellow the requested light value
        if 6 <= now.hour >= 20:   # only turn on light between 06h00 and 20h00.
            print("light on (lux = {})".format(lux))     # Turn on light (need to find a relay)
        else
            print("light off (lux = {})".format(lux))    # Turn off light (need to find a relay)

if __name__ == "__main__":
    main()
