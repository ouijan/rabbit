import click
import subprocess
import sys
from . import group

def transformData(data = {}):
	""" Take a yaml command decleration and 
	transoform it into a command object.
	@param		dict			data - simple command object
	@return		Command 	 		 - command object or None
	"""
	hop = data.get('hop')
	to = data.get('to')
	description = data.get('description')
	if hop is None or to is None:
		return None
	return Command(hop, to, description)


class Command(group.Group):
	""" Command Class

	Responsible for:
	- Storing command data
	- Calling a command
	"""
	
	def __init__ (self, hop, to, description = None):
		""" Command Object Constructor
		@param string hop					- registered trigger
		@param string to					- proxied command
		@param string description	-	command info
		"""
		self.data = {}
		self.data['hop'] = hop
		self.data['to'] = to
		self.data['description'] = description;
		if self.data['description'] is None:
			self.data['description'] = self.generateDescription()

		# Run parent constructor with this name
		super(Command, self).__init__(self.getName());
		self.groups = self.getGroups()


	# Needs Tests
	def build(self):
		""" sets the click object of this command 
		@return click.command
		"""
		return click.command(
			name = self.getName(),
			help = self.data.get('description'),
			context_settings = self.context
		)(self.getCallback())


	# Needs Tests
	def run(self, context):
		""" Runs the given command 
		@param object context - contains input info
		"""
		toCommand = self.data.get('to')
		extraArgs = ' '.join(context.args)
		runCommand = '{0} {1}'.format(toCommand, extraArgs)
		sys.exit(subprocess.call(runCommand, shell=True))


	def generateDescription(self):
		""" Generates a basic description 
		@return string - generated description
		"""
		toCommand = self.data.get('to')
		if toCommand:
			return 'Alias for: ' + self.data.get('to');
		return ''


	def getGroups(self):
		""" Gets all the groups for this command 
		@return list - array or parent commands in order
		"""
		hop = self.data.get('hop')
		if hop is None:
			return []
		segmented = hop.split(' ')
		return segmented[:-1]


	def getName(self):
		""" Determines the name of this command 
		@return string - the last word of the hop command
		"""
		hop = self.data.get('hop')
		if hop is None:
			return None
		segmented = hop.split(' ')
		return segmented[-1]