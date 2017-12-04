from tkinter import Tk, Label, Button
from recieve import returnPSI

class TheGUI:
	def __init__(self, master):
		self.master = master
		
		self.master=master
		pad=3
		self._geom='200x200+0+0'
		master.geometry("{0}x{1}+0+0".format( master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
		master.bind('<Escape>',self.toggle_geom)   
	
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

	def toggle_geom(self,event):
		geom=self.master.winfo_geometry()
		print(geom,self._geom)
		self.master.geometry(self._geom)
		self._geom=geom

# root = Tk()
# my_gui = TheGUI(root)
# root.mainloop()
