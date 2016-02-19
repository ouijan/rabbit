#!.env/bin/python
import yaml
import io

class Config (object):
	""" 
	Config class for managing rabbit's configuration

	Responsible for :
	- loading configs
	- storing configs
	"""

	def __init__ (self):
		self.data = {}


	def get(self, key, default = None):
		"""
		Get the value of a config item
		"""
		try:
			return self.data[key]
		except:
			return default


	def load(self, path):
		"""
		Load a file into the config from path
		"""
		fileData = self._read(path)
		if fileData is not None:
			self.data = self._merge(self.data, fileData);
			return True
		return False


	def _read (self, filepath):
		"""
		Reads the given filepath and returns a dict
		"""
		try:
			stream = io.open(filepath, 'r')
			value = yaml.safe_load(stream)
			return value
		except:
			return None

	def _merge(self, origData, newData):
		try:

			# Set the iterator or return newData
			iterator = None
			if isinstance(newData, list): iterator = enumerate(newData)
			elif isinstance(newData, dict): iterator = newData.items()	
			else: origData = newData

			# Iterate through setting values
			for key, val in iterator:
				# If new value isnt None
				if val is not None:
					origData[key] = self._merge(origData[key], newData[key])

			# return the modified Data
			return origData
		except:
			return newData

