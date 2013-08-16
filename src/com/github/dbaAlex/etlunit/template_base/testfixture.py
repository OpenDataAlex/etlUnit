#!/usr/bin/python
#
# This file was created by etlUnit.
# Create date: create_date
#

import unittest
from sqlalchemy_connector import DB_Connector


class MyTestFixture(unittest.TestCase):

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

    connector = DB_Connector(connections['test conn'])

    def setUp(self):
        print 'Setting up fixture'
        setup = {
            'test conn': {
                'table': 'test',
                'records': [
                    {'test': 0},
                    {'test': 1},
                ]
            }
        }

        conn = self.connector.engine.connect()
        table = self.connector.getTable(setup['test conn']['table'])

        for item in setup['test conn']['records']:
            ins = table.insert().values(test=item['test'])
            conn.execute(ins)

    def tearDown(self):
        print "Tearing down fixture"
        teardown = {
            'test conn': {
                'table': 'test',
                'where': [
                    {'test': 0},
                    {'test': 1},
                ]
            }
        }

        conn = self.connector.engine.connect()
        table = self.connector.getTable(teardown['test conn']['table'])

        for item in teardown['test conn']['where']:
            delete = table.delete(table._columns.test!=item['test'])
            conn.execute(delete)
