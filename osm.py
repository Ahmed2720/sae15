import markdown
import requests

def get_node(id:int) -> dict:
    url = f"https://api.openstreetmap.org/api/0.6/node/{id}.json"
    reponse = requests.get(url)
    donnes = reponse.json()
    return donnes['elements'][0] # on renvoi le dico
    
# Version on trie les info quon veux avec des if    
'''def node_to_md(donnes:dict,fichier:str) -> None:
    with open(fichier, "w", encoding="utf-8") as f:

        if "tags" in donnes and "name" in donnes["tags"]: # On verifie si les cle tags et name son presente dons le dico
            nom = donnes["tags"]["name"]
        else:
            nom = "SANS NOM" # cas ou ya pas la cle name

        f.write(f"# {nom}\n")
        f.write("Voici les informations :\n")
        if "id" in donnes:
            f.write(f"* **ID** : {donnes['id']}\n")
        if "lat" in donnes:
            f.write(f"* **Latitude** : {donnes['lat']}\n")
        if "lon" in donnes:
            f.write(f"* **Longitude** : {donnes['lon']}\n")
        f.write("\n## Tags\n")
        if "tags" in donnes:
            for cle, valeur in donnes["tags"].items():
                f.write(f"- **{cle}** : {valeur}\n")
        else:
            f.write("Aucun tag trouvé.\n")'''
# Version on balance toutes les donnes d'un coup
'''def node_to_md2(donnes:dict,fichier:str) -> None:
    with open(fichier, "w", encoding="utf-8") as f:

        if "tags" in donnes and "name" in donnes["tags"]:
            nom = donnes["tags"]["name"]
        for cle, valeur in donnes.items():
                f.write(f"- **{cle}** : {valeur}\n")'''


# Version qui separe tags et le reste
def node_to_md(donnes:dict,fichier:str) -> None:
    with open(fichier, "w", encoding="utf-8") as f:

        if "tags" in donnes and "name" in donnes["tags"]:
            nom = donnes["tags"]["name"]
    
        f.write(f"# {nom}\n\n")
        id = donnes.get('id')
        f.write(f'## [lien](https://www.openstreetmap.org/node/{id})\n\n')
        f.write("Voici les informations :\n\n")
       
        for cle, valeur in donnes.items():
                if cle == "tags":
                    break # Nous permet de s'arreter des qu'on tombe sur tags yess
                f.write(f"- **{cle}** : {valeur}\n")
        for cle, valeur in donnes["tags"].items():
                f.write(f"- **{cle}** : {valeur}\n")
            

def convert():
    with open('osm.md', 'r') as f:
        text = f.read()

    html = markdown.markdown(text)
    
    with open('osm.html', 'w') as f:
        f.write(html)


def fiche_osm(id:int):
    get_node(id) 
    node_to_md(get_node(id),"osm.md")
    convert()


