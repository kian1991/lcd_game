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
                if self.position == gp.up:
                        lcd.cursor_pos = gp.up
                        lcd.write_string(" ")
                        lcd.cursor_pos = gp.dwn
                        lcd.write_string(chr(0))
                        self.position = gp.dwn
                elif self.position == gp.dwn:
                        lcd.cursor_pos = gp.dwn
                        lcd.write_string(" ")
                        lcd.cursor_pos = gp.up
                        lcd.write_string(chr(0))
                        self.position = gp.up        
        
	
		
			
