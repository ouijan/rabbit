import click
from . import command

# Needs Tests
class Group(object):

	def __init__ (self, name = None):
		self.children = []
		self.name = name
		self.clickObj = click.Group(name=name)

	# Needs Tests
	def getClickObject(self):
		return self.clickObj

	# Needs Tests
	def fire(self):
		self.clickObj()

	# Needs Tests
	def add(self, child):
		if isinstance(child, (command.Command)) and not child.isValid():
			return False
		self.children.append(child)
		clickObj = child.getClickObject()
		self.clickObj.add_command(clickObj)
		return True

	# Needs Tests
	def resolveGroup(self, name):
		for child in self.children:
			if isinstance(child, (Group)) and child.name == name:
				return child
		newGroup = Group(name)
		self.add(newGroup)
		return newGroup

	# Needs Tests
	def resolveGroups(self, groups):
		if len(groups) > 0:
			group = self.resolveGroup(groups[0])
			return group.resolveGroups(groups[1::])
		return self
