def get_dataset(requete):
    # L'adresse de l'API
    url = "https://overpass-api.de/api/interpreter"
    
    ma_requete ="""
    [out:json][timeout:90];
    area["wikipedia"="fr:Caen"]->.zone_de_recherche;
    (
      node["shop"="florist"](area.zone_de_recherche);
      nwr["shop"="supermarket"](area.zone_de_recherche);
    );
    out geom;
    """
    # On envoie la requete (avec 90s d'attente max pour eviter l'erreur 504)
    reponse = requests.get(url, params={'data': requete}, timeout=90)
    resultat = reponse.json()
    # Si c'est bon (200), on renvoie le JSON
    if reponse.status_code == 200:
        print(f"J'ai recupere {len(resultat['elements'])} elements.")
    else:
        print("Erreur API : " + str(reponse.status_code))
        return None


import requests
import json

def get_dataset2(requete):
    url = "https://overpass-api.de/api/interpreter"
    
    reponse = requests.get(url, params={'data': requete}, timeout=90)
    
    if reponse.status_code == 200:
        data = reponse.json()
        print(f" J'ai récupéré {len(data['elements'])} éléments.")
        return data
    else:
        print("Erreur API : " + str(reponse.status_code))
        return None
    


def compute_statistics(donnees):
    compteur_etoiles = {}
    compteur_handicap = {}

    elements = donnees['elements']

    liste_hotels = donnees['elements']
    for hotel in liste_hotels:
        if 'tags' in hotel:
            tags = hotel['tags']
        if 'stars' in tags:
            etoiles = tags['stars'] 
        if etoiles not in compteur_etoiles:
            compteur_etoiles[etoiles] = 0
            compteur_etoiles[etoiles] = compteur_etoiles[etoiles] + 1
        if 'wheelchair' in tags:
                acces = tags['wheelchair']
                if acces not in compteur_handicap:
                    compteur_handicap[acces] = 0
                compteur_handicap[acces] += 1
    total_etoiles = 0
    total_handi = 0
    for cle in compteur_etoiles:
        total_etoiles += compteur_etoiles[cle]
        compteur_etoiles[cle] = str(int(compteur_etoiles[cle] / total_handi * 100)) + "%"

    for cle in compteur_handicap:
        total_handi += compteur_handicap[cle]
        compteur_handicap[cle] = str(int(compteur_handicap[cle] / total_handi * 100)) + "%"


def compute_statistics2(donnees):
    elements = donnees['elements']
    
    dico_etoiles = {}
    total_etoiles = 0
    
    dico_handicap = {}
    total_handi = 0


    for hotel in elements:
        tags = hotel.get('tags', {})

        if 'stars' in tags:
            nb = tags['stars']
            if nb not in dico_etoiles:
                dico_etoiles[nb] = 0
            dico_etoiles[nb] += 1
            total_etoiles += 1

        if 'wheelchair' in tags:
            acces = tags['wheelchair']
            if acces not in dico_handicap:
                dico_handicap[acces] = 0
            dico_handicap[acces] += 1
            total_handi += 1

    for cle in dico_etoiles:
        valeur = dico_etoiles[cle]
        if total_etoiles > 0:
            pourcentage = int((valeur / total_etoiles) * 100)
            dico_etoiles[cle] = str(pourcentage) + "%"

    for cle in dico_handicap:
        valeur = dico_handicap[cle]
        if total_handi > 0:
            pourcentage = int((valeur / total_handi) * 100)
            dico_handicap[cle] = str(pourcentage) + "%"

    return dico_etoiles, dico_handicap