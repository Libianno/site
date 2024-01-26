from googlesearch import search 
from rich.pretty import pprint
import json

def get_animes():
    with open('scripts/listanimes.json', 'r') as animes:
        animes = animes.read()
        animes = json.loads(animes)
        return animes['animes']

def get_links(animes):
    base_name = 'crunchyroll'
    dicionario_de_animes = {}
    for anime in animes:  
        dicionario_de_animes[anime] = next(search(base_name + anime))
    return dicionario_de_animes

def write_json(animes):
    with open('animes.json', 'w') as jsonanimes:
        jsonanimes.write(animes)
        
    

if __name__ == '__main__':
    animes = get_animes()
    animes = get_links(animes)
    animes = json.dumps(animes, indent=2)
    write_json(animes)
