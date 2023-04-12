import os
import json
from dotenv import load_dotenv

load_dotenv()



# get the verbs/nouns in JSON file
verbs = []
with open("save_verbs.json", "r") as f:
  d = json.load(f)
  verbs = d
  f.close()


print(f"number of verbs: {len(verbs)}")


with open("verbs_exemple.txt", "r") as f:
  for line in f:
    line = line.replace('\n', '').split(';')
    
    print(line[0])
    verb = list(filter(lambda x: x['infinity'] == line[0], verbs))[0]
    if 'examples' not in verb:
      verb['examples'] = []
    verb['examples'].append((line[1], line[2]))
    
print(verbs)

with open('save_verbs.json', "w") as f:
  f.write(json.dumps(verbs, indent=4))
    
