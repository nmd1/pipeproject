import subprocess


def openKeyboard():
	p = subprocess.Popen(["xvkbd"])
	print("Process ID of subprocess " + str(p.pid))
	return p


def closeKeyboard(p):
	p.terminate()
	# Wait for process to terminate
	returncode = p.wait()
	print ("Returncode of subprocess: " + str(returncode))
