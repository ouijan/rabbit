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







