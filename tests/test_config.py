import unittest
import mock
from rabbit.config import Config

class TestConfig(unittest.TestCase):


	# def test_it_can_load_config_dict(self):
	# 	config = Config()
	# 	config.load({
	# 		"commands": [
	# 			{ "map": "hello", "to": "echo hello world" },
	# 		],
	# 	})

	# May require mocking the OS
	def test_it_can_find_a_config_file(self):
		config = Config()
		result = config.find()
		self.assertEqual("./rabbit.yaml", result)



