import unittest
from mock import *
from rabbit.group import Group


class TestGroup(unittest.TestCase):

	def test_it_creates_a_new_object(self):
		group = Group()
		self.assertTrue(isinstance(group, (Group)))
