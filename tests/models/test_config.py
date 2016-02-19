import unittest
import mock
import yaml
from rabbit.models.config import *


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
	@mock.patch('rabbit.models.config.Config._read')
	def test_returns_False_if_self_read_returns_None(self, read_mock):
		config = Config()
		read_mock.return_value = None
		result = config.load('test')
		read_mock.assert_called_with('test')
		self.assertFalse(result)

	@mock.patch('rabbit.models.config.Config._read')
	def test_returns_true_on_success(self, read_mock):
		config = Config()
		read_mock.return_value = {'foo': 'bar'}
		result = config.load('test')
		self.assertTrue(result)

	@mock.patch('rabbit.models.config.Config._read')
	@mock.patch('rabbit.models.config.Config._update')
	def test_correctly_sets_config_data(self, update_mock, read_mock):
		fileData = {'foo': 'bar'}
		config = Config()
		read_mock.return_value = fileData
		update_mock.return_value = fileData
		result = config.load('test')
		update_mock.assert_called_with({}, fileData)
		self.assertEquals(config.data, fileData)

	"""
	Test Config._read
	- returns None on IOError
	- returns None on YAMLError
	- returns a value of yaml.safe_load on success
	"""
	@mock.patch('io.open')
	# @mock.patch('yaml.safe_load')
	def test_it_returns_None_on_IOError_exception(self, io_open):
		io_open.side_effect = IOError('File Not Found')
		config = Config()
		result = config._read('test')
		self.assertEquals(result, None)

	@mock.patch('io.open')
	@mock.patch('yaml.safe_load')
	def test_it_returns_None_on_YAMLError_exception(self, safe_load, io_open):
		io_open.return_value = "{'foo': 'bar'}"
		safe_load.side_effect = yaml.YAMLError()
		config = Config()
		result = config._read('test')
		self.assertEquals(result, None)

	@mock.patch('io.open')
	@mock.patch('yaml.safe_load')
	def test_it_returns_None_on_YAMLError_exception(self, safe_load, io_open):
		io_open.return_value = "{'foo': 'bar'}"
		safe_load.return_value = {'foo': 'bar'}
		config = Config()
		result = config._read('test')
		self.assertEquals(result, {'foo': 'bar'})

