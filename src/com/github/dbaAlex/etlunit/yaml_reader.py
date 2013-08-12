__author__ = 'coty'

import glob
import logging

import yaml

from src.com.github.dbaAlex.utils.settings import etlunit_config, console


class YAMLReader():
    """
        Class to read yaml files and produce code based on templates that we provide.
    """

    def __init__(self, in_file, in_dir, out_dir):
        self.log = logging.getLogger(name='YAMLReader')
        self.log.setLevel(etlunit_config['logging_level'])
        self.log.addHandler(console)

        self.in_file = in_file
        self.in_dir = in_dir
        self.out_dir = out_dir
        self.tests = {}

    def readTests(self):
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
        with open(filename, 'r') as f:
                prop_list = yaml.load(f.read())
                self.log.debug("Reading file %s." % filename)
                self.log.debug("File contents: %s." % prop_list)
                self.tests[filename] = prop_list