# import unittest
# import mock
# import yaml
# from rabbit.rabbit import Rabbit

# class TestRabbit(unittest.TestCase):

#   def test_it_can_read_yaml_file(self):
#     testYaml = 'rabbit.yaml'
#     expected = yaml.load(open(testYaml, 'r'))
#     result = Rabbit().read(testYaml)
#     self.assertEqual(result, expected)

#   @mock.patch('rabbit.rabbit.subprocess')
#   def test_it_can_run_a_command(self, subprocess_mock):
#     callArgs = "echo hello world"
#     result = Rabbit().run(callArgs)
#     subprocess_mock.call.assert_called_with(callArgs, shell=True)

#   def test_it_can_convert_a_command_string_to_array(self):
#     command = 'test command example'
#     expected = ['test', 'command', 'example']
#     result = Rabbit().converStringToArgs(command)
#     self.assertEqual(result, expected)

#   def test_it_can_convert_a_command_string_to_array_with_quotes_single(self):
#     command = "echo 'hello world'"
#     expected = ['echo', "'hello world'"]
#     result = Rabbit().converStringToArgs(command)
#     self.assertEqual(result, expected)

#   def test_it_can_convert_a_command_string_to_array_with_quotes_double(self):
#     command = 'echo "hello world"'
#     expected = ['echo', '"hello world"']
#     result = Rabbit().converStringToArgs(command)
#     self.assertEqual(result, expected)

#   def test_it_can_find_command_in_config(self):
#     command = ['hello', 'world']
#     expected = {
#       'hop': 'hello world',
#       'to': 'echo "hello world"' 
#     }
#     config = { 'commands': [ expected ] }
#     result = Rabbit().findCommandInConfig(command, config)
#     self.assertEqual(result, expected)

#     def test_it_can_find_command_in_config_no_match(self):
#       command = ['hello']
#       expected = {
#         'hop': 'hello world',
#         'to': 'echo "hello world"' 
#       }
#       config = { 'commands': [ expected ] }
#       result = Rabbit().findCommandInConfig(command, config)
#       self.assertEqual(result, False)

