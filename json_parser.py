import os
import json
import sys
import glob
import logging
import time
 
from logging.handlers import TimedRotatingFileHandler

def create_timed_rotating_log(name_age):
    """
    PATH: global variable - 
    
    """
    logger.info(name_age)


try:
    prefix = sys.argv[1]
except:
    print "Error: No argument passed!!"


#print "checking files with prefix"
#prefixed = [filename for filename in os.listdir('/srv/runme') if filename.startswith(prefix)]

# if there are no files with prefix name. Exit code
#if not prefixed:
 #   print "No file starts with this name"
  #  exit()

PATH = "/srv/runme/" + prefix + "/proc.txt"

print "/srv/runme/" + prefix
#print glob.glob("/srv/runme/" + prefix)

#if(os.path.exists(PATH+"*")):

if glob.glob(PATH+"*") != []:
    for f in glob.glob(PATH+"*"):
        os.remove(f)


logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler(PATH,
                                       when="m",
                                       interval=2,
                                       backupCount=5)
logger.addHandler(handler)

for filename in glob.glob("/srv/runme/" + prefix + "/*"):
    print filename
    if 'Raw.txt' in filename:
        print "Found file" + filename
        with open(filename, 'r') as f:
            try:
                file = f.readlines()
            except:
                pass
        print len(file)
        for line in file:
            try:
                j_line = json.loads(line)
                print j_line
                if ('name' in j_line) and ('prop' in j_line) and ('age' in j_line['prop']) and (j_line['prop']['age'] > 0):
                    
                    name_age = j_line['name'] + "\t" + str(j_line['prop']['age'])+"\n"
                    print name_age
                    create_timed_rotating_log(name_age)
                    
            except:
                pass


#os.system('mv /home/testtest/Analytics-Ingestion-Engine/' + prefix + '.txt /srv/runme/')

