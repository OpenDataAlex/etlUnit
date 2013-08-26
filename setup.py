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
        'Jinja2==2.7.1',
        'MarkupSafe==0.18',
        'MySQL-python==1.2.4',
        'PyYAML==3.10',
        'SQLAlchemy==0.8.2',
        'unittest-xml-reporting==1.5.0',
        'wsgiref==0.1.2',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta'
        'Natural Language :: English',
    ],
    test_requires='unittest',
    test_suite='etlunit.test'
)
