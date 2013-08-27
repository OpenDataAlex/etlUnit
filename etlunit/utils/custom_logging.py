"""
    This file was created to house custom logging functions.
"""

__author__ = 'coty'

import logging


# Created a trace category for things less than debug to print on
TRACE = 5
logging.addLevelName(TRACE, 'TRACE')


def trace(self, message, *args, **kws):
    """
        This method creates the trace method on the logger that were using allowing me to use log.trace() in my code.
    """
    self.log(TRACE, message, *args, **kws)
logging.Logger.trace = trace

# This category was created as a result to the test option. When that opt is used, then this category prints the
# output from test logging.
TESTING = 21
logging.addLevelName(TESTING, 'TESTING')


def testing(self, message, *args, **kws):
    """
        This method creates the testing method on the logger that were using allowing me to use log.testing() in my
        code. This specific level is for the preview mode that the application can run it. It prints what code it
        generates instead of writing it to a file under the TESTING level.
    """
    self.log(TESTING, message, *args, **kws)
logging.Logger.testing = testing
