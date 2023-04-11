import os
import json
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

with open("verbs.json", "r") as f:
  d = json.load(f)
  verbs = d
  
print(len(verbs))

verbs = list(verbs)
with open("verbs.txt", "a") as f:
  for i in range(0, len(verbs), 50):
      j = i + 50
      verbs_chunk = verbs[i:j]
      print(verbs_chunk)
      
      completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "user", "content": f"Peux-tu classer les verbes suivants avec un niveau (A1,A2,B1,B2,C1,C2) et une fréquence d'apparition entre 1 et 10. Un verbe par ligne de la forme: eat;A1;10 par exemple. Voici la liste {verbs_chunk}"}
        ]
      )
      print(completion.choices[0].message.content, file=f)
    
    
 




