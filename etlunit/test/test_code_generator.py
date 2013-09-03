"""
    This is the test module for the code_generator module.
"""

__author__ = 'coty'

import unittest


class code_generator_tests(unittest.TestCase):

    def setUp(self):
        self.data = {'name': 'test'}

        from tempfile import mkdtemp
        self.out_dir = mkdtemp()

    def test_generateCode(self):
        print 'test'  # dummy test for now...
