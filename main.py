from tkinter import Tk, Label, Button
from recieve import returnPSI
from gui import TheGUI
import time
print("MAIN PROGRAM RUNNING")

root = Tk()
my_gui = TheGUI(root)
# root.mainloop()

while True:
	my_gui.updatePSI()
	time.sleep(.01)
