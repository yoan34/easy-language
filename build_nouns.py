import os
import json


# get the verbs/nouns in JSON file
new_nouns = []
nouns = []
with open("nouns_french_level_frequency.txt", "r") as f:
  for noun in f:
      noun = noun.replace('\n', '')
      noun, french, level, frequency = noun.split(';')
      nouns.append(noun)
      print(noun)
      new_nouns.append({
        "noun": noun.capitalize(),
        "french": french.capitalize(),
        "level": level.upper(),
        "frequency": int(frequency)
      })
      
print(f"in file nouns_french_level_frequency -> {len(nouns)} nouns.")
      
      
# get the verbs/nouns in JSON file
other_nouns = []
with open("nouns_tag_info1_info2.txt", "r") as f:
  for noun in f:
      noun = noun.replace('\n', '')
      noun, tag, info1, info2, _ = noun.split(';')
      get_noun = list(filter(lambda x: x['noun'] == noun, new_nouns))[0]
      get_noun["tag"] = tag
      get_noun["info1"] = info1
      get_noun["info2"] = info2
      other_nouns.append(noun)
      
with open('save_nouns.json', "w") as f:
  f.write(json.dumps(new_nouns, indent=4))
    

