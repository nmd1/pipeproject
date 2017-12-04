
from tkinter import Tk, Label, Entry, Button, Frame,X
import keyboard
import os
import datetime

class Settings:
	def __init__(self, master):
		self.master = master
		
		pad=0
		self._geom='200x200+0+0'
		master.geometry("{0}x{1}+0+0".format( master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
		master.bind('<Escape>',self.toggle_geom)   
		
		master.title("Settings")
		self.labelnames = ['Threshold PSI','Silent Leak Timeout', \
'Silent Leak Check Time','Email', 'Wifi Network Name', 'Wifi Network Password']
		self.settingsNumb = len(self.labelnames)
		self.frames = []
		
		# Turn on the keyboard
		self.keyboardprocess = keyboard.openKeyboard()

		for n in range(self.settingsNumb+1):
			frame = Frame(master)
			frame.pack(side='top', anchor='w')
			self.frames.append(frame)

		self.entryboxes = {frame: [] for frame in self.frames}

		for i, frame in enumerate(self.frames):
			# Don't do this for the last frame
			if(i==self.settingsNumb): break

			# add label
			label = Label(frame, text=self.labelnames[i], font=('ariel',12))
			label.pack(side='left')
			
			# add textbox
			textbox = Entry(frame, width = 15)
			textbox.pack(side='left')
			self.entryboxes[frame].append(textbox)


#		self.entryboxes[0][0].insert(0, 'hello')		
		self.killButton = Button(self.frames[self.settingsNumb], text='Save', command=self.kill, height=10, width=100)
		self.killButton.pack()		

	def kill(self):
		# Save settings
		print('killing myself')
		keyboard.closeKeyboard(self.keyboardprocess)
		self.master.destroy()
		
	def greet(self):
		print("Greetings!")

	def toggle_geom(self,event):
		geom=self.master.winfo_geometry()
		print(geom,self._geom)
		self.master.geometry(self._geom)
		self._geom=geom

# settings functions
class SettingsHandler:
	
	def __init__(self):
		self.exists = os.path.exists('config')
		self.leakInterval = 3	
		self.config = []
		# self.tpsi = 0
		# self.leaktime = ""
		# self.email = ""
		# self.wifiNet = ""
		# self.wifiPass = ""

	def exists(self):
		return os.path.exists('config')

	def getData(self):
		if(not self.exists()):
	                setroot = Tk()
	                set_gui = Settings(setroot)
		else:
			with open('config','r') as file:
				self.config = [l.strip() for l in file]
				
	def setData(changelist):
		for value,i in changelist:
			if(value==""): continue
			self.config[i] = value
	
	
			


