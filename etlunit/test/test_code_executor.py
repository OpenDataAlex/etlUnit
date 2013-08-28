"""
    This module is for testing the code_executor module.
"""

__author__ = 'coty'

import unittest
import os
from etlunit.code_executor import CodeExecutor


class code_executor_tests(unittest.TestCase):

    def setUp(self):
        self.one_dir_path = self.setup_oneFile()
        self.multi_dir_path = self.setup_twoFiles()

    def setup_oneFile(self):
        from tempfile import mkdtemp, mkstemp
        dir_path = mkdtemp()

        (fh, f_path) = mkstemp(suffix='.py', dir=dir_path)
        f = os.fdopen(fh, 'w')
        f.write("#!/usr/bin/python\n\nimport sys\nsys.exit(1)")
        os.chmod(f_path, 0770)
        f.close()

        return dir_path

    def setup_twoFiles(self):
        from tempfile import mkdtemp, mkstemp
        dir_path = mkdtemp()

        (fh, f_path) = mkstemp(suffix='.py', dir=dir_path)
        f = os.fdopen(fh, 'w')
        f.write("#!/usr/bin/python\n\nimport sys\nsys.exit(1)")
        os.chmod(f_path, 0770)
        f.close()

        (fh, f_path) = mkstemp(suffix='.py', dir=dir_path)
        f = os.fdopen(fh, 'w')
        f.write("#!/usr/bin/python\n\nimport sys\nsys.exit(1)")
        os.chmod(f_path, 0770)
        f.close()

        return dir_path

    def tearDown(self):
        from shutil import rmtree
        rmtree(self.one_dir_path)
        rmtree(self.multi_dir_path)

    def test_init(self):
        ce = CodeExecutor("test")
        self.assertEqual("test", ce.out_dir)

    def test_execute_one_test_mode(self):
        ce = CodeExecutor(self.one_dir_path)
        self.assertEqual(ce.execute(True), 0)

    def test_execute_multi_test_mode(self):
        ce = CodeExecutor(self.multi_dir_path)
        self.assertEqual(ce.execute(True), 0)

    def test_execute_one(self):
        ce = CodeExecutor(self.one_dir_path)
        self.assertEqual(ce.execute(False), 1)

    def test_execute_multi(self):
        ce = CodeExecutor(self.multi_dir_path)
        self.assertEqual(ce.execute(False), 1)



