#!/usr/bin/env python

import threading, time
import lcd
import gameplay as gp
import random


level = gp.level

##instanciate and init lcd

lcd = lcd.lcd

class player:

	def __init__(self): 
                self.position = gp.up
                lcd.write_string(chr(0))

        def move(self):
                if self.position == up:
                        lcd.cursor_pos = up
                        lcd.write_string(" ")
                        lcd.cursor_pos = dwn
                        lcd.write_string(chr(0))
                        self.position = dwn
                elif self.position == dwn:
                        lcd.cursor_pos = dwn
                        lcd.write_string(" ")
                        lcd.cursor_pos = up
                        lcd.write_string(chr(0))
                        self.position = up        
        
	
		
			
