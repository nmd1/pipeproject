# 16 is the yellow wire
# 12 is the green wire



import RPi.GPIO as GPIO
import time

yellow = 16
green = 12

GPIO.setmode (GPIO.BCM)
GPIO.setup(green,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	print GPIO.input(green)
	time.sleep(0.25)

