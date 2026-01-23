
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
    elements = donnees['elements'] # Récupère la liste des hôtels

    total_etoiles= 0
    total_handi = 0   

    dico_etoiles = {}                       
    dico_handi = {} 

    for hotel in elements:                  # On parcourt chaque hôtel un par un
        tags = hotel.get('tags', {})        # on recupere les tags sans faire planter si vide grace a .get 

        if 'stars' in tags:                 
            nb = tags['stars']              # lit le nombre d'étoiles
            if nb not in dico_etoiles:      # au cas ou la cle existe pas deja
                dico_etoiles[nb] = 0        # on cree la cle à 0
            dico_etoiles[nb] += 1           # on ajoute 1 au compteur
            total_etoiles += 1          

        if 'wheelchair' in tags:            
            acces = tags['wheelchair']     
            if acces not in dico_handi:  
                dico_handi[acces] = 0    
            dico_handi[acces] += 1
            total_handi += 1      

    
    resultat_etoiles = {}                   # nouveau dico pour stocker les % 
    for cle, valeur in dico_etoiles.items():
        pourcentage = int((valeur / total_etoiles) * 100)       # calcul Nombre / Total * 100
        resultat_etoiles[cle] = str(pourcentage) + "%"  # str comme on fait + on peut + des int et des str

    resultat_handicap = {}                  
    for cle, valeur in dico_handi.items():
        pourcentage = int((valeur / total_handi) * 100)       
        resultat_handicap[cle] = str(pourcentage) + "%" 

    return resultat_etoiles, resultat_handicap          # Renvoie les deux dico 

def dataset_to_md(dataset: dict, filename: str):
    with open(filename, "w", encoding="utf-8") as f:
      
        f.write("# HOTELS BARCELONAIS\n\n")

        f.write("### Informations Légales\n")
        f.write("Les données sont issues de [OpenStreetMap](https://www.openstreetmap.org).\n\n")

        stats_etoiles, stats_handi = compute_statistics2(dataset) 

        f.write("## Statistiques\n\n")
        
        f.write("### Pourcentage d'étoiles\n")
        for cle, valeur in stats_etoiles.items():
            f.write(f"- **{cle}** : {valeur}\n")

        f.write("\n### Pourcentage Handicap\n")
        for cle, valeur in stats_handi.items():
            f.write(f"- **{cle}** : {valeur}\n")

        f.write("\n## Liste complète\n\n")

        elements = dataset['elements']
        for element in elements:
            tags = element.get('tags', {})
            nom = tags.get('name', "Inconnu")
            
            f.write(f"### {nom}\n\n")

            id = element.get('id')
            type = element.get('type')
            f.write(f"[Voir sur la carte](https://www.openstreetmap.org/{type}/{id})\n\n")

            for cle, valeur in tags.items(): 
                f.write(f"- **{cle}** : {valeur}\n")
            
            f.write("\n")

def convert(fichier1,fichier2):
    with open(fichier1, 'r') as f:
        text = f.read()

    html = markdown.markdown(text)
    
    with open(fichier2, 'w') as f:
        f.write(html)

def info_locales(donnes):
    compute_statistics2(donnes)
    dataset_to_md(donnes,'info_locales.md')
    convert('info_locales.md', 'info_locales.html')



if __name__ == "__main__":
    query = """
    [out:json][timeout:90];
    area["wikipedia"="ca:Barcelona"]->.searchArea;
    nwr["tourism"="hotel"](area.searchArea);
    out center;
    """

    donnees = get_dataset2(query)
    
    if donnees:
        info_locales(donnees)

