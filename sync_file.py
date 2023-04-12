import os
import json


# get the verbs/nouns in JSON file
nouns = []
with open("nouns_french_level_frequency.txt", "r") as f:
  for noun in f:
      noun = noun.replace('\n', '')
      noun, french, level, frequency = noun.split(';')
      nouns.append(noun)
      
print(f"in file nouns_french_level_frequency -> {len(nouns)} nouns.")
      
      
# get the verbs/nouns in JSON file
other_nouns = []
with open("nouns_tag_info1_info2.txt", "r") as f:
  for noun in f:
      noun = noun.replace('\n', '')
      noun, french, level, frequency, _ = noun.split(';')
      other_nouns.append(noun)
      
      
print(f"in file nouns_with_gpt_update2 -> {len(other_nouns)} nouns.")

for noun in nouns:
    if noun not in other_nouns:
        print(f'ERROR: {noun}')
      