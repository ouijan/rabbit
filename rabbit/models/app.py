from .config import Config
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
		self.bootstrap()

	def bootstrap(self):
		"""Bootstrap the application"""
		self.loadHomeConfig()
		self.loadLocalConfig()

	def loadHomeConfig (self):
	  """Load Config From Home Directory"""
	  homepath = expanduser('~') + '/' + CONFIG_FILE
	  self.config.load(homepath)

	def loadLocalConfig (self):
	  """Load Config From Local (Current) Directory"""
	  localpath = './' + CONFIG_FILE
	  self.config.load(localpath)

		