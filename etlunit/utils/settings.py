__author__ = 'coty'

import logging
import pprint
import os
import yaml

# Begin CustomLogging
# this import adds the additional log levels I created
import etlunit.utils.custom_logging

# create console handler and set level to info
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# set formatter
console.setFormatter(formatter)
# End CustomLogging

etlunit_config = {}

settings_log = logging.getLogger(name="settings")
settings_log.setLevel(logging.DEBUG)
settings_log.addHandler(console)

pp = pprint.PrettyPrinter(indent=4)

settings_filename = '.etlunit-settings.yml'

settings_fs_locs = ["{}/{}".format(os.path.expanduser("~"), settings_filename), "".join(settings_filename)]

settings_loaded = False
for the_path in settings_fs_locs:
    settings_log.debug("Attempting to load {}".format(the_path))
    try:
        with open(the_path, 'r') as f:
            prop_list = yaml.load(f.read())
            for key, value in prop_list.items():
                etlunit_config[key] = value

            settings_log.debug("Settings loaded from %s" % the_path)
            settings_loaded = True
            break
    except (OSError, IOError) as e:
        settings_log.warn("{} {}".format(e.strerror, the_path))


if not settings_loaded:
    settings_log.error("Could not find settings file in {}. Using defaults where present".format(','.join(settings_fs_locs)))
    # For now there is nothing in the settings file that is required for operation. Removing the exit call.
    # exit()

# INFO = 20
# TESTING = 21
# DEBUG = 10
# TRACE = 5
try:
    console.level = etlunit_config['logging_level']
except KeyError:
    etlunit_config['logging_level'] = 20  # set default level to info
    console.level = etlunit_config['logging_level']
