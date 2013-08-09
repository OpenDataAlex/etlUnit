__author__ = 'coty'

import logging
from settings import etlunit_config, console


class CodeGenerator():
    """
        This class performs the generation of the code. Using the jinja2 template engine, we are taking in yaml
        and generating code from it by filling in templates.
    """

    def __init__(self, out_dir, arr):
        self.log = logging.getLogger(name='CodeGenerator')
        self.log.setLevel(etlunit_config['logging_level'])
        self.log.addHandler(console)

        # TODO: Update file extension to '.py'
        self.file_ext = '.sh'

        self.arr = arr
        self.out_dir = out_dir

    def generateCode(self):
        from jinja2 import Environment, FileSystemLoader
        import os

        # TODO: Find a more efficient way to pull in this template other than ../
        out_path = "%s/../../../../templates/" % os.path.dirname(os.path.abspath(__file__))
        j2_env = Environment(loader=FileSystemLoader(out_path), trim_blocks=True)
        # TODO: Should the template name be dynamic? Will it changed based on the yaml?
        template_output = j2_env.get_template("%s.tmp" % self.arr[0]['suite']['name'])\
            .render(connections=self.arr[0]['suite']['connections'])

        self.persist_output(template_output)

    def persist_output(self, output):
        import os
        # TODO: Decide if naming the files based on the test name from the yaml is ok
        with open("%s/%s%s" % (self.out_dir, self.arr[0]['suite']['name'], self.file_ext), 'w') as f:
            # TODO: Figure out how to dynamically write the shabang based on file ext...
            # Should probably be a header variable populated based on the file_ext
            f.write("#!/bin/sh\n")

            os.chmod(f.name, 0770)

            f.write(output)
            f.close()
