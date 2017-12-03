from tkinter import Tk, Label, Button
from recieve import returnPSI

class TheGUI:
	def __init__(self, master):
		self.master = master
		master.title("Current Pressure")

		self.pressureTitle = Label(master, text="Current Pressure Readings")
		self.pressureTitle.pack()
		self.pressure = Label(master, text="[Pressure should appear here]")
		self.pressure.pack()

		self.greet_button = Button(master, text="Greet", command=self.greet)
		self.greet_button.pack()

		self.close_button = Button(master, text="Close", command=master.quit)
		self.close_button.pack()

	def updatePSI(self):
		newPressure = str(returnPSI())
		self.pressure['text'] = newPressure
		self.pressure.update()

	def greet(self):
		print("Greetings!")

# root = Tk()
# my_gui = TheGUI(root)
# root.mainloop()
