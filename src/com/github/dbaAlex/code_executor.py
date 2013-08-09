__author__ = 'coty'

import logging
from settings import etlunit_config, console


class CodeExecutor():
    """
        Class that executes the code that we built from the templates.
    """

    def __init__(self, out_dir):
        self.log = logging.getLogger(name='CodeGenerator')
        self.log.setLevel(etlunit_config['logging_level'])
        self.log.addHandler(console)

        self.out_dir = out_dir

    def execute(self):
        from os import listdir
        from os.path import isfile, join

        # TODO: Should this list every file in the out_dir? What if we didn't create it? How do we mitigate that?
        onlyfiles = [f for f in listdir(self.out_dir) if isfile(join(self.out_dir, f))]

        self.log.debug(onlyfiles)

        # TODO: It looks like when you have no command that it doesnt fail...it just does nothing. Plz 2 fix.
        import subprocess
        for f in onlyfiles:
            file_path = "%s/%s" % (self.out_dir, f)
            self.log.debug(file_path)
            subprocess.call(file_path, cwd=self.out_dir)

        # this block will work ONLY for python files :)
        # for f in onlyfiles:
        #    file_path = "%s/%s" % (self.out_dir, f)
        #    execfile(file_path)