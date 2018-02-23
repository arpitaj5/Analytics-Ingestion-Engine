import os
import json
import sys


def create_timed_rotating_log(PATH, name_age):
    """
    PATH: global variable - 
    
    """
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
 
    handler = TimedRotatingFileHandler(PATH,
                                       when="m",
                                       interval=2,
                                       backupCount=5)
    logger.addHandler(handler)
    
 
    logger.info(name_age)


try:
    prefix = sys.argv[1]
except:
    print "Error: No argument passed!!"


print "checking files with prefix"
prefixed = [filename for filename in os.listdir('/srv/runme') if filename.startswith(prefix)]

# if there are no files with prefix name. Exit code
if not prefixed:
    print "No file starts with this name"
    exit()

PATH = "/srv/runme/" + prefix + "/proc.txt"

for filename in prefixed:
    with open('/srv/runme/'+filename, 'r') as f:
        try:
            file = f.readlines()
        except:
            pass
    print len(file)
    for line in file:
        try:
            j_line = json.loads(line)
            if ('name' in j_line) and ('prop' in j_line) and ('age' in j_line['prop']) and (j_line['prop']['age'] > 0):

                name_age = j_line['name'] + "\t" + str(j_line['prop']['age'])+"\n"
                create_timed_rotating_log(PATH, name_age)
        except:
            pass


#os.system('mv /home/testtest/Analytics-Ingestion-Engine/' + prefix + '.txt /srv/runme/')

