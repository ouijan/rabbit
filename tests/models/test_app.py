import unittest
import mock
from rabbit.models.app import *
from rabbit.models.config import *

class TestApp(unittest.TestCase):

	def test_it_creates_a_new_object(self):
		app = App()
		self.assertNotEqual(app, None)

	def test_it_sets_config_property(self):
		app = App()
		self.assertTrue(isinstance(app.config, (Config)))

	@mock.patch('rabbit.models.app.App.bootstrap')
	def test_it_runs_bootstrap_on_init(self, bootstrap):
		app = App()
		bootstrap.assert_called_with()

	"""
	Bootstrap Tests
	"""
	@mock.patch('rabbit.models.app.App.loadHomeConfig')
	def test_it_runs_bootstrap_on_init(self, loadHomeConfig):
		app = App()
		app.bootstrap()
		loadHomeConfig.assert_called_with()

	# @mock.patch('rabbit.models.app.App.loadHomeConfig')
	# def test_it_runs_bootstrap_on_init(self, loadHomeConfig):
	# 	app = App.bootstrap()
	# 	loadHomeConfig.assert_called_with()



