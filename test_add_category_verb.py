import os
import json
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

with open("save_verbs.json", "r") as f:
  d = json.load(f)
  verbs = d
  
print(len(verbs))

verbs = list(verbs)[:250]
with open("category_verbs.txt", "a") as f:
  for i in range(0, len(verbs), 50):
      j = i + 50
      verbs_chunk = verbs[i:j]
      print(verbs_chunk)
      
      completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "user", "content": f"Peux-tu classer les verbes suivants avec une catégorie par exemple, 'action physique', 'action mental', 'sentiment' et d'autres que tu pourrais créer. Voici la liste {verbs_chunk}"}
        ]
      )
      print(completion.choices[0].message.content, file=f)