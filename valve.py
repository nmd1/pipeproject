import RPi.GPIO as GPIO # Import GPIO library

def open(pin=1):
	GPIO.setmode(GPIO.BCM) # Use board pin numbering
	GPIO.setup(pin, GPIO.OUT) # Setup GPIO Pin 7 to OUT
	GPIO.output(pin,True)

def close(pin=1):
	GPIO.setmode(GPIO.BCM) # Use board pin numbering
	GPIO.setup(pin, GPIO.OUT) # Setup GPIO Pin 7 to OUT
	GPIO.output(pin,False)

def change(state,pin=1):
        GPIO.setmode(GPIO.BCM) # Use board pin numbering
        GPIO.setup(pin, GPIO.OUT) # Setup GPIO Pin 7 to OUT
        GPIO.output(pin,state)




