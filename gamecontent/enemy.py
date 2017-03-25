#!/usr/bin/env python

import threading, time
import lcd
import gameplay as gp
import random, sys
import RPi.GPIO as GPIO

level = gp.level

##instanciate and init lcd

lc = lcd.lcd
thrds = []



class enemy (threading.Thread):

	def __init__(self):
                super(enemy, self).__init__()
                self.daemon = True
                self.spawn = True
                self.threadNumber = 0
                
                
	def enemySpawner(self):
        	while self.spawn:
                        print "running Threads: " + str(threading.activeCount())
                        row = random.randint(0, 1)
                        t = spawner(row, self.threadNumber)
                        self.threadNumber += 1
                        t.start()
                        thrds.append(t)
                        time.sleep(random.randint(3, 5))

        def run(self):
		self.enemySpawner()

class spawner(threading.Thread):

        def __init__(self, row, number):
                super(spawner, self).__init__()
                self.daemon = True
                self._stop = threading.Event()
                self.row = row
                self.number = number

        def run(self):
                while not self.isStopped():
                        print "starting Thread# " + str(threading.currentThread())
                        x = self.row
                        for i in range(15, -1, -1):
                                if i < 15:
                                        lc.cursor_pos = (x, i + 1)
                                        lc.write_string(" ")
                                lc.cursor_pos = (x, i)
                                lc.write_string(chr(1))
                                time.sleep(level[gp.current])##Speed of enemys depends on current level
				if i == 0:
					if gp.positon == (x, i):##check collidsion
						sys.exit()
					else:##delete enemy
                                                lc.cursor_pos = (x, i)
						lc.write_string(' ')
                        else:
                                self.stop()
                

        def stop(self):
                self._stop.set()

        def isStopped(self):
                return self._stop.isSet()
                
		
			
