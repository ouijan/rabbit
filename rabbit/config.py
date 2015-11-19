#!.env/bin/python
import os
import yaml

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
		while (fileFound == False and depth < searchDepth):
			search = './'
			for index in range(depth):
				search += '../'
			search += config['fileName']
			if os.path.isfile(search):
				fileFound = search
			depth += 1
		return fileFound

	@staticmethod
	def load (self, configDict):
		"""
		Loads the given config dict into this config
		"""
		stream = file(filepath, 'r')
		value = yaml.load(stream)
		return value



	