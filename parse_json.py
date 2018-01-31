import json
import sys

prefix = sys.argv[1]

try: # prefix might not exist
    with open(prefix+'.json') as f:
        file = json.load(f)
except:
    pass

file_w = []
for d in file:
    try: # age or name attibutes might not exist
        name = d['name']
        age = str(d['prop']['age'])
        file_w.append(name+'\t'+age)
    except:
        pass
    
try: # prefix might not exist
    with open(prefix+'.txt', 'w') as f:
        for line in file_w:
            f.write(line+'\n')
except:
    pass