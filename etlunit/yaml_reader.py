"""
    This file houses all of the code to read in the YAML files.
"""

__author__ = 'coty'

import glob
import logging

import yaml

from etlunit.utils.settings import etlunit_config, console


class YAMLReader():
    """
        Class to read YAML files.
    """

    def __init__(self, in_file, in_dir):
        """
            This method takes in a couple options (in_file and in_dir) and determines what files we are reading in.

            :param in_file: Input file that we want to read.
            :type in_file: str.
            :param in_dir: Input directory that we want to read files from.
            :type in_dir: str.
        """
        self.log = logging.getLogger(name='YAMLReader')
        self.log.setLevel(etlunit_config['logging_level'])
        self.log.addHandler(console)

        self.in_file = in_file
        self.in_dir = in_dir
        self.tests = {}

    def readTests(self):
        """
            This method determines if were reading a file or a directory, then calls the readFile method.
        """
        if self.in_file is not None:
            # this block reads and parses yaml from an individual file
            self.readFile(self.in_file)
        elif self.in_dir is not None:
            # this block reads and parses yaml from multiple files
            for test_path in glob.glob('{}/*.yml'.format(self.in_dir)):
                self.readFile(test_path)

        self.log.trace(self.tests)
        return self.tests

    def readFile(self, filename):
        """
            This method actually reads the files contents and adds them an array for later consumption.

            :param filename: The file name that we are reading.
            :type filename: str.
        """
        with open(filename, 'r') as f:
                prop_list = yaml.load(f.read())
                self.log.debug("Reading file %s." % filename)
                self.log.debug("File contents: %s." % prop_list)
                self.tests[filename] = prop_list

                from os import path
                self.tests[filename]['res_dir'] = self.in_dir or path.dirname(self.in_file)