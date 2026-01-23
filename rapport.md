# Ahmed Abdelmounim, Maxence Yazdani
               ## SAE 105 : API


1. - Concernant le choix du sujet on a beaucoup hésite au debut on pensait a une comparaison des fast food au sein d'une ville puis comparer les station velolib de Caen mais en relisant le cahier des charges on a vu un exemple qui nous a plu les hotels a Barcelone en plus personellement je supporte le club de barcelone au foot ducoup ca ma parle hahaha.
    - Pour le choix des statistiques on a pense a recense les etoiles des hotels mais comme on a vu que c'etait assez leger comme info on a rajoute avec une stat qui etait souvent presente entant qu'attribut l'acces pour les fauteuil roulant.

2. - Concernant les difficultes tout d'abord ces choix de statistiques nous ont un peu fais galere car il n'y avait pas tous les hotels de barcelone qui ont des etoile donc dans la foction compute statitistqiue quand on venait additionner les ppourcentages ca faisait pas 100% et c'etait des % faibles. C'est a cause de ca que on a rajouter l'acces au personne handicape. Quand mr Brisacier est passe on avait change dans la requete un petit parametre en plus qui faisait que on recuperer que les hotels a minimus 3 etoiles dcp on divisait a la fin pour nos pourcentages par le len(elements) c'etait plus pratique: ["stars"~"3|4|5"]
Finalement il nous a aiguiller a faire 2 totaux qu'on incrementer a chaque fois pour nos divisons a la fin. Ce qui fait que on obtient tous nos pourcentage additioner qui donne environ 100%

- Autre detail qu'on a pas reussi a faire c'est trie nos pourcentages dans e fichier md pour  que ca soit moinns dans le desordre.



- Enfin la partie la plus complique ete celle des tuiles car encore maintenant notre tuile est pas vraiment sur l'hotel que l'on veut. C'est optionnel mais le marqueur tel que l'image du cahier des charges on a pas reussi.
Pour faire un minimum on a fait un petit marqueur rond grace a une doc pillow mais le rond aussi est pas du tout sur l'hotel.
