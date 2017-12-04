from tkinter import Tk, Label, Button
from recieve import returnPSI
from settings import Settings
from sleaks import silentLeak

class TheGUI:
	def __init__(self, master):
		self.master = master
		LEFT = 'left'		
		self.master=master
		pad=3
		self._geom='200x200+0+0'
		master.geometry("{0}x{1}+0+0".format( master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
		master.bind('<Escape>',self.toggle_geom)   
	
		master.title("Water Pressure Monitor")
		
		

		self.pressureTitle = Label(master, text="Water Pressure", font=("arial",24))
		self.pressureTitle.pack()

		self.pressure = Label(master, text="[Pressure should appear here]", font=("Courier",42))
		self.pressure.pack()

		self.settingsB = Button(master, text="Settings", command=self.settings, height = 5)
		self.settingsB.pack(side=LEFT)

		self.silentB = Button(master, text="Silent Leak Check (now)", command=self.leak, height=5)
		self.silentB.pack(side=LEFT)

		self.logB = Button(master, text="View Logs", command=self.log, height=5)
		self.logB.pack(side=LEFT)

		self.sendlogB = Button(master, text="Send Logs to Email", command=master.quit,height=5)
		self.sendlogB.pack(side=LEFT)

		
	def updatePSI(self):
		psi = returnPSI()
		if(type(psi)==type("noo")):
			newPressure = psi + ""
			self.pressure['font'] = ('Courier',20)

		else:
			psi = round(psi,3)
			self.log(psi)
			newPressure = str(psi) + " psi"
			self.pressure['font'] = ('Courier',42)

		self.pressure['text'] = newPressure
		self.pressure.update()

	def greet(self):
		print("Greetings!")

	def settings(self):
		setroot = Tk()
		set_gui = Settings(setroot)
		
	def leak(self):
		result = silentLeak()
		self.status['text'] = result
		# Check for silent leaks now

	def log(self,psi):
		with open('logs','a') as file:
			file.write(str(psi)+'\n')
		# view the logs

	def sendlog(self):
		pass
		# send logs over email to user

	def toggle_geom(self,event):
		geom=self.master.winfo_geometry()
		print(geom,self._geom)
		self.master.geometry(self._geom)
		self._geom=geom

# root = Tk()
# my_gui = TheGUI(root)
# root.mainloop()
