#!/usr/bin/python
import time
import RPi.GPIO as GPIO
from RPLCD import CharLCD


##Custom char creation
enemy = (
 0b00000,
 0b00000,
 0b01010,
 0b01110,
 0b11111,
 0b10101,
 0b01110,
 0b01010,
 )

player = (
 0b00111,
 0b00111,
 0b00100,
 0b11110,
 0b11110,
 0b10010,
 0b10010,
 0b11011,
 )

GPIO.setmode(GPIO.BCM)
lcd = CharLCD(cols=16, rows=2,
                pin_rw=None,
                pin_rs=17,
                pin_e=18,
                pins_data=[27,22,23,24],
                numbering_mode=GPIO.BCM)

def init():
        lcd.create_char(1, enemy)
	lcd.create_char(0, player)

		

