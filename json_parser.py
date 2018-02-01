import os
import json
prefix = sys.argv[1]

prefixed = [filename for filename in os.listdir('srv/runme') if filename.startswith(prefix)]

# if there are no files with prefix name. Exit code
if not prefixed:
	print "No file starts with this name"
	exit()

name = list()
age = list()
for filename in prefixed:
	with open('srv/runme/'+filename, 'r') as f:
		try:
	    	datastore = json.load(f)
	    except:
	    	pass
	for i in range(len(datastore)):
		name.append(datastore[i]['name'])
		age.append(datastore[i]['prop']['age'])

fh = open("srv/runme/"+prefix+".txt", "w")
for i in range(len(name)):
	fh.write(name[i] + "\t" + str(age[i])+"\n")
fh.close()