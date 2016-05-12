import unittest
from mock import *
from rabbit import settings
from rabbit.app import App
from rabbit.config import Config
from rabbit.command import Command
from rabbit.group import Group


class TestApp(unittest.TestCase):

	def test_it_creates_CONFIG_FILE_global(self):
		self.assertNotEqual(settings.CONFIG_FILE, None)

	def test_it_sets_CONFIG_FILE_to_rabbit_yaml(self):
		self.assertEquals(settings.CONFIG_FILE, 'rabbit.yaml')

	def test_it_creates_a_new_object(self):
		app = App()
		self.assertTrue(isinstance(app, (App)))

	def test_it_sets_config_property(self):
		app = App()
		self.assertTrue(isinstance(app.config, (Config)))

	def test_it_sets_baseGroup_property(self):
		app = App()
		self.assertTrue(isinstance(app.baseGroup, (Group)))

	@patch('rabbit.app.App.bootstrap')
	def test_it_runs_bootstrap_on_init(self, bootstrap):
		app = App()
		bootstrap.assert_called_with()

	"""
	Bootstrap Tests
	- Runs the loadHomeConfig Method
	- Runs the loadHomeConfig Method
	"""
	@patch('rabbit.app.App.loadHomeConfig')
	def test_bootstrap_runs_the_loadHomeComfig(self, loadHomeConfig):
		app = App()
		app.bootstrap()
		loadHomeConfig.assert_called_with()

	@patch('rabbit.app.App.loadLocalConfig')
	def test_bootstrap_runs_the_loadLocalComfig(self, loadLocalConfig):
		app = App()
		app.bootstrap()
		loadLocalConfig.assert_called_with()

	@patch('rabbit.app.App.loadCommands')
	def test_bootstrap_runs_the_loadLocalComfig(self, loadCommands):
		app = App()
		app.bootstrap()
		loadCommands.assert_called_with()

	"""
	loadHomeConfig Tests
	- it runs the app.config.load on the correct path
	"""
	@patch('rabbit.config.Config.load')
	@patch('os.path.expanduser')
	def test_bootstrap_runs_the_loadLocalConfig(self, expanduser_mock, config_load):
		app = App()
		expanduser_mock.return_value = 'test'
		homepath = "test/" + settings.CONFIG_FILE
		app.loadHomeConfig()
		config_load.assert_called_with(homepath)

	"""
	loadLocalConfig Tests
	- it runs the app.config.load on the correct path
	"""
	@patch('rabbit.config.Config.load')
	def test_bootstrap_runs_the_loadLocalConfig(self, config_load):
		app = App()
		localpath = "./" + settings.CONFIG_FILE
		app.loadLocalConfig()
		config_load.assert_called_with(localpath)

	"""
	loadCommands Tests
	- It doesnt call addCommand when no commands are present
	- It creates a new command with given data
	- It calls addCommand for each command
	"""
	@patch('rabbit.config.Config.get')
	def test_it_doesnt_call_addCommand_when_no_commands_are_present(self, config_get):
		app = App()
		config_get.return_value = None
		result = app.loadCommands()
		self.assertFalse(result)

	@patch('rabbit.config.Config.get')
	@patch('rabbit.app.App.createCommand')
	def test_it_creates_a_new_command_with_given_data(self, create_command, config_get):
		app = App()
		config_get.return_value = [1]
		result = app.loadCommands()
		create_command.assert_called_with(1)
		self.assertTrue(result)

	@patch('rabbit.config.Config.get')
	@patch('rabbit.app.App.createCommand')
	@patch('rabbit.app.App.addCommand')
	def test_it_calls_addCommand_for_each_command(self, add_command, create_command, config_get):
		app = App()
		config_get.return_value = [1]
		create_command.return_value = 'test';
		result = app.loadCommands()
		add_command.assert_called_with('test')
		self.assertTrue(result)

	"""
	addCommand Tests
	- It validates command object falsy
	- It finds the correct child group
	- It adds the command to the given child group
	"""
	def test_it_validates_command_object_falsy(self):
		app = App()
		command = object
		result = app.addCommand(command)
		self.assertFalse(result)

	def test_it_finds_the_correct_child_group(self):
		app = App()
		command = Command()
		result = app.addCommand(command)
		self.assertTrue(result)
