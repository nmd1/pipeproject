
from tkinter import Tk, Label, Entry, Button, Frame,X
import keyboard
import os
import easygui
from network import *
import datetime

# settings functions
class Settings:
	
	def __init__(self):
		self.exists = os.path.exists('config')
		self.config = {}
		self.config['upsi'] = 0
		self.config['lpsi'] = 0
		self.config['ltimeout'] = 60
		self.config['leaktime'] = ""
		self.config['email'] = ""
		self.config['wifiNet'] = ""
		self.config['wifipass'] = ""

	def exists(self):
		# does the config file current exist?
		return os.path.exists('config')

	def getKeys(self):
		return list(self.config.keys())


	def refresh(self):
		# Get data from config file
		keys = self.config.keys()
		infolist = []
		with open('config','r') as file:
				infolist = [l.strip() for l in file]
		i = 0
		for keys in self.config:
			self.config[keys] = infolist[i]
			i = i + 1


	def save(self):
		# save data to config file
		with open('config','w') as file:
			for key in self.config:
				file.write(self.config[key] + '\n')


	def set(self, setting):
		# set a setting
		if (not setting in self.config.keys()):
			if ('wifi' in setting):
				wifistate = isInternet()
				if(wifistate): wifistate = 'Connected'
				else: wifistate = 'Disconnected'

				username = easygui.enterbox('Enter New username', 'Wifi Username - ' + wifistate, )
				newpass = easygui.multpasswordbox('Password', 'Enter your password - ' + wifistate, ['Save, Cancel'])

				if(username == None or newpass == None): return False
				else: connect(username, newpass)
			return False

		val = easygui.enterbox(str('Enter Setting for' + setting +'. Currently ' + self.config[setting]),setting)
		if(not val == None): self.config[setting] = val

		if(setting == 'upsi' or setting == "ltimeout" or setting=='lpsi'): self.config[setting] = float(val)




	def get(self, setting):
		# get a setting
		if (not setting in self.config.keys()):
			return False
		return self.config[setting]

	
			


