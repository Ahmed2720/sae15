import markdown
import requests
import math
from PIL import Image, ImageDraw

def get_node(id:int) -> dict:
    url = f"https://api.openstreetmap.org/api/0.6/node/{id}.json"
    reponse = requests.get(url)
    donnes = reponse.json()
    return donnes['elements'][0] # on renvoi le dico
    
# Version qui separe tags et le reste
def node_to_md(donnes:dict,fichier:str) -> None:
    with open(fichier, "w", encoding="utf-8") as f:

        nom = "pas de nom"
        if "tags" in donnes and "name" in donnes["tags"]:
            nom = donnes["tags"]["name"]
    
        f.write(f"# {nom}\n\n")

        f.write("### Carte\n\n")
        f.write("![Carte](carte_marqueur.png)\n\n")

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


def deg2num(lat_deg, lon_deg, zoom):
    """Formule mathématique pour trouver les coordonnées de la tuile."""
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return xtile, ytile

def generate_map(lat, lon):
    zoom = 16
    x, y = deg2num(lat, lon, zoom)
    
    url = f"https://tile.openstreetmap.org/{zoom}/{x}/{y}.png"
    reponse = requests.get(url)
    
    with open("carte_temp.png", "wb") as f:
        f.write(reponse.content)

    img = Image.open("carte.png")
    d = ImageDraw.Draw(img)
    d.ellipse([123, 123, 133, 133], fill='red')
    img.save("carte_marqueur.png")

def fiche_osm(id:int):
    donnes = get_node(id)
    lat = donnes['lat']
    lon = donnes['lon']
    generate_map(lat, lon)
    node_to_md(donnes,"osm.md")
    convert()

if __name__ == "__main__":

    id_test = 192067263
    fiche_osm(id_test)