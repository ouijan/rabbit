import unittest
from mock import *
from rabbit.commands import *

class TestCommand(unittest.TestCase):
	""" Test suite for the Command class"""

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

	@patch('rabbit.commands.Command.generateDescription')
	def test_it_sets_missing_description_data_on_init(self, gen_desc):
		data = {'to': 'foo', 'hop': 'bar'}
		gen_desc.return_value = 'test'
		command = Command(data)
		gen_desc.assert_called_with()
		self.assertEquals(command.data['description'], 'test')

	@patch('rabbit.commands.Command.generateDescription')
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


class TestCommandCollection(unittest.TestCase):
	""" Test suite for the CommandCollection class"""
	
	def test_it_creates_a_new_object(self):
		collection = CommandCollection()
		self.assertTrue(isinstance(collection, (CommandCollection)))

	def test_it_sets_a_private_data_property(self):
		collection = CommandCollection()
		self.assertEquals(collection._data, [])

	"""
	add - test it can add to the collection
	"""
	def test_it_will_reject_None(self):
		collection = CommandCollection()
		collection._data = MagicMock()
		result = collection.add(None)
		self.assertFalse(result)
		collection._data.append.assert_not_called()

	def test_it_will_reject_non_Command(self):
		command = MagicMock()
		collection = CommandCollection()
		collection._data = MagicMock()
		result = collection.add(command)
		self.assertFalse(result)
		collection._data.append.assert_not_called()

	def test_it_adds_the_command_to_collection(self):
		command = Command({'hop': 'foo', 'to': 'bar'})
		collection = CommandCollection()
		collection._data = MagicMock()
		result = collection.add(command)
		self.assertTrue(result)
		collection._data.append.assert_called_with(command)

	def test_it_will_return_false_if_command_is_not_valid(self):
		command = MagicMock(spec=Command)
		command.isValid.return_value = False
		collection = CommandCollection()
		collection._data = MagicMock()
		result = collection.add(command)
		self.assertFalse(result)
		collection._data.append.assert_not_called()

	@patch('rabbit.commands.CommandCollection.getCommand')
	@patch('rabbit.commands.CommandCollection.remove')
	def test_it_will_update_existing_command(self, remove_mock, get_command):
		commandA = Command({'hop': 'test', 'to': 'foo'})
		commandB = Command({'hop': 'test', 'to': 'bar'})
		collection = CommandCollection()
		collection._data = MagicMock()
		get_command.return_value = commandA
		result = collection.add(commandB)
		self.assertTrue(result)
		get_command.assert_called_with('test')
		remove_mock.assert_called_with(commandA)
		collection._data.append.assert_called_with(commandB)

	"""
	remove - test it can remove from the collection
	"""
	def test_it_will_reject_None(self):
		collection = CommandCollection()
		collection._data = MagicMock()
		collection.remove('test')
		collection._data.remove.assert_called_with('test')

	"""
	getCommand - test it can get a command from the collection
	"""
	def test_it_will_return_None_if_not_found(self):
		collection = CommandCollection()
		collection._data = []
		result = collection.getCommand('test')
		self.assertEquals(result, None)

	def test_it_will_return_Command_on_hop_match(self):
		commandA = Mock(spec=Command)
		commandA.data = MagicMock()
		commandA.data.get = MagicMock(return_value='foobar')
		commandB = MagicMock(spec=Command)
		commandB.data = MagicMock()
		commandB.data.get = MagicMock(return_value='test')
		collection = CommandCollection()
		collection._data = [commandA, commandB]
		result = collection.getCommand('test')
		self.assertEquals(result, commandB)

	"""
	registerAll - test it can register every command in the collection
	"""
	def test_it_will_run_register_on_every_command(self):
		commandA = Mock(spec=Command)
		commandB = Mock(spec=Command)
		commandC = Mock(spec=Command)
		collection = CommandCollection()
		collection._data = [commandA, commandB, commandC]
		collection.registerAll()
		commandA.register.assert_called_with()
		commandB.register.assert_called_with()
		commandC.register.assert_called_with()

	"""
	is Iterable - test it can be iterated through
	"""
	def test_it_can_be_iterated_through(self):
		collection = CommandCollection()
		collection._data = [1, 2, 3]
		iterated = False
		for item in collection:
			iterated = True
		self.assertTrue(iterated)
