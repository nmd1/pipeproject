from tkinter import Tk, Label, Button
import datetime
import time
import easygui
from recieve import returnPSI
from settings import Settings
from sleaks import silentLeak
from logview import Logs
from gmail3 import *
import valve

class TheGUI:
	def __init__(self, master):
		self.master = master
		LEFT = 'left'		
		self.master=master
		pad=3
		self._geom='200x200+0+0'
		master.geometry("{0}x{1}+0+0".format( master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
		master.bind('<Escape>',self.toggle_geom)   
	
		master.title("YES, PVC")
				
		self.pressureTitle = Label(master, text="Water Pressure", font=("arial",24))
		self.pressureTitle.pack()

		self.pressure = Label(master, text="[Pressure should appear here]", font=("Courier",42))
		self.pressure.pack()
		self.origColor = self.pressure.cget("background")


		self.status = Label(master, text="")
		self.status.pack()

		self.settingsB = Button(master, text="Settings", command=self.settings, height = 5)
		self.settingsB.pack(side=LEFT)

		self.silentB = Button(master, text="Silent Leak Check (now)", command=self.leak, height=5)
		self.silentB.pack(side=LEFT)

		self.logB = Button(master, text="View Logs", command=self.viewLog, height=5)
		self.logB.pack(side=LEFT)

		self.sendlogB = Button(master, text="Toggle Valve", command=self.toggle,height=5)
		self.sendlogB.pack(side=LEFT)

		self.vstate = True
		valve.open()

	def updatePSI(self,update):
		#update psi
		state = Settings()
		state.refresh()
		psi = returnPSI()
		if(type(psi)==type("noo")):
			newPressure = psi + ""
			self.pressure['font'] = ('Courier',20)
		else:
			psi = round(psi,3)
			self.log(psi)
			newPressure = str(psi) + " psi"
			self.pressure['font'] = ('Courier',42)

		if(update):
			self.pressure['text'] = newPressure
			self.pressure.update()

			# are the values too high/low?
			upperbound = state.get('upsi')
			lowerbound = state.get('lpsi')
			email = state.get('email')
			# Change colors if they are
			self.pressure['bg'] = self.origColor
			if (not type(psi) == type('dangit')):
				if (psi > float(upperbound)):
					# TOO HIGH
					valve.close()
					print('pressure high')
					sendEmail('The Valve Pressure is too high!', email)
					self.pressure['bg'] = 'red'

				if (psi < float(lowerbound)):
					# Too low
					sendEmail('The Valve Pressuer is too low', email)
					print('pressure low')
					self.pressure['bg'] = 'gold'

		#is it silent leak time?
		timeNow = time.strftime('%H:%M')

		timeSet = state.get('leaktime')
		if(timeNow == timeSet):
			self.leak()






	def settings(self):
		state = Settings()
		state.refresh()
		options = state.getKeys()
		options.append('wifi')
		self.master.withdraw()
		option = easygui.buttonbox("Tap a button to view or change it's setting", "Tap a button to view or change it's setting", options)
		state.set(option)
		state.save()
		self.master.deiconify()

	def leak(self):
		self.status['text'] = 'Checking for silent leaks'
		state = Settings()
		state.refresh()
		result = silentLeak(int(state.get('ltimeout')))
		self.status['text'] = result
		# Check for silent leaks now

	def log(self,psi):
		# Get a timestamp and put the data into a file 
		stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') 
		out = stamp + "> " + str(psi)
		with open('logs','a') as file:
			file.write(str(out)+'\n')

	def viewLog(self):
		# view the lgos
		logroot = Tk()
		log_gui = Logs(logroot)
		log_gui.update_textbox()
		
	def toggle(self):
		self.vstate = not self.vstate
		valve.change(self.vstate)
		
	def toggle_geom(self,event):
		geom=self.master.winfo_geometry()
		print(geom,self._geom)
		self.master.geometry(self._geom)
		self._geom=geom

# root = Tk()
# my_gui = TheGUI(root)
# root.mainloop()
