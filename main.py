#!/usr/bin/env python

import RPi.GPIO as GPIO
import time, thread, random
import gamecontent.enemy as enemy
import gamecontent.player as player
import gamecontent.lcd as lcd



if __name__ == '__main__':
	button = 16
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(button, GPIO.IN)

		
	##init Spawner and move
	try:
        	##init me, lcd and enemys
	        lcd.init()
       		player = player.player()
		spawner = enemy.enemy()
		spawner.start()
	
        
		##MAIN THREAD
		while(True):
			if GPIO.input(button):
				player.move();
				print "pressed"
			time.sleep(0.4)
	except KeyboardInterrupt:
		GPIO.cleanup()
