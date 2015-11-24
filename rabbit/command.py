#!.env/bin/python
import subprocess

class Command (object):
	""" 
	Command class for managing a rabbit command

	Responsible for:
	- comparing this command to an input command
	"""

	def __init__ (self, data):
		"""
		Constructor/Init function
		"""
		self.hop = data['hop']
		self.to = data['to']
		self.description = "runs '" + self.to + "'"
		if 'description' in data: self.description = data['description']

	def matches(self, compCommand):
		""" 
		Checks the input command matches this command 
		"""
		matches = True
		for index, letter in enumerate(self.hop):
			if letter is not compCommand[index]:
				matches = False
				break;
		return matches

	def run(self, input):
		"""
		Runs this command given the input command 
		"""
		command = self.to
		subprocess.call(command, shell=True);
		pass