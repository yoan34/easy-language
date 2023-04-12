import os
import json
from dotenv import load_dotenv

load_dotenv()



verbs = {}
with open("save_verbs.json", "r") as f:
  d = json.load(f)
  verbs = d
  f.close()

new_verbs = []
with open("verbs.txt", "r") as f:
  for line in f:
    verb, level, frequency = line.replace('\n', '').split(';')
    print(f"verb: {verb} -- level: {level} -- frequency: {frequency}")
    new_verbs.append({
      "infinity": verb,
      "past_simple": verbs[verb]['past_simple'],
      "past_participe": verbs[verb]['past_participe'],
      "french": verbs[verb]['french'],
      "level": verbs[verb]['level'],
      "frequency": int(verbs[verb]['frequency'])
    })


with open('save_verbs.json', "w") as f:
  f.write(json.dumps(new_verbs, indent=4))
    
