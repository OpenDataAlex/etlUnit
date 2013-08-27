"""
    This file houses the code that reads in the connections file and instantiates an array of connections keyed on the
    connection name for use by the generated application.
"""

__author__ = 'coty'

import yaml


# create an empty connections array
connections = {}

# populate the array with connections from the YAML file.
try:
    filename = '/home/coty/custom/source/etlUnit/res/connections.yml'
    with open(filename, 'r') as f:
        prop_list = yaml.load(f.read())
        connections = prop_list
except:
    print "Unable to load connections file."
    # exit()