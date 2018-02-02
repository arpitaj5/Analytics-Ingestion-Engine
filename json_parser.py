import os
import json
import sys
prefix = sys.argv[1]


print "checking files with prefix"
prefixed = [filename for filename in os.listdir('/srv/runme') if filename.startswith(prefix)]

# if there are no files with prefix name. Exit code
if not prefixed:
    print "No file starts with this name"
    exit()

name = list()
age = list()

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
            name.append(j_line['name'])
            age.append(j_line['prop']['age'])
        except:
            pass

fh = open('/home/ec2-user/Analytics-Ingestion-Engine/'+prefix+".txt", "w")
for i in range(len(name)):
    fh.write(name[i] + "\t" + str(age[i])+"\n")
fh.close()

os.system('sudo mv /home/ec2-user/Analytics-Ingestion-Engine/' + prefix + '.txt /srv/runme/')