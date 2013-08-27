__author__ = 'coty'

from setuptools import setup, find_packages
import etlunit
from setuptools.command.test import test as TestCommand
import sys

class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

import os

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='etlUnit',
    version=etlunit.__version__,
    url='http://github.com/dbaAlex/etlunit',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    description='Test framework for ETL code.',
    author='Alex Meadows, Coty Sutherland',
    packages=find_packages(),
    install_requires=required,
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta'
        'Natural Language :: English',
    ],
    cmdclass = {'tox': Tox},
    test_suite='etlunit.test'
)
