#!/usr/bin/python
#
# This file was created by etlUnit.
# Create date: %s strftime("%a, %d %b %Y %X +0000", gmtime()
#

import unittest

from testfixture import *


class MyTestSuite(MyTestFixture):

    def test(self):
        assert 1 == 2

if __name__ == "__main__":
    unittest.main(verbosity=2)