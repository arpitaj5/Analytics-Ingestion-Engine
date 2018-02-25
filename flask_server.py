from flask import Flask
import logging
import time
import sys
import os
import shutil
from logging.handlers import TimedRotatingFileHandler
import json

app = Flask(__name__)

prefix = sys.argv[1]
dir = "/srv/runme/" + prefix
PATH_RAW = dir + "/Raw.txt"
PATH_PARSED = dir + "/proc.txt"


if(os.path.exists(dir)):
    shutil.rmtree(dir)
os.mkdir(dir)

logging_level_raw = logging.DEBUG
logging_level_parsed = logging.DEBUG

logger_raw = logging.getLogger('raw file')
logger_parsed = logging.getLogger('parsed file')

log_handler_raw = logging.handlers.TimedRotatingFileHandler(PATH_RAW, when="M", interval=2, backupCount=10)
log_handler_parsed = logging.handlers.TimedRotatingFileHandler(PATH_PARSED, when="M", interval=2, backupCount=10)

logger_raw.addHandler(log_handler_raw)
logger_parsed.addHandler(log_handler_parsed)


logger_raw.setLevel(logging_level_raw)
logger_parsed.setLevel(logging_level_parsed)



@app.route("/<json_txt>")
def store_json(json_txt):
    json_txt = json_txt.replace('\n', '')
    with open(PATH_RAW, 'a'):
        logger_raw.debug(json_txt)
    try:
        j_line = json.loads(json_txt)
        name = j_line['name']
        age = j_line['prop']['age']
        if (age > 0):
            with open(PATH_PARSED, 'a'):
                logger_parsed.debug(name + "\t" + str(age))
    except:
        pass

    return ""


app.run(host='0.0.0.0', port=8080)
