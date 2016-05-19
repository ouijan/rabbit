import click

"""
ABSTRACT CLASS: 
THIS SHOULD NEVER BE INSTANTIATED DIRECTLY
"""

class ClickObject(object):
	""" ClickObject 'Abstract' Class
	The main purpose of this class is to help abstract click,
	in the case that it needs to replaced later. This is also
	the perfect place to extend upon the click library.
	
	Responsabilities:
		- Accessing click Object
		- Handling click context
		- Contracting a build method to be defined by subclasses
		- Contracting a run method to be defined by subclasses
	"""
	
	def __init__ (self, name = None):
		""" Constructor method.
		@param	string name - the name or path of this ClickObject.
		"""
		self.name = name
		self.context = {
			'allow_extra_args': True,
			'allow_interspersed_args': True,
		}
		self.click = self.build();


	def getClick(self):
		""" Get the click data object of this ClickObject.
		@return object Click Command or Group
		"""
		return self.click


	def getCallback(self):
		""" Get the callback method bound to the current context 
		@return function - function ready for click decoration
		"""
		return click.pass_context(self.run)


	def build(self):
		""" build a click object for this ClickObject
		@raise NotImplementedError - abstract method
		"""
		raise NotImplementedError('Subclasses must override this method!')


	def run(self):
		""" Define what is called when this click object is hit 
		@raise NotImplementedError - abstract method
		"""
		raise NotImplementedError('Subclasses must override this method!')
