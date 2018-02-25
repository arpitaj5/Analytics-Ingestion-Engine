from flask import Flask
import logging
import time
import sys 
import os
import shutil
from logging.handlers import TimedRotatingFileHandler

app = Flask(__name__)

prefix = sys.argv[1]
dir = "/srv/runme/" + prefix
PATH_RAW = dir + "/Raw.txt"
PATH_PARSED = dir + "/proc.txt"


if(os.path.exists(dir)):
    shutil.rmtree(dir)
os.mkdir(dir)

logging_level = logging.DEBUG
formatter = logging.Formatter()

handler_raw = logging.handlers.TimedRotatingFileHandler(PATH_RAW, when="M", interval=2, backupCount=10)
handler_parsed = logging.handlers.TimedRotatingFileHandler(PATH_PARSED, when="M", interval=2, backupCount=10)

handler_raw.setFormatter(formatter)
handler_parsed.setFormatter(formatter)

logger_raw = logging.getLogger() 
logger_raw.addHandler(handler_raw)
logger_raw.setLevel(logging_level)

logger_parsed = logging.getLogger() 
logger_parsed.addHandler(handler_parsed)
logger_parsed.setLevel(logging_level)

@app.route("/<json_txt>")
def store_json(json_txt):
    json_txt = json_txt.replace('\n', '')
    with open(PATH, 'a'):
        logger_raw.debug(json_txt)

    name_age = []
    try:
    	j_line = json.loads(line)
        name = j_line['name']
        age = j_line['prop']['age']
        if (age > 0):
            logger_parsed.debug(name + "\t" + str(age))
    except:
    	pass
        
    return "testing"



app.run(host='0.0.0.0', port=8080)
