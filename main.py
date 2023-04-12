import os
import json
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")


verbs = {}
with open("save_verbs.json", "r") as f:
  d = json.load(f)
  verbs = d
  
print(f"number of verb: {len(verbs)}")

verbs_sorted_by_level = sorted(verbs, key=lambda x: (x['level'], -x['frequency']))

def get_verbs_by(level):
  return [verb for verb in verbs_sorted_by_level if verb['level'] == level]

verbs_A1 = get_verbs_by('A1')
verbs_A2 = get_verbs_by('A2')
verbs_B1 = get_verbs_by('B1')
verbs_B2 = get_verbs_by('B2')
verbs_C1 = get_verbs_by('C1')

print(len(verbs_A1), len(verbs_A2), len(verbs_B1), len(verbs_B2), len(verbs_C1))
for i in range(len(verbs_B2)):
  if len(verbs_A1) > i:
    va1 = f"{verbs_A1[i]['infinity']:<11} {verbs_A1[i]['level']:<4} {verbs_A1[i]['frequency']:<4}"
  else:
    va1 = " " * 21

  if len(verbs_A2) > i:
    va2 = f"{verbs_A2[i]['infinity']:<11} {verbs_A2[i]['level']:<4} {verbs_A2[i]['frequency']:<4}"
  else:
    va2 = " " * 21
  
  if len(verbs_B1) > i:
    vb1 = f"{verbs_B1[i]['infinity']:<11} {verbs_B1[i]['level']:<4} {verbs_B1[i]['frequency']:<4}"
  else:
    vb1 = " " * 21
  if len(verbs_B2) > i:
    vb2 = f"{verbs_B2[i]['infinity']:<11} {verbs_B2[i]['level']:<4} {verbs_B2[i]['frequency']:<4}"
  else:
    vb2 = " " * 21
  if len(verbs_C1) > i:
    vc1 = f"{verbs_C1[i]['infinity']:<11} {verbs_C1[i]['level']:<4} {verbs_C1[i]['frequency']:<4}"
  else:
    vc1 = " " * 21
  
  print(f"{va1} |    {va2} |    {vb1} |    {vb2} |    {vc1}")

  # print(f"{verb['infinity']:<15} {verb['level']:<4} {verb['frequency']}")







# verbs = list(verbs)
# with open("verbs.txt", "a") as f:
#   for i in range(0, len(verbs), 50):
#       j = i + 50
#       verbs_chunk = verbs[i:j]
#       print(verbs_chunk)
      
#       completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#           {"role": "user", "content": f"Peux-tu classer les verbes suivants avec un niveau (A1,A2,B1,B2,C1,C2) et une fréquence d'apparition entre 1 et 10. Un verbe par ligne de la forme: eat;A1;10 par exemple. Voici la liste {verbs_chunk}"}
#         ]
#       )
#       print(completion.choices[0].message.content, file=f)
    
    
 




