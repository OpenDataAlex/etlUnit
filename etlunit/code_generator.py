"""
    This file houses all of the code necessary to generate code from templates.
"""

__author__ = 'coty'

import logging
from etlunit.utils.settings import etlunit_config, console


class CodeGenerator:
    """
        This class performs the generation of the code. Using the Jinja2 template engine, we are taking in YAML
        and generating code from it by filling in templates.
    """

    # TODO: Determine if the array passed into the class is a single YAML array or if it is multile arrays from files
    def __init__(self, out_dir, data, is_test):
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
        self.is_test = is_test

    def generateCode(self):
        """
            This method actually generates the code.
        """
        # TODO: Implement a YAML validation class.

        self.setup_jinja_env()

        for test_suite_key in self.resource_data.keys():
            self.log.info("Generating code from %s..." % test_suite_key)
            test_suite = self.resource_data[test_suite_key]

            # TODO: Determine how we handle dependencies on single files.
            try:
                if test_suite['fixture'] is not None:
                    fixture_data = self.get_fixture_data(test_suite)
                    variables = {
                        'header': self.header,
                        'name': test_suite['fixture'].replace(' ', ''),
                        'fixture': test_suite['fixture'],
                        'setup': fixture_data['setup'],
                        'teardown': fixture_data['teardown'],
                    }
                    self.generate_from_template("testfixture.jj2", variables)
            except KeyError:
                test_suite['fixture'] = "unittest.TestCase"  # Default value for fixture
                self.log.info("Fixture not present, generating TestSuite...")
            finally:
                variables = {
                    'header': self.header,
                    'name': test_suite['name'].replace(' ', ''),
                    'fixture': test_suite['fixture'],
                    'tests': test_suite['tests'],
                }
                # TODO: Add logic for setup/teardown if fixture is unittest.TestCase ?
                self.generate_from_template("testsuite.jj2", variables)

        self.log.info("Code generation complete.")

    def get_fixture_data(self, test_suite):
        # get fixture data
        from etlunit.yaml_reader import YAMLReader
        fixture_res = "%s/%s.yml" % (test_suite['res_dir'], test_suite['fixture'])
        reader = YAMLReader(fixture_res, None)
        return reader.readTests()[fixture_res]

    def generate_from_template(self, template_name, variables):
        # create template object and get stream
        template = self.j2_env.get_template(template_name)

        if self.is_test:
            self.log.testing("\n{}".format(template.render(variables)))
        else:
            template_stream = template.stream(variables)

            # Dump stream to file. Double slashes annoy me :)
            if self.out_dir.endswith("/"):
                template_stream.dump("%s%s.py" % (self.out_dir, variables['name']))
            else:
                template_stream.dump("%s/%s.py" % (self.out_dir, variables['name']))

    def setup_jinja_env(self):
        from jinja2 import Environment, PackageLoader
        from time import strftime, gmtime
        self.j2_env = Environment(loader=PackageLoader('etlunit', 'templates'), trim_blocks=True, lstrip_blocks=True)

        # Header lines created here and added to the templates as required
        self.header = "#!/usr/bin/python\n" \
                 "#\n" \
                 "# This file was created by etlUnit.\n#" \
                 " Create date: %s\n" \
                 "#\n" % \
                 strftime("%a, %d %b %Y %X +0000", gmtime())