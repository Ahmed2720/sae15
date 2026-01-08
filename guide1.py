import markdown
import requests

def get_node_name(id:int):
    url = f"https://api.openstreetmap.org/api/0.6/node/{id}.json" # On met l'id dans l'url a l'aide d'un f string ??? (pas sur d'avoir totalement compris)
    reponse = requests.get(url) # on recupere les info via une requete a l'aide de l'url
    donnes = reponse.json() # conversion de notre reponse en json dans une variable donnes
    if len(data['elements']) > 0: # On verifie juste que la liste elements n'est pas vide
        element = donnes['elements'][0] # On stocke dans element la valeur de la cle elemnts du dico donnes qui est une liste elle meme
        if 'tags' in element: # Si il y a une cle tags dans la liste de dico elements 
            return element['tags'].get('name') # on recupere la valeur de la cle name
    return "Sans Nom"

# Version renvoyer dico ??
def print_node_attributes(id):
    url = f"https://api.openstreetmap.org/api/0.6/node/{id}.json"
    reponse = requests.get(url)
    donnes = reponse.json()
    element = donnes['elements'][0]
    return element["tags"]

# Version mieux peut etre ??
def print_node_attributes(id:int):
    url = f"https://api.openstreetmap.org/api/0.6/node/{id}.json"
    reponse = requests.get(url)
    donnes = reponse.json() # conversion de notre reponse en json dans une variable donnes
    element = donnes['elements'][0]
    if "tags" in element: # On vérifie la présence de tags
        for c,v in element["tags"].items(): #Boucle pour acceder a la fois a la cle et a la valeur
            print(c,":",v)
    

