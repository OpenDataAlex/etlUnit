# etlUnit

[![Build Status](https://travis-ci.org/dbaAlex/etlUnit.png?branch=develop)](https://travis-ci.org/dbaAlex/etlUnit) [![Coverage Status](https://coveralls.io/repos/dbaAlex/etlUnit/badge.png?branch=develop)](https://coveralls.io/r/dbaAlex/etlUnit?branch=develop)

### Installation

You can install **etlUnit** by downloading the source and using the setup.py script as follows:

    $ git clone https://github.com/dbaAlex/etlUnit.git
    $ cd etlUnit
    $ python setup.py install
   
This setup call installs all of the necessary python dependencies. There are a few external dependencies as well, so please see the section below labeled "Non-Python Dependencies". I have not created any links or anything yet for the installation so you need to refer to the python code in this directly when you run it.

Once you have done that, its ready to run!

### So what is etlUnit anyway?

etlUnit was created because there is no testing framework that truly addresses ETL testing in a manner that fits into
modern coding practices (i.e. object oriented coding) that also interfaces with the various data integration tools.
This is not surprising due to the nature of data integration tools because many of them are proprietary and don't play
 well outside of their tool suites.  etlUnit is designed to use black/grey box testing practices as well as utilize the
 best practices of the xUnit family of testing tools.
 
### Quickstart

To actually use etlUnit, you need a resource file for it to act on. A most basic resource file can be found in the [res](https://github.com/dbaAlex/etlUnit/tree/develop/res) directory of the project (testsuite.yml). Executing the following will take that resource, generate some python code in the output directory specified, and run the code which will display the output of the tests executed to your terminal.

    $ python etlunit/etlUnit.py -f res/testsuite.yml -o /tmp/ -g -e

### Documentation

The documentation for **etlUnit** can be found on Read the Docs [here](https://etlunit.readthedocs.org/en/latest/).

### Non-Python Dependencies

The only dependencies that are not handled in python currently are the ones for SQLAlchemy to connect to datasources. Documentation on how to install these is as follows:

* [MySQL](https://github.com/dbaAlex/etlUnit/blob/develop/docs/mysql_deps.md)
* [Oracle](https://github.com/dbaAlex/etlUnit/blob/develop/docs/oracle_deps.md)

### Reporting Issues

We would love some feedback! Please do not hesitate to report any issues/questions/comments via the [Github Issue Tracker](https://github.com/dbaAlex/etlUnit/issues).
