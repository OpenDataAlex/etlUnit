'''
  This class holds all of the code required to build database objects for test queries to be executed.
'''


__author__ = 'ameadows'

import logging
from yaml_reader import YAMLReader
from subprocess import call

from etlunit.utils.settings import etlunit_config, console

class ObjectGenerator:
    '''
      This class will read from a database connection settings file and reverse engineer the database into a
      sqlalchemy object set that can be then used for the unit tests.
    '''

    def __init__(self, out_dir, settings_dir, conn_name):
        """
            This method initializes the logging variables as well as the settings_dir and out_dir variables.
            :param out_dir: The output directory that we will generate code in.
            :param conn_name:  The name of the database connection that will be reverse engineered.
            :type out_dir: str
            :type settings_dir: str
            :type conn_name: str
        """
        self.log = logging.getLogger(name='ObjectGenerator')
        self.log.setLevel(etlunit_config['logging_level'])
        self.log.addHandler(console)

        self.settings_dir = settings_dir
        self.out_dir = out_dir
        self.conn_name = conn_name
        self.connection_file = './res/connections.yml'
        self.outfile = self.settings_dir + "/" + self.conn_name + ".sqlalchemy"

        self.connections = YAMLReader(self.connection_file).readFile()
        self.connection = self.connections[self.connection_file][self.conn_name]

        self.engine = self.connection['dbtype'] + "://" + self.connection['user'] + ":" + self.connection[
            'password'] + "@" + self.connection['host'] + ":" + self.connection['port'] +"/" + self.connection['dbname']


    def generateObject(self):
        '''
            This method generates the object set based on the given connection and object.
        '''

        call("sqlacodegen", "--outfile " + self.outfile + " " + self.engine)