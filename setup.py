__author__ = 'coty'

from setuptools import setup, find_packages

setup(name='etlUnit',
      packages=find_packages(),
      version='0.1',
      description='Test framework for ETL code.',
      author='Alex Meadows, Coty Sutherland',
      install_requires=[
          'pyyaml',
          'jinja2',
          'sqlalchemy'
      ],
)