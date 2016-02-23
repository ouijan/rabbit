class CommandCollection(object):
	""" CommandCollection Class

	Responsible for:
	- Keeping a track of multiple commands
	"""
	
	def __init__ (self):
		self._collection = []

	def add(self, command):
		""" Add a command to the collection """
		pass

	def remove(self, command):
		""" remove a command from the collection """
		pass

	def registerAll(self):
		""" runs the register method of all commands """
		pass