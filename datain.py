# 16 is the yellow wire
# 12 is the green wire



import RPi.GPIO as GPIO
import time
import os


yellow = 16
green = 12
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25
 
DEBUG = 1

# GPIO Setup
GPIO.setmode (GPIO.BCM)
GPIO.setup(green,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)
# read in SPI data from the Analog to Digital Converter

def readAD(adcnum):
	cspin = SPICS      # Reset Pin
	clockpin = SPICLK  # Clock. We have one. The sensor does not....
	mosipin = SPIMOSI  # Data out pin (useless for us)
	misopin = SPIMISO  # Data in pin (all that we want)
	
	if ((adcnum > 7) or (adcnum < 0)):
		return -1
	GPIO.output(cspin, True)
	GPIO.output(clockpin, False)	# Start the clock low
	GPIO.output(cpsin, False)	# Bring reset low
	
	# I have no idea how the rest of this code works tbh...
	
	commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
 
        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1
 
        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout
