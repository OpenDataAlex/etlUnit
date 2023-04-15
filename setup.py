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

setup(
    name='etlUnit',
    version=etlunit.__version__,
    url='http://github.com/dbaAlex/etlunit',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    description='Test framework for ETL code.',
    author='Alex Meadows, Coty Sutherland',
    packages=find_packages(),
    install_requires=[
        'Jinja2==2.7.1',
        'MarkupSafe==0.18',
        'MySQL-python==1.2.4',
        'PyYAML==3.10',
        'Pygments==1.6',
        'SQLAlchemy==0.8.2',
        'Sphinx==1.2b1',
        'docutils==0.11',
        'py==1.11.0',
        'tox==1.6.0',
        'unittest-xml-reporting==1.5.0',
        'virtualenv==1.10.1',
        'wsgiref==0.1.2',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta'
        'Natural Language :: English',
    ],
    cmdclass = {'tox': Tox},
    test_suite='etlunit.test'
)
