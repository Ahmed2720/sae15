
import markdown
import requests
import json

def get_dataset2(requete):
    url = "https://overpass-api.de/api/interpreter"
    
    reponse = requests.get(url, params={'data': requete}, timeout=90)
    
    if reponse.status_code == 200:
        data = reponse.json()
        print(len(data['elements']))
        return data
    else:
        print("Erreur API : " + str(reponse.status_code))
        return None # quand ya l'erreur api
    

def compute_statistics2(donnees):
    elements = donnees['elements']          # Récupère la liste des hôtels
    total = len(elements)                   # Le total est la taille de la liste pour la division plus tard 
    dico_etoiles = {}                       
    dico_handicap = {}                     

    for hotel in elements:                  # On parcourt chaque hôtel un par un
        tags = hotel.get('tags', {})        # on recupere les tags sans faire planter si vide grace a .get 

        if 'stars' in tags:                 
            nb = tags['stars']              # lit le nombre d'étoiles
            if nb not in dico_etoiles:      # au cas ou la cle existe pas deja
                dico_etoiles[nb] = 0        # on cree la cle à 0
            dico_etoiles[nb] += 1           # on ajoute 1 au compteur

        if 'wheelchair' in tags:            
            acces = tags['wheelchair']     
            if acces not in dico_handicap:  
                dico_handicap[acces] = 0    
            dico_handicap[acces] += 1       

    resultat_etoiles = {}                   # nouveau dico pour stocker les % 
    for cle, valeur in dico_etoiles.items():
        pourcentage = int((valeur / total) * 100)       # calcul Nombre / Total * 100
        resultat_etoiles[cle] = str(pourcentage) + "%"  # str comme on fait + on peut + des int et des str

    resultat_handicap = {}                  
    for cle, valeur in dico_handicap.items():
        pourcentage = int((valeur / total) * 100)       
        resultat_handicap[cle] = str(pourcentage) + "%" 

    return resultat_etoiles, resultat_handicap          # Renvoie les deux dico 

def dataset_to_md(dataset: dict, filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# donnees\n\n")

        stats_etoiles, stats_handi = compute_statistics2(dataset) #On recupere les stat via comput stat

        f.write("## Statistiques\n\n")
        f.write("### pourcentage d'étoiles\n")
        for cle, valeur in stats_etoiles.items():
            f.write(f"- **{cle}** : {valeur}\n")

        f.write("\n### Pourcentage Handicap\n")
        for cle, valeur in stats_handi.items():
            f.write(f"- **{cle}** : {valeur}\n")

        f.write("\n## liste complete\n\n")

        elements = dataset['elements']
        for element in elements:
            tags = element.get('tags', {})
            nom = tags.get('name', "Inconnu")
            
            f.write(f"### {nom}\n\n")

            for cle, valeur in tags.items(): # # On affiche tous les tags de l'hôtel
                f.write(f"- **{cle}** : {valeur}\n")
            
            f.write("\n")


def convert(fichier1,fichier2):
    with open('info_locales.md', 'r') as f:
        text = f.read()

    html = markdown.markdown(text)
    
    with open('info_locales.html', 'w') as f:
        f.write(html)

def info_locales(data):
    compute_statistics2(get_dataset2(query))
    dataset_to_md(data,'info_locales.md')
    convert('info_locales.md','info_locales.html')




query = """
[out:json][timeout:90];
area["wikipedia"="ca:Barcelona"]->.searchArea;
// C'est ICI que la magie opère :
nwr["tourism"="hotel"]["stars"~"3|4|5"](area.searchArea);
out center;
"""




