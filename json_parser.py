import os
import json
import sys
from os.path import expanduser

def extract_info(line, text_file):
    """
    For each json blob extract name and age and write them to the given file

    rtype: None
    """
    json_text = json.loads(line)
    try:
        name = json_text['name']
        age = json_text['prop']['age']
        if (name != '') and (age != '') and (int(age) > 0):
            text_file.write(str(name) + "\t" + str(age) + '\n')
        else: pass
    except: pass

# run script
PATH = "/srv/runme/"

try:
    prefix = sys.argv[1]
except:
    print "Error: No argument passed!!"

if os.path.exists(PATH):
    json_files = [filename for filename in os.listdir(PATH) if filename.startswith(prefix)]

    if len(json_files) == 0:
        print "No file starts with this name"
        exit(0)

    with open(PATH + str(prefix) + '.txt', 'w') as text_file:

        for filename in json_files:

            with open(PATH + str(filename), 'r') as f:
                for line in f:
                    try:
                        extract_info(line, text_file)

                    except:
                        pass
    text_file.close()
else: 
    print("Directory " + PATH + " does not exist")

