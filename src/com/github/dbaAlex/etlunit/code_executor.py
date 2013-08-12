__author__ = 'coty'

import logging
from src.com.github.dbaAlex.utils.settings import etlunit_config, console


class CodeExecutor():
    """
        Class that executes the code that we built from the templates.
    """

    def __init__(self, out_dir):
        self.log = logging.getLogger(name='CodeExecutor')
        self.log.setLevel(etlunit_config['logging_level'])
        self.log.addHandler(console)

        self.out_dir = out_dir

    def execute(self, test):
        from os import listdir
        from os.path import isfile, join

        # TODO: Should this list every python file in the out_dir? What if we didn't create it? How do we mitigate that?
        # We can mitigate it via the formatting of the name of the files, a specific fingerprint, etc.  There are a few options... - Alex
        # get a list of all files from out_dir that end with .py
        files = [f for f in listdir(self.out_dir) if isfile(join(self.out_dir, f)) and f.endswith(".py")]

        self.log.debug(files)

        import subprocess
        for f in files:
            file_path = "%s/%s" % (self.out_dir, f)

            if test:
                self.log.testing("Would execute %s" % file_path)
            else:
                self.log.debug(file_path)
                # Using subprocess versus execfile because the unittests will not execute under execfile
                subprocess.call(file_path)
