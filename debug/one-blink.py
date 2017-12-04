import RPi.GPIO as GPIO # Import GPIO library
import sys
from time import sleep
pin = int(sys.argv[1])
sec = int(sys.argv[2])

GPIO.setmode(GPIO.BCM) # Use board pin numbering
GPIO.setup(pin, GPIO.OUT) # Setup GPIO Pin 7 to OUT
GPIO.output(pin,True) # Turn on GPIO pin 7

sleep(sec)

GPIO.cleanup()
