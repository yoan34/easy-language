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
  
    
    nouns = nouns[:100]
    with open("nouns_with_gpt_update.txt", "a") as f:
        
        for i in range(0, len(nouns), 50):
            j = i + 50
            nouns_chunk = nouns[i:j]
            print(nouns_chunk)
            
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                {"role": "user", "content": f"peux-tu traduire, citer une catégorie pour les noms suivant, un niveau entre A1,A2,B1,B2,C1,C2 et un score de fréquence entre 1 et 10 de la forme: apple;pomme;A1;7;fruit par exemple. Voici la liste des noms: {nouns_chunk}"}
                ]
            )
            print(completion.choices[0].message.content, file=f)
        
        
    
