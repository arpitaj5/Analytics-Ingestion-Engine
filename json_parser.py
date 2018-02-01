import os
import json
prefix = 'lala'
prefixed = [filename for filename in os.listdir('srv/runme') if filename.startswith(prefix)]


name = list()
age = list()
for filename in prefixed:
	with open('srv/runme/'+filename, 'r') as f:
	    datastore = json.load(f)
	for i in range(len(datastore)):
		name.append(datastore[i]['name'])
		age.append(datastore[i]['prop']['age'])

fh = open("srv/runme/"+prefix+".txt", "w")
for i in range(len(name)):
	fh.write(name[i] + "	" + str(age[i])+"\n")
fh.close()