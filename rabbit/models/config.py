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
			self.data = self._update(self.data, fileData);
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

	def _update(self, origData, newData):
		origData = newData
		pass


