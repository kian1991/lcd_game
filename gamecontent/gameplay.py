#!/usr/bin/env python2

import RPi.GPIO as GPIO
import time, thread, random
import lcd

##instanciate LCD
lcd = lcd.lcd

##positions
up = (0, 0)
dwn = (1, 0)

##current position
position = ()

##LEVEL
level = (
1.2, 1.0,
0.8, 0.6,
0.4, 0.2
)
current = 0#Current Level



