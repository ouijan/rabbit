import unittest
import mock
from rabbit.models.config import *

class TestConfig(unittest.TestCase):

	def test_it_creates_a_new_object(self):
		config = Config()
		self.assertTrue(isinstance(config, (Config)))

	def test_it_sets_config_property(self):
		config = Config()
		self.assertEquals(config.data, {})