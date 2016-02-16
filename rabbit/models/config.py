#!.env/bin/python
import os
import yaml
from command import Command

class Config (object):
	""" 
	Config class for managing rabbit's configuration

	Responsible for :
	- finding config file based on current working directory
	- loading a config file
	- keeping a track of active rabbit.yaml files
	- providing the available commands / configuration
	"""
	
	fileName = "rabbit.yaml"
	searchDepth = 3

	def __init__ (self):
		self.commands = []
	
	def find (self):
		""" 
		finds config file based on current working directory 
		"""
		fileFound = False
		depth = 0
		while (fileFound == False and depth < self.searchDepth):
			search = './'
			for index in range(depth):
				search += '../'
			search += self.fileName
			if os.path.isfile(search):
				fileFound = search
			depth += 1
		return fileFound

	def read (self, filepath):
		"""
		Reads the given filepath and returns a dict
		"""
		try:
			stream = file(filepath, 'r')
			value = yaml.load(stream)
			return value
		except:
			return None

	def load (self, configDict):
		"""
		Loads the given config dict into this config
		"""
		if configDict is None: return False
		for command in configDict['commands']:
			self.commands.append( Command(command) )
		return None

	def findCommand (self, givenCommand):
		"""
		Finds the first matching command in the commands list
		"""
		found = None
		for command in self.commands:
			if command.matches(givenCommand):
				found = command
				break;
		return found

	def displayHelp (self):
	  """
	  translates config into help and prints it
	  """
	  print "\033[1m\033[4m\033[32mRabbit Command Line Hopper \033[0m"
	  for command in self.commands:
	    default = "runs '" + command.to + "'"
	    print "\033[1m\033[36m%-20s \033[0m %-10s" % (command.hop, command.description)
		