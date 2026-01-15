def ex2():
    url = "https://overpass-api.de/api/interpreter"
    
    # La requête de l'exercice 2 (carré de coordonnées)
    requete = """
    [out:json][timeout:90];
    node ["name"] (49.14745,-0.35641,49.15107,-0.34930);
    out geom;
    """
    
    # On envoie la requête
    reponse = requests.get(url, params={'data': requete})

    if reponse.status_code == 200:
        data = reponse.json()
        nb_elements = len(data['elements'])
        print(f"Succès ! L'API a renvoyé {nb_elements} élément(s).")
    else:
        print(f"Erreur : {reponse.status_code}")

if __name__ == "__main__":
    ex2()