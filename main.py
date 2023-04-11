import os
import openai
import datetime
openai.api_key = "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"



for letter in ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
  with open(f"verb_{letter}.txt", "w") as f:
    a = datetime.datetime.now()
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": f"Peux-tu créer une liste des verbes les plus courants qui commence par '{letter}' en anglais, séparer par un point-virgule ';' et les en-têtes sont verbe;traduction française;niveau (A1,A2,B1,B2,C1,C2);score de fréquence entre 1 à 10;"}
      ]
    )
    b = datetime.datetime.now()
    print(f"TIME: {b-a}")
    print(completion.choices[0].message.content, file=f)