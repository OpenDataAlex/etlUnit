#!/usr/bin/python
#
# This file was created by etlUnit.
# Create date: %s strftime("%a, %d %b %Y %X +0000", gmtime()
#

import unittest


class MyTestFixture(unittest.TestCase):

    def setUp(self):
        print "Fixture setup"

    def tearDown(self):
        print "Fixture teardown"