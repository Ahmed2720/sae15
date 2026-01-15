def ex2():
    url = "https://overpass-api.de/api/interpreter"
    
    requete = """
    [out:json][timeout:90];
    node ["name"] (49.14745,-0.35641,49.15107,-0.34930);
    out geom;
    """
    reponse = requests.get(url, params={'data': requete})

    if reponse.status_code == 200:
        data = reponse.json()
        nb_elements = len(data['elements'])
        print(f"Succès ! L'API a renvoyé {nb_elements} élément(s).")
    else:
        print(f"Erreur : {reponse.status_code}")
