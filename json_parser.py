import os
import json
import sys
import glob
import logging
import time 
from logging.handlers import TimedRotatingFileHandler

#def create_timed_rotating_log(path, name_age):
    """
    PATH: global variable - 
    
    
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
    handler = TimedRotatingFileHandler(path,
                                       when="m",
                                       interval=2)
    logger.addHandler(handler)
    logger.info(name_age)
    """

def main():
    try:
        prefix = sys.argv[1]
    except:
        print "Error: No argument passed!!"

    PATH = "/srv/runme/" + prefix + "/proc.txt"

    if glob.glob(PATH+"*") != []:
        for f in glob.glob(PATH+"*"):
            os.remove(f)


    logging_level = logging.DEBUG
    formatter = logging.Formatter()
    handler = logging.handlers.TimedRotatingFileHandler(PATH, when="M", interval=2, backupCount=10)
    handler.setFormatter(formatter)
    logger = logging.getLogger("Rotating Log") # or pass string to give it a name
    logger.addHandler(handler)
    logger.setLevel(logging_level)
:
    for filename in glob.glob("/srv/runme/" + prefix + "/*"):
        if 'Raw.txt' in filename:
            with open(filename, 'r') as f:
                try:
                    file = f.readlines()
                except:
                    pass
            print len(file)
            for line in file:
                try:
                    j_line = json.loads(line)
                    if ('name' in j_line) and ('prop' in j_line) and ('age' in j_line['prop']) and (j_line['prop']['age'] > 0):
                        
                        name_age = j_line['name'] + "\t" + str(j_line['prop']['age'])
                        with open(PATH, 'a'):
                            logger.debug(name_age)                   
                except:
                    pass

if (__name__ ==' __main__'):
    main()


