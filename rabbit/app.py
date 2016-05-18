import sys
import click
import pkg_resources
from os.path import expanduser
from . import config
from . import command
from . import group
from . import flags
from . import settings
from . import display


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
		self.name = settings.NAME
		self.version = self.getVersion();
		self.bootstrap()

	def bootstrap (self):
		""" Bootstrap the application """
		self.loadHomeConfig()
		self.loadLocalConfig()
		self.loadCommands()
		flags.addAll(self)

	def loadHomeConfig (self):
		""" Load Config From Home Directory """
		homepath = expanduser('~') + '/' + settings.CONFIG_FILE
		self.config.load(homepath)

	def loadLocalConfig (self):
		""" Load Config From Local (Current) Directory """
		localpath = './' + settings.CONFIG_FILE
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
		""" adds a command to the base group """
		if not isinstance(cmd, (command.Command)):
			return False
		commandGroups = cmd.getGroups()
		childGroup = self.baseGroup.resolveGroups(commandGroups)
		childGroup.add(cmd)
		return True

	def createCommand(self, commandData):
		""" creates a command object """
		return command.Command(commandData)

	def run(self):
		""" executes the click basegroup object """
		self.baseGroup.fire()

	def getVersion(self):
		"""
		Finds the installed version of this package/application
		Uses pkg_resources and self.name to determine installed
		packages and the version of that package installed.
		"""
		module = self.name
		dist = pkg_resources.get_distribution(module)
		return dist.version

