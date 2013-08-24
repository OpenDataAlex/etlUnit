__author__ = 'coty'

from setuptools import setup, find_packages
import etlunit


setup(
    name='etlUnit',
    version=etlunit.__version__,
    url='http://github.com/dbaAlex/etlunit',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    description='Test framework for ETL code.',
    author='Alex Meadows, Coty Sutherland',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'jinja2',
        'sqlalchemy'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta'
        'Natural Language :: English',
    ]
)
