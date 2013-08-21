__author__ = 'coty'

import yaml


connections = {}

try:
    filename = '/home/coty/custom/source/etlUnit/res/jinja2/connections.yml'
    with open(filename, 'r') as f:
        prop_list = yaml.load(f.read())
        connections = prop_list
except:
    print "Unable to load connections file."
    exit()