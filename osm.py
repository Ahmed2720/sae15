import markdown
import requests
import math
from PIL import Image, ImageDraw

def get_node(id:int) -> dict:
    url = f"https://api.openstreetmap.org/api/0.6/node/{id}.json"
    reponse = requests.get(url) # on recupere les info via une requete a l'aide de l'url
    donnes = reponse.json() # conversion de notre reponse en json dans une variable donnes
    return donnes['elements'][0] # on renvoi le dico
    
# Ecrit toutes les infos et l'image dans un fichier md
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
            
# convertit le md en html
def convert():
    with open('osm.md', 'r') as f:
        text = f.read()

    html = markdown.markdown(text)
    
    with open('osm.html', 'w') as f:
        f.write(html)

## fonction faite avec la doc wiki
def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return xtile, ytile

# Télécharge l'image de la carte et dessine un point rouge au milieu.
def generate_map(lat, lon):
    zoom = 16
    x, y = deg2num(lat, lon, zoom)
    url = f"https://tile.openstreetmap.org/{zoom}/{x}/{y}.png" # url de la tuile avec zoom et x,y pour zoom latitude longitude
    reponse = requests.get(url,headers={"User-Agent":"sae"}) # l'user agent sert a contourner l'acces blocked 
    
    with open("carte_temp.png", "wb") as f:
        f.write(reponse.content)

    img = Image.open("carte_temp.png") # ouverture de l'image
    img = img.convert("RGB") # donne acces a toute les couleur
    draw = ImageDraw.Draw(img) # outil pour dessiner sur l'image
    draw.ellipse([123, 123, 133, 133], fill='red') # dessine un rond rouge / la tuile fait 256 pixel le milieu est a 128 les coordonnes servent a centrer le rond
    img.save("carte_marqueur.png") # on enregistre la nouvelle image modifiée

# fonction finale
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