# Dans ton fichier info_locales.py ou dans ton terminal
query = """
[out:json][timeout:90];
area["wikipedia"="ca:Barcelona"]->.searchArea;
// C'est ICI que la magie opère :
nwr["tourism"="hotel"]["stars"~"3|4|5"](area.searchArea);
out center;
"""


query ="""
[out:json][timeout:90];
area["name"="Caen"]->.searchArea;
nwr["tourism"="hotel"]["stars"~"3|4|5"](area.searchArea);
out center;
"""