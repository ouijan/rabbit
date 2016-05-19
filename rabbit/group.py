import click
from . import clickObject

# Needs Tests
class Group(clickObject.ClickObject):
	""" Group Class
	The main purpose of this class is to store Commands.
	It will registed a click group and any commands added 
	to this group will be registered on the click group.
	
	Responsabilities:
		- Tracking commands in a group
		- Building a click Group object
		- Handling how a click Group is called
	"""

	def __init__ (self, name = None):
		""" Build click object & store children

		@param string name - the name of this group
		"""
		super(Group, self).__init__(name)
		self.children = []

	def build(self):
		return click.Group(self.name)

	# Needs Tests
	def run(self):
		""" Define when to do when this object is run
		@return mixed - group run response
		"""
		return self.click()

	# Needs Tests
	def add(self, child):
		""" Handle adding a command/group to this group
		@params object 	child - child to add
		@return	boolean				- True if successfull
		"""
		self.children.append(child)
		childClick = child.getClick()
		self.getClick().add_command(childClick)
		return True


	# Needs Tests
	def resolveGroup(self, name):
		"""
		Either finds the group or creates a new one and 
		returns it. It does this for the given command name

		@param 	string name - the name of the requested group
		@return Group  			- the group to add to
		"""
		for child in self.children:
			if isinstance(child, (Group)) and child.name == name:
				return child
		newGroup = Group(name)
		self.add(newGroup)
		return newGroup


	# Needs Tests
	def resolveGroups(self, groups):
		"""
		Recursive function that sifts through an array of 
		groups and returns the lowest level group. That is
		the group that a command is added to.
	
		@param 	List	groups - an array of (string) group names
		@return Group 			 - The resolved group
		"""
		if len(groups) > 0:
			group = self.resolveGroup(groups[0])
			return group.resolveGroups(groups[1::])
		return self
