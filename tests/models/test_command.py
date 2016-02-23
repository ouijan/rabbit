import unittest
import mock
from rabbit.models.Command import *

class TestCommand(unittest.TestCase):

	def test_it_creates_a_new_object(self):
		command = Command()
		self.assertTrue(isinstance(command, (Command)))

	"""
	Requires data.hop on init
	"""
	def test_it_sets_hop_data_on_init(self):
		data = {'to': 'foo', 'hop': 'bar'}
		command = Command(data)
		self.assertEquals(command.data['hop'], 'bar')

	def test_it_handles_missing_hop_data_on_init(self):
		data = {'to': 'foo', 'hop': None}
		command = Command(data)
		self.assertEquals(command.data['hop'], None)

	def test_it_handles_empty_hop_data_on_init(self):
		data = {'to': 'foo', 'hop': None}
		command = Command(data)
		self.assertEquals(command.data['hop'], None)

	"""
	Requires data.to on init
	"""
	def test_it_sets_to_data_on_init(self):
		data = {'to': 'foo', 'hop': 'bar'}
		command = Command(data)
		self.assertEquals(command.data['to'], 'foo')

	def test_it_handles_missing_to_data_on_init(self):
		data = {'to': None, 'hop': 'bar'}
		command = Command(data)
		self.assertEquals(command.data['to'], None)

	def test_it_handles_empty_to_data_on_init(self):
		data = {'to': None, 'hop': 'bar'}
		command = Command(data)
		self.assertEquals(command.data['to'], None)

	"""
	Sets data.description on init
	"""
	def test_it_sets_description_data_on_init(self):
		data = {'to': 'foo', 'hop': 'bar', 'description': 'test'}
		command = Command(data)
		self.assertEquals(command.data['description'], 'test')

	@mock.patch('rabbit.models.Command.Command.generateDescription')
	def test_it_sets_missing_description_data_on_init(self, gen_desc):
		data = {'to': 'foo', 'hop': 'bar'}
		gen_desc.return_value = 'test'
		command = Command(data)
		gen_desc.assert_called_with()
		self.assertEquals(command.data['description'], 'test')

	@mock.patch('rabbit.models.Command.Command.generateDescription')
	def test_it_handles_empty_description_data_on_init(self, gen_desc):
		data = {'to': 'foo', 'hop': 'bar', 'description': None}
		gen_desc.return_value = 'test'
		command = Command(data)
		gen_desc.assert_called_with()
		self.assertEquals(command.data['description'], 'test')

	"""
	generateDescription - can generate a description
	"""
	def test_it_can_generate_a_description(self):
		data = {'to': 'foo', 'hop': 'bar'}
		desc = Command(data).generateDescription()
		self.assertEquals(desc, 'Alias for: foo')

	def test_it_handles_no_to_data(self):
		data = {}
		desc = Command(data).generateDescription()
		self.assertEquals(desc, '')


	"""
	isValid - can check if it is valid
	"""
	def test_isValid_passes(self):
		data = {'to': 'foo', 'hop': 'bar'}
		command = Command(data)
		self.assertTrue(command.isValid())

	def test_isValid_fails_when_hop_data_None(self):
		data = {'to': 'foo', 'hop': None}
		command = Command(data)
		self.assertFalse(command.isValid())

	def test_isValid_fails_when_to_data_None(self):
		data = {'to': None, 'hop': 'bar'}
		command = Command(data)
		self.assertFalse(command.isValid())
