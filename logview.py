from tkinter import Tk, Label, Text, Button, DISABLED, NORMAL, INSERT
import keyboard 
import os 
import datetime
from gmail3 import sendFile
from settings import SettingsData


class Logs:
	def __init__(self, master):
		self.master = master
		
		w, h = master.winfo_screenwidth(), master.winfo_screenheight()
		master.geometry("%dx%d+0+0" % (w, h))	


		master.title("Logs")
		

		#label = Label(master, text=self.labelnames[i], font=('ariel',12))
		#label.pack()

		
		self.logbox = Text(master, state=DISABLED, height = 15, width=200)
		self.logbox.pack()
		w = 27
		h = 5
		self.killButton = Button(master, text='Exit', command=self.kill, height=h,  width=w)
		self.killButton.pack(side='left')
		self.emailButton = Button(master,text='Send Email',command=self.sendAway, height=h, width=w)
		self.emailButton.pack(side='left')
		

	def kill(self):
		# Save settings
		print('killing myself [logs]')
		self.master.destroy()
		
	def sendAway(self):
		s = SettingsData()
		email = s.getEmail()
		sendFile('Pressure Data!',email,'logs')
		pass
	
	def update_textbox(self):
		text = ''
		tally = 0
		i = 0
		with open('logs','r') as file:
			for line in file:
				text = text + line
				val = 0
				try:
					l = line.partition("> ")[2]
					val = float(l)
					tally = tally + val
					i = i + 1
				except ValueError:
					pass
		if(not i ==0): avg = (tally / i)
		else: avg = 0

		self.master.title("Logs: Average is " + str(round(avg,2)) + " psi")	
		self.logbox['state'] = NORMAL
		self.logbox.insert(INSERT,text)
		self.logbox['state'] = DISABLED
