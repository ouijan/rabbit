import click
from os.path import expanduser
from config import Config
from command import Command
from group import Group


CONFIG_FILE = "rabbit.yaml"

class App(object):
	""" Base application class

	Responsible for:
	- bootstrapping
	- setting configs
	- dependency management
	- running the application
	"""
	
	def __init__ (self):
		self.config = Config()
		self.baseGroup = Group('base')
		self.bootstrap()

	def bootstrap (self):
		""" Bootstrap the application """
		self.loadHomeConfig()
		self.loadLocalConfig()
		self.loadCommands()

	def loadHomeConfig (self):
	  """ Load Config From Home Directory """
	  homepath = expanduser('~') + '/' + CONFIG_FILE
	  self.config.load(homepath)

	def loadLocalConfig (self):
	  """ Load Config From Local (Current) Directory """
	  localpath = './' + CONFIG_FILE
	  self.config.load(localpath)

	def loadCommands (self):
	 	""" Load Commands from the current configs """
	 	commands = self.config.get('commands')
	 	if commands is None:
	 		return
	 	for commandData in commands:
	 		command = Command(commandData)
	 		commandGroups = command.getGroups()
			childGroup = self.baseGroup.resolveGroups(commandGroups)
			childGroup.add(command)
	
	def run(self):		
		self.baseGroup.fire()


