#from __future__ import print_function 	# I converted this to python 3 now
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pins = [0,5,13,19,26,16,21,20,6,12]
# more pins: 6,12
pins = list(reversed(pins)) 		# The pins are reversed in the arduino, so we flip it back here.

for pin in pins:
	GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def convert(val):
	volts = (val/1024.0) * 5;	# rescale value to voltage (2^8 wires)
	outv = (volts/0.24) - 0.5;	# raw math (credit to cho)
	psi = (outv * 10.1379);		# more math
	return psi

def getBits():
	rawbin = []
	for pin in pins:
                rawbin.append(GPIO.input(pin))
	return rawbin

def debugReturnPSI():	
	rawbinary = getBits()		# get bits from arduino
	binary = ""
	for unit in rawbinary:		# convert array to string
    		binary += str(unit)
	value = int(binary, 2)		# convert bin string to int
	psi = convert(value)		# do math conversion
	return psi,rawbinary
	
	
def returnPSI():
	rawpsi = debugReturnPSI()[0]
	if (rawpsi >= 0):
		return rawpsi		# wrap debug function for external use
	else:
		return "Sensor not connected"

def run():
	while True:
		psi = debugReturnPSI()
		print(psi[1],end=' ')
		print(psi[0])
		time.sleep(.01)
	

