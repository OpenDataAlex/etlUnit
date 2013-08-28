"""
    This file houses all of the code necessary to generate code from templates.
"""

__author__ = 'coty'

import logging
import os

from etlunit.utils.settings import etlunit_config, console


class CodeGenerator:
    """
        This class performs the generation of the code. Using the Jinja2 template engine, we are taking in YAML
        and generating code from it by filling in templates.
    """

    # TODO: Determine if the array passed into the class is a single YAML array or if it is multile arrays from files
    def __init__(self, out_dir, data):
        """
            This method initializes the logging variables as well as the resource_data and out_dir variables.
            :param out_dir: The output directory that we will generate code in.
            :type out_dir: str.
            :param data: An array of data that comes from the YAML resource file.
            :type data: arr.
        """
        self.log = logging.getLogger(name='CodeGenerator')
        self.log.setLevel(etlunit_config['logging_level'])
        self.log.addHandler(console)

        self.resource_data = data
        self.out_dir = out_dir

    def generateCode(self, test):
        """
            This method actually generates the code.
            :param test: A boolean that determines if we are running a test or not. If its true, then we don't persist
            the code that we generate, it prints to stdout instead.
            :type test: bool.
        """
        # TODO: Implement a YAML validation class.

        from jinja2 import Environment, PackageLoader
        from time import strftime, gmtime
        j2_env = Environment(loader=PackageLoader('etlunit', 'templates'), trim_blocks=True, lstrip_blocks=True)

        # Header lines created here and added to the templates as required
        header = "#!/usr/bin/python\n" \
                 "#\n" \
                 "# This file was created by etlUnit.\n#" \
                 " Create date: %s\n" \
                 "#\n" % \
                 strftime("%a, %d %b %Y %X +0000", gmtime())

        for test_suite_name in self.resource_data.keys():
            self.log.info("Generating code from %s..." % test_suite_name)
            self.test_suite = self.resource_data[test_suite_name]

            # TODO: Determine how we handle dependencies on single files.
            # TODO: Added fixture definition to the mix. Currently it generates a fixture but it has no variables.
            try:
                if self.test_suite['fixture'] is not None:
                    from etlunit.yaml_reader import YAMLReader
                    self.fixture = self.test_suite['fixture']
                    fixture_res = "../res/%s.test_suite_name" % self.fixture
                    reader = YAMLReader(fixture_res, None)
                    fixture_data = reader.readTests()[fixture_res]

                    self.template_output = j2_env.get_template("testfixture.jj2")\
                        .render(header=header,
                                fixture=self.fixture,
                                setup=fixture_data['setup'],
                                teardown=fixture_data['teardown'])

                    self.persist_output(self.test_suite['fixture'], self.template_output, test)
            except KeyError:
                self.fixture = "unittest.TestCase"  # Default value for fixture
                self.log.info("Fixture not present, generating TestSuite...")
            finally:
                self.template_output = j2_env.get_template("testsuite.jj2") \
                    .render(header=header,
                            fixture=self.fixture,
                            tests=self.test_suite['tests'],
                            suitename=self.test_suite['name'].replace(' ', ''))

                self.persist_output(self.test_suite['name'], self.template_output, test)
        self.log.info("Code generation complete.")

    def persist_output(self, name, output, test):
        """
            This method persist the generated code to the output directory specified.
            :param name: The name of the test suite.
            :type name: str.
            :param output: The output from the template being rendered.
            :type output: str.
            :param test: A boolean that determines if we are testing or not. If we are testing, then output is not
            persisted.
            :type test: bool.
        """
        if test:
            self.log.testing('\n' + self.template_output + '\n')
        else:
            # check for ending / in file path
            if self.out_dir.endswith("/"):
                file_path = "%s%s.py" % (self.out_dir, name.replace(' ', ''))
            else:
                file_path = "%s/%s.py" % (self.out_dir, name.replace(' ', ''))

            self.log.debug("Writing %s" % file_path)
            with open(file_path, 'w') as f:
                os.chmod(f.name, 0770)

                f.write(output)
                f.close()
