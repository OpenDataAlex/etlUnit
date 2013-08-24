import unittest


class TestCase(unittest.TestCase):

    def test_dummy(self):
        expectedResult = "test"
        result = "test"

        self.assertEqual(expectedResult, result)

if __name__ == "__main__":
    unittest.main(verbosity=2)
