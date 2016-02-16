#!.env/bin/python
from config import Config

class App():
	""" 
	Base application class.
	Used to setup, configure & run the application. 
	"""
	configFile = "rabbit.yaml"

	def __init__ (self):
		"""
		Constructor/Init function
		"""
		self.loadGlobalConfig()
		self.loadLocalConfig()
		self.buildCommands()

	def loadGlobalConfig(self):
		"""
		Loads the global config from the users home directory
		and stores it in the globalConfig property of the app
		"""
		homepath = expanduser("~") + "/" + configFile;
		if self.configs is None:
			self.configs = {}
		self.configs.global = Config(homepath)

	def loadLocalConfig(self):
		"""
		Loads the local config from the users current directory
		and stores it in the localConfig property of the app
		"""
		localpath = "./" + configFile;
		if self.configs is None:
			self.configs = {}
		self.configs.local = Config(localpath)

	def buildCommands(self):
		"""
		Polupates the self.commands dict with commands objects
		built from the loaded configs
		"""
		self.commands = {}
		# load global commands
		try {
			for commandData in self.globalConfig.commands:
				self.commands[commandData.hop] = Command(commandData)
		}
		# load local commands
		try {
			for commandData in self.localConfig.commands:
				self.commands[commandData.hop] = Command(commandData)
		}
		