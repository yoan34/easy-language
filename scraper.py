import requests
from bs4 import BeautifulSoup
import json
import os
import openai

from dotenv import load_dotenv

load_dotenv()

    
def get_html(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return BeautifulSoup(response.content.decode('utf-8', 'ignore'),'html.parser')


def get_verbs():
    verbs = {}
    for letter in range(ord('a'), ord('z')+1):
        r = get_html(f"https://www.abaenglish.com/fr/verbes-anglais/avec-{chr(letter)}/")
        for row in r.find_all("tr"):
            data = row.find_all('td')
            if len(data) == 4:
                english, past_simple, past_participe, french = [d.text.strip() for d in data]
                if english not in verbs and english != 'Infinitive':
                    verbs[english] = {
                        "past_simple": past_simple,
                        "past_participe": past_participe,
                        "french": french
                    }
    with open("verbs.json", "w") as f:
        json.dump(verbs, f, indent=4)
        

def get_nouns():
    with open("nouns.txt", "w") as f:
        r = get_html(f"https://7esl.com/list-of-nouns/")
        for line in r.find_all("li", attrs={'class': None}):
            print(line.text.strip(), file=f)
            if str(line) == "<li>Youth</li>":
                break
            
        


if __name__ == "__main__":

    nouns = []
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    with open("nouns.txt", "r") as f:
        for line in f:
            nouns.append(line.replace('\n', ''))
  
    
    with open("nouns_with_gpt_update2.txt", "a") as f:
        
        for i in range(0, len(nouns), 200):
            j = i + 200
            nouns_chunk = nouns[i:j]
            print(nouns_chunk)
            prompt = f"""
            f"peux-tu dans un format CSV avec comme en-tête nom;tag;info1;info2 avec comme tag par exemple animal, vegetable, object, human, transport, work, nature et autre.
            Et pour info1 si c'est abstract ouconcrete et info2 si c'est countable ou uncountable. N'écris rien d'autre que les lignes des noms sous forme CSV. quelques exemples:
            apple;vegetable;concrete;coutnable;
            car;transport;concrete;countable
            mind;human;abstract;countable
            Voici la liste des noms: {nouns_chunk}"
            """
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                {"role": "user", "content": prompt}
                ]
            )
            print(completion.choices[0].message.content, file=f)
        
        
    
