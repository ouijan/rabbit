from .config import Config
from .commands import CommandCollection, Command
from os.path import expanduser

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
		self.commands = CommandCollection()
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
	 		command = self._createCommand(commandData)
	 		self.commands.add(command)
	 	return

	def _createCommand (self, commandData):
		""" Creates Command Object from the given data """
		return Command(commandData)


		