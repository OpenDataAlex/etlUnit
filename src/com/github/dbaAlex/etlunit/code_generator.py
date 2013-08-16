__author__ = 'coty'

import logging
import os

from src.com.github.dbaAlex.utils.settings import etlunit_config, console


class CodeGenerator():
    """
        This class performs the generation of the code. Using the jinja2 template engine, we are taking in yaml
        and generating code from it by filling in templates.
    """

    # TODO: Determine if the array passed into the class is a single yaml array or if it is multile arrays from files
    def __init__(self, out_dir, data):
        self.log = logging.getLogger(name='CodeGenerator')
        self.log.setLevel(etlunit_config['logging_level'])
        self.log.addHandler(console)

        self.yaml_data = data
        self.out_dir = out_dir

    def generateCode(self, test):
        """
            Generate code has to be smart enough to determine if the json array should generate a test case, or a
            fixture or if it needs to generate both.

            * If setup or teardown is present, then its a test case
            * If parent is present, then it needs to extend a fixture
        """
        #TODO: Maybe we should have a yaml validation class?
        #Totaly agree - that makes perfect sense.
        from jinja2 import Environment, FileSystemLoader
        from time import strftime, gmtime

        # TODO: Find a more efficient way to pull in this template other than ../
        # Is is possible to parameterize the template directory?  It should be a static location... - Alex
        # Maybe we can use the PackageLoader
        out_path = "%s/../../../../../templates/test/" % os.path.dirname(os.path.abspath(__file__))
        j2_env = Environment(loader=FileSystemLoader(out_path), trim_blocks=True)

        # Header lines created here and added to the templates as required
        header = "#!/usr/bin/python\n" \
                 "#\n" \
                 "# This file was created by etlUnit.\n#" \
                 " Create date: %s\n" \
                 "#\n" % \
                 strftime("%a, %d %b %Y %X +0000", gmtime())

        for yml in self.yaml_data.keys():
            self.log.info("Generating code from %s..." % yml)
            self.yml_data = self.yaml_data[yml]

            # TODO: Determine how we handle dependencies on single files.
            # TODO: Added fixture definition to the mix. Currently it generates a fixture but it has no variables.
            try:
                if self.yml_data['fixture'] is not None:
                    self.fixture = self.yml_data['fixture']
                    # TODO: At this point we need to try and read in the fixture definition and THEN generate from the template.
                    self.template_output = j2_env.get_template("testfixture.jj2")\
                        .render(header=header,
                                fixture=self.fixture)

                    self.persist_output(self.yml_data['fixture'], self.template_output, test)
            except KeyError:
                self.fixture = "unittest.TestCase"  # Default value for fixture
                self.log.info("Fixture not present, generating TestSuite...")
            finally:
                self.template_output = j2_env.get_template("testsuite.jj2") \
                    .render(header=header,
                            fixture=self.fixture,
                            tests=self.yml_data['tests'],
                            suitename=self.yml_data['name'].replace(' ', ''))

                self.persist_output(self.yml_data['name'], self.template_output, test)
        self.log.info("Code generation complete.")

    def persist_output(self, name, output, test):
        if test:
            self.log.testing('\n' + self.template_output + '\n')
        else:
            file_path = "%s/%s.py" % (self.out_dir, name.replace(' ', ''))
            self.log.debug("Writing %s" % file_path)
            with open(file_path, 'w') as f:
                os.chmod(f.name, 0770)

                f.write(output)
                f.close()
