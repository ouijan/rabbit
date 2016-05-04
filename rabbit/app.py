import click
from os.path import expanduser
from . import config
from . import command
from . import group

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
		self.config = config.Config()
		self.baseGroup = group.Group('base')
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
			return False
		for commandData in commands:
			cmd = self.createCommand(commandData)
			self.addCommand(cmd)
		return True

	def addCommand(self, cmd):
		if not isinstance(cmd, (command.Command)):
			return False
		commandGroups = cmd.getGroups()
		childGroup = self.baseGroup.resolveGroups(commandGroups)
		childGroup.add(cmd)
		return True

	def createCommand(self, commandData):
		return command.Command(commandData)
	
	def run(self):		
		self.baseGroup.fire()


