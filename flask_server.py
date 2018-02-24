from flask import Flask
import logging
import time
import sys 
import os
import shutil
from logging.handlers import TimedRotatingFileHandler


app = Flask(__name__)

prefix = sys.argv[1]
PATH = "/srv/runme/" + prefix + "/Raw.txt"


if(os.path.exists("/srv/runme/" + prefix)):
    shutil.rmtree("/srv/runme/" + prefix)
os.mkdir("/srv/runme/" + prefix)

logging_level = logging.DEBUG

formatter = logging.Formatter()

handler = logging.handlers.TimedRotatingFileHandler(PATH, when="M", interval=2, backupCount=10)

handler.setFormatter(formatter)

logger = logging.getLogger() # or pass string to give it a name

logger.addHandler(handler)

logger.setLevel(logging_level)

@app.route("/<json_txt>")
def store_json(json_txt):
    json_txt = json_txt.replace('\n', '')
    with open(PATH, 'a'):
        logger.debug(json_txt)
    return "testing"



app.run(host='0.0.0.0', port=8080)
