import markdown
import requests

def get_node(id:int) -> dict:
    url = f"https://api.openstreetmap.org/api/0.6/node/{id}.json"
    reponse = requests.get(url)
    donnes = reponse.json()
    if len(donnes['elements']) > 0:
        return donnes['elements'][0]
    
def node_to_md(data:dict,fichier:str) -> None:
