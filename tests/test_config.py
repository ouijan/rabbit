import unittest
from mock import *
import yaml
from rabbit.config import Config


class TestConfig(unittest.TestCase):

	def test_it_creates_a_new_object(self):
		config = Config()
		self.assertTrue(isinstance(config, (Config)))

	def test_it_sets_config_property(self):
		config = Config()
		self.assertEquals(config.data, {})


	"""
	Test Config.get
	- it will return the value of a data key
	- it will return the default if key doesnt exist
	- it will return None if the value is None
	"""
	def test_it_will_return_the_value_of_a_data_key(self):
		config = Config()
		config.data = {'test': 'value'}
		result = config.get('test', 'default')
		self.assertEquals(result, 'value')

	def test_it_will_return_the_default_if_key_doesnt_exist(self):
		config = Config()
		config.data = {}
		result = config.get('test', 'default')
		self.assertEquals(result, 'default')

	def test_it_will_return_None_if_the_value_is_None(self):
		config = Config()
		config.data = { 'test': None }
		result = config.get('test', 'default')
		self.assertEquals(result, None)

	"""
	Test Config.load
	- returns False if self._read returns None
	- returns True on success
	- correctly sets config.data
	"""
	@patch('rabbit.config.Config._read')
	def test_returns_False_if_self_read_returns_None(self, read_mock):
		read_mock.return_value = None
		result = Config().load('test')
		read_mock.assert_called_with('test')
		self.assertFalse(result)

	@patch('rabbit.config.Config._read')
	def test_returns_true_on_success(self, read_mock):
		read_mock.return_value = {'foo': 'bar'}
		result = Config().load('test')
		self.assertTrue(result)

	@patch('rabbit.config.Config._read')
	@patch('rabbit.config.Config._merge')
	def test_correctly_sets_config_data(self, merge_mock, read_mock):
		fileData = {'foo': 'bar'}
		read_mock.return_value = fileData
		merge_mock.return_value = fileData
		config = Config()
		result = config.load('test')
		merge_mock.assert_called_with({}, fileData)
		self.assertEquals(config.data, fileData)

	"""
	Test Config._read
	- returns None on IOError
	- returns None on YAMLError
	- returns a value of yaml.safe_load on success
	"""
	@patch('io.open')
	def test_it_returns_None_on_IOError_exception(self, io_open):
		io_open.side_effect = IOError('File Not Found')
		result = Config()._read('test')
		self.assertEquals(result, None)

	@patch('io.open')
	@patch('yaml.safe_load')
	def test_it_returns_None_on_YAMLError_exception(self, safe_load, io_open):
		io_open.return_value = "{'foo': 'bar'}"
		safe_load.side_effect = yaml.YAMLError()
		result = Config()._read('test')
		self.assertEquals(result, None)

	@patch('io.open')
	@patch('yaml.safe_load')
	def test_it_returns_None_on_YAMLError_exception(self, safe_load, io_open):
		io_open.return_value = "{'foo': 'bar'}"
		safe_load.return_value = {'foo': 'bar'}
		result = Config()._read('test')
		self.assertEquals(result, {'foo': 'bar'})


	"""
	Test Config._merge
	- it doesnt update a value with None
	- it works recursively
	- it updates to new value
	- it merges old and new
	- it works for nested dicts
	- it works for lists append
	- it works for lists in dicts
	- it doesn't modify the original object
	- it sets None if not previously set on dicts
	- it merges lists by concatinating them
	"""
	def test_it_doesnt_update_a_value_with_none(self):
		old = {'foo': 'bar'}
		new = {'foo': None }
		result = Config()._merge(old, new)
		self.assertEquals(result, old)

	def test_it_works_recursively(self):
		old = {'test': {'foo': 'bar'}}
		new = {'test': {'foo': None }}
		result = Config()._merge(old, new)
		self.assertEquals(result, old)

	def test_it_updates_to_new_value(self):
		old = {'foo': 'bar'}
		new = {'foo': 'zap' }
		result = Config()._merge(old, new)
		self.assertEquals(result, new)

	def test_it_merges_old_and_new(self):
		old = {'foo': 'bar', 'test': None}
		new = {'test': 'zap' }
		expected = {'foo': 'bar', 'test': 'zap'}
		result = Config()._merge(old, new)
		self.assertEquals(result, expected)

	def test_it_works_for_nested_dicts(self):
		old = {'foo': {'bar': True}, 'test': None}
		new = {'foo': {'bar': None}, 'test': {'zap': True}}
		expected = {'foo': {'bar': True}, 'test': {'zap': True}}
		result = Config()._merge(old, new)
		self.assertEquals(result, expected)

	def test_it_works_for_lists_append(self):
		old = ['test']
		new = ['test', 'foo']
		expected = ['test', 'test', 'foo']
		result = Config()._merge(old, new)
		self.assertEquals(result, expected)

	def test_it_works_for_nested_lists(self):
		old = [['test'], [['foo']]]
		new = [['test'], ['test', 'thing']]
		expected = [['test'], [['foo']], ['test'], ['test', 'thing']]
		result = Config()._merge(old, new)
		self.assertEquals(result, expected)

	def test_it_works_for_lists_in_dicts(self):
		old = {'test': ['bar']}
		new = {'test': ['bar', 'foo']}
		expected = {'test': ['bar', 'bar', 'foo']}
		result = Config()._merge(old, new)
		self.assertEquals(result, expected)

	def test_it_works_for_dicts_in_lists(self):
		old = [{'test': 'thing'}, 'mix']
		new = [{'test': 'bar'}]
		expected = [{'test': 'thing'}, 'mix', {'test': 'bar'}]
		result = Config()._merge(old, new)
		self.assertEquals(result, expected)

	def test_it_sets_None_if_not_previously_set_on_dicts(self):
		old = {'foo': 'bar'}
		new = {'test': None}
		expected = {'test': None, 'foo': 'bar'}
		result = Config()._merge(old, new)
		self.assertEquals(result, expected)
	
	def test_it_doesnt_modify_the_original_object(self):
		old = {'foo': None}
		new = {'foo': 'bar'}
		expected = {'foo': 'bar'}
		result = Config()._merge(old, new)
		self.assertEquals(result, expected)
		self.assertEquals(old, {'foo': None})

	def test_it_should_merge_lists_concat(self):
		old = ['foo']
		new = ['bar']
		expected = ['foo', 'bar']
		result = Config()._merge(old, new)
		self.assertEquals(result, expected)

