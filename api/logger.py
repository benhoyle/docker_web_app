"""Logging configuration for the API."""
# See https://www.pylenin.com/blogs/python-logging-guide/#logging-from-multiple-modules
import logging
import os
import sys

# Define module logger
logger = logging.getLogger(__name__)
# create console handler and set level to debug
consoleHandler = logging.StreamHandler(stream=sys.stderr)

# create formatter - can also use %(lineno)d -
# see https://stackoverflow.com/questions/533048/how-to-log-source-file-name-and-line-number-in-python/44401529
formatter = logging.Formatter(
    '%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s | %(filename)s > %(module)s > %(funcName)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# add formatter to ch
consoleHandler.setFormatter(formatter)

# add ch to logger
logger.addHandler(consoleHandler)

# Get logging level from environment variable - tweak to convert to boolean
DEBUG_MODE = (os.environ.get('DEBUG_MODE', 'False') == 'True')
if DEBUG_MODE:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)
