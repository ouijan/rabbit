#!.env/bin/python
import subprocess

class Command (object):
	""" 
	Command class for managing a rabbit command

	Responsible for:
	- comparing this command to an input command
	"""

	def matches(self, input):
		""" Checks the input command matches this command """
		pass

	def run(self, input):
		""" runs this command given the input command """
		# subprocess.call(command, shell=True);
		pass