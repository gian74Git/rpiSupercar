#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import sys
import os

iMaxLed = 6
if (len(sys.argv) > 1):
  sTime = float(sys.argv[1])
else:
  sTime = 0.05

bEsegui = True
bSem = True
iVolte = 0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def accendi(iLed):
	global bEsegui
 	global iVolte
	global bSem
	if ((GPIO.input(3) == False) & (bSem)):	
		iVolte = iVolte + 1
		bEsegui = not bEsegui
		bSem = False
		print "SCHIACCIATO " + str(iVolte) + " volte"
		time.sleep(0.2)
		#time.sleep(1)
	#Se input(3) e' True, ho rilasciato il pulsante e se bSem e' False
	#deve essere rimesso a posto.
	elif ((GPIO.input(3) == True) & (not bSem)):
		bSem = True
	
	if bEsegui:
		for i in [7,8,11,12,15,16,21,22]:
			GPIO.output(i, GPIO.LOW)
	        GPIO.output(iLed, GPIO.HIGH)
		time.sleep(sTime)
	return

os.system('clear')
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.IN)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

while True:
  accendi(7)
  accendi(8)
  accendi(11)
  accendi(12)
  accendi(15)
  accendi(16)
  accendi(21)
  accendi(22)
  accendi(21)
  accendi(16)
  accendi(15)
  accendi(12)
  accendi(11)
  accendi(8)
