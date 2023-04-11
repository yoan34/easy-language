import requests
from bs4 import BeautifulSoup

def get_urls():
    # Test si les critères de selection sont correct
    try:

        # On récupère le HTML de la page d'accueil
        # et on retoune une liste d'URLS des catégories.
        html = self.get_html(self.url)
        urls = (html.find('ul', {'class': 'nav nav-list'})
                .find('ul').findAll('a'))
        urls = [self.url + url['href'] for url in urls]
    except Exception:
        print("The criteria are not suitable, check them on the url: {}"
                .format(self.url))
    else:
        return urls
    
def get_html(url):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return BeautifulSoup(response.content.decode('utf-8', 'ignore'),'html.parser')


if __name__ == "__main__":
    
    r = get_html("https://www.abaenglish.com/fr/verbes-anglais/avec-a/")


        
    for row in r.find_all("tr"):
        data = row.find_all('td')
        if len(data) == 4:
            accent_word, accented_1, accented_2, french_word = [d.text.strip() for d in data]
        print(accent_word, accented_1, accented_2, french_word)