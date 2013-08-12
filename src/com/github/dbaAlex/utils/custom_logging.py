__author__ = 'coty'

import logging

"""
    This file was created to house custom logging functions.
"""

# Created a trace category for things less than debug to print on
TRACE = 5
logging.addLevelName(TRACE, 'TRACE')

def trace(self, message, *args, **kws):
    self.log(TRACE, message, *args, **kws)
logging.Logger.trace = trace

# This category was created as a result to the test option. When that opt is used, then this category prints the
# output from test logging.
TESTING = 21
logging.addLevelName(TESTING, 'TESTING')

def testing(self, message, *args, **kws):
    self.log(TESTING, message, *args, **kws)
logging.Logger.testing = testing
