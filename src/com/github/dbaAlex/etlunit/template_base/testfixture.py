#!/usr/bin/python
#
# This file was created by etlUnit.
# Create date: create_date
#

import unittest
from sqlalchemy_connector import DB_Connector


class MyTestFixture(unittest.TestCase):

    connector = DB_Connector('test conn')

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
        records = setup['test conn']['records']

        ins = table.insert().values(records)
        conn.execute(ins)

    def tearDown(self):
        print "Tearing down fixture"
        teardown = {
            'test conn': {
                'table': 'test',
            }
        }

        conn = self.connector.engine.connect()
        table = self.connector.getTable(teardown['test conn']['table'])
        delete = table.delete()
        conn.execute(delete)
