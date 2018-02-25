from flask import Flask
import logging
import time
import sys
import os
import shutil
from logging.handlers import TimedRotatingFileHandler
import json


"""
	Code is used to take input from user as a GET request.
	We then store the request in a Raw file.
	If we have a valid JSON request, we also store the parsed result in proc.txt
"""

app = Flask(__name__)

prefix = sys.argv[1]
dir = "/srv/runme/" + prefix
PATH_RAW = dir + "/Raw.txt" # raw input
PATH_PARSED = dir + "/proc.txt" # processed input

# creating firectory
if(os.path.exists(dir)):
    shutil.rmtree(dir)
os.mkdir(dir)


# log initialization and creating handlers
logging_level_raw = logging.DEBUG
logging_level_parsed = logging.DEBUG

logger_raw = logging.getLogger('raw file')
logger_parsed = logging.getLogger('parsed file')

# two minute rotation
log_handler_raw = logging.handlers.TimedRotatingFileHandler(PATH_RAW, when="M", interval=2, backupCount=10)
log_handler_parsed = logging.handlers.TimedRotatingFileHandler(PATH_PARSED, when="M", interval=2, backupCount=10)

logger_raw.addHandler(log_handler_raw)
logger_parsed.addHandler(log_handler_parsed)

logger_raw.setLevel(logging_level_raw)
logger_parsed.setLevel(logging_level_parsed)



@app.route("/<json_txt>")
def store_json(json_txt):
    """	
	This function is called each time a new user input is sent.
	Data is stored in log rotated file called Raw.txt -> rotated every 2 minutes.
	Any valid JSON string is stored in proc.txt -> rotated every 2 minutes
    """
    json_txt = json_txt.replace('\n', '') # remove hard returns
    with open(PATH_RAW, 'a'):
        logger_raw.debug(json_txt) # store in raw
    try:
	# process json
        j_line = json.loads(json_txt)
        name = j_line['name']
        age = j_line['prop']['age']
        # if valid age
	if (age > 0):
            with open(PATH_PARSED, 'a'):
                logger_parsed.debug(name + "\t" + str(age)) # store in processed
    except KeyError:
	print "KeyError"
      	pass
    except ValueError:
	print "ValueError"
	pass

    return ""


app.run(host='0.0.0.0', port=8080)
