"""
    This is a test module for the connection_reader module.
"""

__author__ = 'coty'

import unittest


class ConnectionTests(unittest.TestCase):
    """
        Test class for the connection_reader module.
    """

    def test_import_connections(self):
        """
            This method checks to see if the import of the connections object works.

            It makes an implied assertion that if it doesn't get an exception, it passes.
        """
        try:
            from etlunit.template_base.connections_reader import connections
        except:
            self.fail("The connections object could not be imported.")

    def test_connection_exists(self):
        """
            This method tests to see if the default connection exists in the connections file.
        """
        try:
            from etlunit.template_base.connections_reader import connections
            test_conn = connections['test conn']
        except:
            self.fail("The test connection does not exist.")

        self.assertTrue(test_conn['dbname'] == "testing")