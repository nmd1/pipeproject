import RPi.GPIO as GPIO
from time import sleep, time
import recieve


def silentLeak(timeout):
	TIMEOUT = timeout #in seconds

	GPIO.setmode(GPIO.BCM)
	motorpin = 1
	GPIO.setup(motorpin,GPIO.OUT)

	# protip: when not powered the valve is shut.

	SHUT = 0
	OPEN = 1
	# shut off motor
	GPIO.output(motorpin,SHUT)# turn the LED on (making the voltage level HIGH)

	# wait a sec
	sleep(2)

	go = True
	# take in reading
	TownPSI = recieve.returnPSI()
	print(TownPSI)
	if (type(TownPSI) == type("text")):
		return TownPSI

	# Take a breath
 
	sleep(.1)

	# Open Valve
	GPIO.output(motorpin,OPEN)

	# Give the water some time
	print("waiting for water")
	sleep(3)

	leak = True
	aleak = False
	start = time()
	runningPSI = 0
	i = 1
	while True:
		currentTime = time()
		currentPSI = recieve.returnPSI()
		runningPSI = runningPSI + currentPSI
		i = i + 1
		if(currentPSI >= TownPSI): leak = False
		if((currentTime - start) > TIMEOUT): break

	if((runningPSI / i) < TownPSI): aleak = True

	statement = ""
	if(leak):
		statement = "Water pressure was always below town pressure: There's a silent leak!"
	else:
		if(aleak):
			statement = "On average water pressure was below town pressure: there's a silent leak"
		else:
			statement = "Your pipes are good! No silent leaks."
	return statement

