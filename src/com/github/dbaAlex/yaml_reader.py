__author__ = 'coty'

import glob
import yaml
import logging
from settings import etlunit_config, console


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
        self.tests = []

    # TODO: Work on nested yaml. It crashes the scanner when you have a few levels deep.
    # How deep is too deep?  There should be some way of handling the nested yaml. - Alex
    def readTests(self):
        # this block reads and parses yaml from an individual file
        if self.in_file is not None:
            # test = {}
            with open(self.in_file, 'r') as f:
                prop_list = yaml.load(f.read())
                self.log.debug(prop_list)
                return prop_list

                # TODO: Need to verify that this is what we want. Will this always return a JSON array?
                # for key, value in prop_list.items():
                #     test[key] = value

            # self.log.debug(test)
            # self.tests.append(test)
        # this block reads and parses yaml from multiple files
        elif self.in_dir is not None:
            for test_path in glob.glob('{}/*.yml'.format(self.in_dir)):
                # test = {}
                with open(test_path, 'r') as f:
                    prop_list = yaml.load(f.read())
                    self.log.debug(prop_list)
                    self.tests[test_path] = prop_list

                    # for key, value in prop_list.items():
                    #     test[key] = value
                # self.log.debug(test)
                # self.tests.append(test)

            return self.tests
