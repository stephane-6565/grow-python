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
light_value = 2000 # Random number, need to test that


## Main function
def main():
    now = datetime.datetime.now()
    while True:
        ltr559.update_sensor()
        lux = ltr559.get_lux()
        if (6 <= now.hour <= 20) and (lux < light_value) :   # only turn on light between 06h00 and 20h00 while Lux value from light sensor is bellow the requested light value.
            print("Time: {a} | Light on (lux = {b})".format(a = now.hour , b = lux))     # Turn on light (need to find $        else:
        else:    
            print("Time: {a} | Light off (lux = {b})".format(a= now.hour , b = lux))    # Turn off light (need to find $

   
if __name__ == "__main__":
   main()
