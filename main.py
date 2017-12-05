from tkinter import Tk, Label, Button
from recieve import returnPSI
from gui import TheGUI
import time
print("MAIN PROGRAM RUNNING")

root = Tk()
my_gui = TheGUI(root)
# root.mainloop()

reset = True
while True:
	if(reset): 
		start_time = time.time()
		reset = False
	if(time.time() - start_time > 2):
		my_gui.updatePSI(True)
		reset = True
	else:
		my_gui.updatePSI(False)
