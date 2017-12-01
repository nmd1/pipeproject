# 16 is the yellow wire
# 12 is the green wire

import RPi.GPIO as GPIO# calling header file for GPIO's of PI
import time# calling for time to provide delays in program
GPIO.setmode (GPIO.BCM)# programming the GPIO by BOARD pin numbers, GPIO21 is called as PIN40
GPIO.setup(16,GPIO.OUT)# initialize digital pin40 as an output.
GPIO.output(16,1)# turn the LED on (making the voltage level HIGH)
time.sleep(1)# sleep for a second
GPIO.cleanup()# turn the LED off (making all the output pins LOW)
time.sleep(1)#sleep for a second    
