"""
    This module tests the sqlalchemy_connector module.
"""

__author__ = 'coty'

import unittest
from etlunit.template_base.sqlalchemy_connector import DB_Connector


class SQLAlchemy_Tests(unittest.TestCase):
    """
        This class will test the sqlalchemy_connector module.
    """

    def test_init(self):
        """
            Testing the init method in the DB_Connector class.
        """
        try:
            connector = DB_Connector("test conn")
        except:
            self.fail("Connector failed to initialize.")

        self.assertTrue(connector.engine != None, "Engine is None.")
        self.assertTrue(connector.meta != None, "Meta is None.")
        self.assertTrue(connector.insp != None, "Insp is None.")
        self.assertTrue(connector.session != None, "Session is None.")
        self.assertTrue(connector.conn != None, "Conn is None.")
