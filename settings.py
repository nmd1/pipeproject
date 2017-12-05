
from tkinter import Tk, Label, Entry, Button, Frame,X
import keyboard
import os
import easygui
from network import *
import datetime
from keyboard import *
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
			for line in file:
				if(line == '\n'): continue
				(key,val) = line.split()
				self.config[key] = val

		
	def save(self):
		# save data to config file
		with open('config','w') as file:
			for key in self.config:
				file.write(str(key) +" "+ str(self.config[key]) + '\n')


	def set(self, setting):
		# set a setting
		pro = openKeyboard()
		if ('wifi' in setting):
			wifistate = isInternet()
			if(wifistate): wifistate = 'Connected'
			else: wifistate = 'Disconnected'
			username = easygui.enterbox('Enter New username', 'Wifi Username - ' + wifistate, )
			newpass = easygui.multpasswordbox('Password', 'Enter your password - ' + wifistate, ['Save, Cancel'])
			closeKeyboard(pro)
			if(username == None or newpass == None): return False
			else: 
				connect(username, newpass)
				return True
		if(not setting in self.config.keys()):
			return False

		val = easygui.enterbox('Enter Setting for ' + str(setting) +'. Currently ' + str(self.config[setting]),str(setting))
		closeKeyboard(pro)
		if(val == None): return val 


		self.config[setting] = val
		if(setting == 'upsi' or setting == "ltimeout" or setting=='lpsi'): self.config[setting] = float(val)




	def get(self, setting):
		# get a setting
		if (not setting in self.config.keys()):
			return False
		return self.config[setting]

	
			


