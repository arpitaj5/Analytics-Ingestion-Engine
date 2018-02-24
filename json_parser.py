import os
import json
import sys
import glob
import logging
import time
from logging.handlers import TimedRotatingFileHandler

prefix = sys.argv[1]
dir = "/srv/runme/" + prefix
PATH = dir + "/proc.txt"

if glob.glob(PATH+"*") != []:
    for f in glob.glob(PATH+"*"):
        os.remove(f)


logging_level = logging.DEBUG
formatter = logging.Formatter()
handler = logging.handlers.TimedRotatingFileHandler(PATH, when="M", interval=2, backupCount=10)
handler.setFormatter(formatter)
logger = logging.getLogger("Rotating Log")
logger.addHandler(handler)
logger.setLevel(logging_level)


files = [filename for filename in glob.glob(dir + "/*") if 'Raw.txt' in filename]
for filename in files:
    with open(filename, 'r') as f:
        try:
            file = f.readlines()
        except:
            print('Bad input!!')

    name_age = []
    for line in file:
        try:
            j_line = json.loads(line)
            name = j_line['name']
            age = j_line['prop']['age']
            if (age > 0):
                name_age.append(name + "\t" + str(age))
        except:
            pass
    with open(PATH, 'a'):
        for name_age_str in name_age:
            logger.debug(name_age_str)