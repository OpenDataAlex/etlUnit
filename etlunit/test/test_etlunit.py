"""
    This file houses the tests for the etlUnit file.
"""

import unittest


class etlUnit_TestCase(unittest.TestCase):
    """
        Test case for the etlUnit class.
    """

    def test_dummy(self):
        """
            Dummy test for now that just checks a static string :)
        """
        expectedResult = "test"
        result = "test"

        self.assertEqual(expectedResult, result)

if __name__ == "__main__":
    unittest.main(verbosity=2)
