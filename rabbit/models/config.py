#!.env/bin/python
import yaml

class Config (object):
	""" 
	Config class for managing rabbit's configuration

	Responsible for :
	- loading configs
	- storing configs
	"""
	fileName = "rabbit.yaml"

	def __init__ (self):
		self.data = {}


	def get(self, item, default = None):
		"""
		Get the value of a config item
		"""
		if self.data.get(item) is not None:
			return self.data.get(item)
		return default


	def load(self, path):
		"""
		Load a file into the config from path
		"""
		fileData = self._read(path)
		if fileData:
			self._update(self.data, fileData);
			return True
		return False

	def _read (self, filepath):
		"""
		Reads the given filepath and returns a dict
		"""
		try:
			stream = file(filepath, 'r')
			value = yaml.load(stream)
			return value
		except:
			return None

	def _update(self, origData, newData):
		origData = newData
		pass


