

class Command(object):
	""" Command Class

	Responsible for:
	- Storing a command data
	- Registering a command
	- Calling a command
	"""
	
	def __init__ (self, data = {}):
		self.data = {}
		# Set to and Hop
		self.data['hop'] = data.get('hop')
		self.data['to'] = data.get('to')
		# Set Description
		self.data['description'] = data.get('description')
		if self.data['description'] is None:
			self.data['description'] = self.generateDescription()

	def generateDescription(self):
		""" Generates a basic description based on the commands properties """
		toCommand = self.data.get('to')
		if toCommand:
			return 'Alias for: ' + self.data.get('to');
		return ''

	def isValid(self):
		""" Checks if this command is valid """
		if self.data.get('hop') is None:
			return False
		if self.data.get('to') is None:
			return False
		return True

	def register(self):
		""" Registers the command in click """
		pass


class CommandCollection(object):
	""" CommandCollection Class

	Responsible for:
	- Keeping a track of multiple commands
	"""
	
	def __init__ (self):
		self._data = []

	def __iter__(self):
		return iter(self._data)

	def add(self, command):
		""" Add a command to the collection 
		Behavior:
		- Return False if it is not a command
		- Return False if command is not valid
		- If Command exists remove it in order to replace
		- Add Command and return True
		Parameters:
		- command (Command): command to add to collection
		"""
		if not isinstance(command, (Command)):
			return False
		if not command.isValid():
			return False
		exists = self.getCommand(command.data.get('hop'))
		if exists:
			self.remove(exists)
		self._data.append(command)
		return True

	def remove(self, command):
		""" remove a command from the collection """
		self._data.remove(command)

	def getCommand(self, hop):
		""" returns the command with the given hop """
		for command in self._data:
			if command.data.get('hop') is hop:
				return command
		return None

	def registerAll(self):
		""" runs the register method of all commands """
		for command in self._data:
			command.register()

		