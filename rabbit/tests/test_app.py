import unittest
from mock import *
from rabbit.app import *
from rabbit.config import Config
from rabbit.command import Command

class TestApp(unittest.TestCase):

	def test_it_creates_CONFIG_FILE_global(self):
		self.assertNotEqual(CONFIG_FILE, None)

	def test_it_sets_CONFIG_FILE_to_rabbit_yaml(self):
		self.assertEquals(CONFIG_FILE, 'rabbit.yaml')

	def test_it_creates_a_new_object(self):
		app = App()
		self.assertTrue(isinstance(app, (App)))

	def test_it_sets_config_property(self):
		app = App()
		self.assertTrue(isinstance(app.config, (Config)))

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
	def test_bootstrap_runs_the_loadLocalComfig(self, expanduser_mock, config_load):
		app = App()
		expanduser_mock.return_value = 'test'
		homepath = "test/" + CONFIG_FILE
		app.loadHomeConfig()
		config_load.assert_called_with(homepath)

	"""
	loadLocalConfig Tests
	- it runs the app.config.load on the correct path
	"""
	@patch('rabbit.config.Config.load')
	def test_bootstrap_runs_the_loadLocalComfig(self, config_load):
		app = App()
		localpath = "./" + CONFIG_FILE
		app.loadLocalConfig()
		config_load.assert_called_with(localpath)

	"""
	loadCommands Tests
	- it adds commands from settings to collection
	"""
	@patch('rabbit.config.Config.get')
	def test_it_adds_nothing_if_commands_is_None(self, config_get):
		app = App()
		config_get.return_value = None
		app.loadCommands()
		config_get.assert_called_with('commands')
		

	@patch('rabbit.config.Config.get')
	def test_it_adds_commands_from_settings_to_collection (self, config_get):
		app = App()
		app.loadCommands()
		
		
		

	


