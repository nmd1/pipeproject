from __future__ import print_function
import RPi.GPIO as GPIO
import time
import easygui

pins = [0,5,13,19,26,16,21,20]
pins = list(reversed(pins))

GPIO.setmode(GPIO.BCM)
for pin in pins:
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def getpsi(val):
	volts = (val/254.0) * 5;
	outv = (volts/0.24) - 0.5;
	psi = (outv * 10.1379);
	return psi

while True:
	rawbin = []	
	for pin in pins:
		rawbin.append(GPIO.input(pin))
	print(rawbin,end='')
	binary = ""
	for unit in rawbin:
    		binary += str(unit)
	value = int(binary, 2)
        print(getpsi(value))
	
	time.sleep(.01)
	
	

