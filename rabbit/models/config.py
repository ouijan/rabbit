import yaml
import io
import copy

class Config(object):
	"""Config class for managing rabbit's configuration

	Responsible for:
	- loading configs
	- storing configs
	"""

	def __init__ (self):
		self.data = {}


	def get(self, key, default = None):
		"""Get the value of a config item

		- (string) key: the data key to access
		- (mixed) default: value to return if not found
		"""
		try:
			return self.data[key]
		except:
			return default


	def load(self, filepath):
		"""Load a file into the config from filepath

		- (string) filepath: the path to the file in the os
		"""
		fileData = self._read(filepath)
		if fileData is not None:
			self.data = self._merge(self.data, fileData);
			return True
		return False


	def _read (self, filepath):
		"""Reads the given filepath and returns a dict

		- (string) filepath: the path to the file in the os
		"""
		try:
			stream = io.open(filepath, 'r')
			value = yaml.safe_load(stream)
			return value
		except:
			return None

	def _merge(self, oldData, newData):
		"""Recursively merges two data objects

		Handles merging lists, dicts, and non-iterables. This has not been
		tested for tuples. It will not affect either of the original objects.

		- (mixed) oldData: the data to update
		- (mixed) newData: the data to override with
		"""
		origData = copy.copy(oldData)
		try:

			# if they are both lists just concat them
			if isinstance(origData, list) and isinstance(newData, list):
				return origData + newData

			# Set the iterator or return newData
			iterator = None
			if isinstance(newData, list): iterator = enumerate(newData)
			elif isinstance(newData, dict): iterator = newData.items()	
			else: origData = newData

			# Iterate through setting values
			for key, val in iterator:
				
				# Get old value
				oldVal = None
				try: oldVal = origData[key]
				except: pass

				# If new value isnt None
				if val is not None:
					origData[key] = self._merge(origData[key], newData[key])
					
				# If it is none and old value not found, set the key
				elif oldVal is None:
					origData[key] = None

			# return the modified Data
			return origData
		except:
			return newData

