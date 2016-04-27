import unittest
from mock import *
from rabbit.command import Command

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

	@patch('rabbit.command.Command.generateDescription')
	def test_it_sets_missing_description_data_on_init(self, gen_desc):
		data = {'to': 'foo', 'hop': 'bar'}
		gen_desc.return_value = 'test'
		command = Command(data)
		gen_desc.assert_called_with()
		self.assertEquals(command.data['description'], 'test')

	@patch('rabbit.command.Command.generateDescription')
	def test_it_handles_empty_description_data_on_init(self, gen_desc):
		data = {'to': 'foo', 'hop': 'bar', 'description': None}
		gen_desc.return_value = 'test'
		command = Command(data)
		gen_desc.assert_called_with()
		self.assertEquals(command.data['description'], 'test')

	"""
	Sets name on init
	"""
	@patch('rabbit.command.Command.getName')
	def test_it_sets_name_on_init(self, get_name):
		data = {'to': 'foo', 'hop': 'bar'}
		get_name.return_value = 'test'
		command = Command(data)
		self.assertEquals(command.name, 'test')

	"""
	Sets groups on init
	"""
	@patch('rabbit.command.Command.getGroups')
	def test_it_sets_name_on_init(self, get_groups):
		data = {'to': 'foo', 'hop': 'bar'}
		get_groups.return_value = 'test'
		command = Command(data)
		self.assertEquals(command.groups, 'test')

	"""
	Sets clickObj on init
	"""
	@patch('rabbit.command.Command.setClickObject')
	def test_it_sets_name_on_init(self, set_clickObj):
		data = {'to': 'foo', 'hop': 'bar'}
		set_clickObj.return_value = 'test'
		command = Command(data)
		self.assertEquals(command.clickObject, 'test')

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

	"""
	getGroups
	- it returns empty an array when groups not set
	- it returns the correct group array
	"""
	def test_it_returns_empty_an_array_when_groups_not_set(self):
		data = {'to': 'foo', 'hop': None}
		command = Command(data)
		result = command.getGroups()
		self.assertEquals(result, [])

	def test_it_returns_the_correct_group_array(self):
		data = {'to': 'foo', 'hop': 'test hopping groups'}
		command = Command(data)
		result = command.getGroups()
		self.assertEquals(result, ['test', 'hopping'])

	"""
	getName
	- it returns None with no name set
	- it returns the correct name
	"""
	def test_it_returns_None_with_no_name_set(self):
		data = {'to': 'foo', 'hop': None}
		command = Command(data)
		result = command.getName()
		self.assertEquals(result, None)

	def test_it_returns_the_correct_name(self):
		data = {'to': 'foo', 'hop': 'test hopping groups'}
		command = Command(data)
		result = command.getName()
		self.assertEquals(result, 'groups')

	"""
	getClickObject
	- it returns the value of self.clickObject
	"""	
	def test_it_returns_the_value_of_self_clickObject(self):
		data = {'to': 'foo', 'hop': 'bar'}
		command = Command(data)
		command.clickObject = 'test'
		result = command.getClickObject()
		self.assertEquals(result, 'test')

	"""
	setClickObject
	- it correctly generates the clickObject
	"""	
	@patch('click.pass_context')
	@patch('click.command')
	def test_it_correctly_generates_the_clickObject(self, click_command, pass_context):
		command = Command({'to': 'foo', 'hop': 'bar'})
		test_func = MagicMock()
		test_func.return_value = 'test_command'
		pass_context.return_value = 'test_function'
		click_command.return_value = test_func
		result = command.setClickObject()
		self.assertEquals(result, 'test_command')
		pass_context.assert_called_with(command.run)
		test_func.assert_called_with('test_function')
		click_command.assert_called_with(
			name = command.getName(),
			help = command.data.get('description'),
			context_settings = {
				'allow_extra_args': True,
				'allow_interspersed_args': True,
			}
		)

	"""
	run
	- it correctly generates the clickObject
	"""	
	@patch('subprocess.call')
	def test_it_correctly_runs_command(self, call_mock):
		command = Command({'to': 'test', 'hop': 'go'})
		context = MagicMock()
		context.args = ['foo', 'bar']
		expected = 'test foo bar'
		try:
			result = command.run(context)
		except SystemExit as e:
			self.assertTrue(isinstance(e.code, MagicMock))
		call_mock.assert_called_with(expected, shell=True)

	"""
	run
	- it tests if the run command returns the correct exit codes
	"""
	def test_run_command_returns_correct_exit_codes(self):
		command = Command({'to': 'ls &> /dev/null', 'hop': 'go'})
		context = MagicMock()
		try:
			command.run(context)
		except SystemExit as e:
			self.assertEquals(e.code, 0)
		context.args = ['foo', 'bar']
		try:
			command.run(context)
		except SystemExit as e:
			self.assertNotEquals(e.code, 0)
