#!/usr/bin/python
#
# This file was created by etlUnit.
# Create date: create_date
#

import unittest
import xmlrunner
from sqlalchemy_connector import DB_Connector
from testfixture import *


class MyTestSuite(MyTestFixture):

    connections = {
        'test conn': {
            'dbname': 'testing',
            'dbtype': 'mysql',
            'user': 'py',
            'pass': 'py_pass',
            'host': 'localhost',
            'port': '3006'
        }
    }

    def test_testcase1(self):
        connector = DB_Connector(self.connections['test conn'])

        test = {
            'test conn': {
                'table': 'test',
                'columns': [
                    'test',
                ],
                'count': 'test'
            },
            'results': {
                'result': 2
            }

        }

        table = connector.getTable(test['test conn']['table'])
        # using func.count you can count individual columns
        # from sqlalchemy import func
        # result = connector.session.query(func.count(table._columns.test)).all()
        result = connector.session.query(table).count()

        self.assertEqual(test['results']['result'], result)

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=xmlrunner.XMLTestRunner(output='.'))