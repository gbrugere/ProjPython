# Estim'risque : à quels risques est soumise mon habitation
Projet mené dans le cadre de notre 2A à l'ENSAE.

<!-- TABLE DES MATIERES -->
<details>
  <summary>Table des Matières</summary>
  <ol>
    <li>
      <a href="#Idée-Principale">Idée principale</a>
    </li>
    <li><a href="#Utilisation">Utilisation</a></li>
    <ul>
        <li><a href="#Stats-Des">Statistiques Descriptives</a></li>
        <li><a href="#Modélisation">Modélisation</a></li>
      <li><a href="#Code-Principal">Code principal</a></li>
      <li><a href="#Données">Données</a></li>
     </ul>
    <li><a href="#Contact">Contact</a></li>
    <li><a href="#Bibliographie">Bibliographie</a></li>
  </ol>
</details>



<!-- IDEE PRINCIPALE -->
## Idée principale

Nous proposons une évaluation des risques naturels auxquels est soumis une habitation. L'utilisateur entre une adresse et reçoit un diagnostique complet des risques auxquels est soumise son habitation. Pour des raisons de taille des données nous nous avons limité notre travail aux départements des Bouches du **Rhône (13)**, de la **Haute Garonne (31)** et de la **Loire Atlantique (44)**. Ces trois departements sont, à notre sens représentatifs de l'ensemble des risques auxquels sont soumises les habitations en France. 


<!-- UTILISATION -->
## Utilisation

Notre projet se décompose en deux parties :  
    · Une partie dédiée aux statistiques descriptives  
    · Une partie contenant le code principal de notre projet  


### Statistiques Descriptives

Les notebooks suivant effectuent des statistiques descriptives. 
- ```INSEE.ipynb``` effectue des statistiques générales sur l'ensemble des risques auxquels est exposé la population française.
- ```Etude_Base_Argiles.ipynb``` présente des statistiques sur le risque de sécheresse et focalisés sur nos 3 départements d'étude (13, 31 et 44)
- ```Stats_Nucleaire.ipynb``` présente des statistiques sur le risque nucléaire pour l'ensemble du territoire français. 

## Modélisation 
Les attendus du projet comprennent une partie modélisation. Les modélisations que nous avons faites sont les suivantes : 
- Nous avons codé un modèle de forecasting de température de type SARIMA. Ce dernier est entrainé sur le base ```temperature_dep.csv``` entre 2010 et 2019, testé entre 2019 et mi 2022 et utilisé pour prédire les temperéture à l'horizon 2030. Le code de ce dernier se trouve dant le module ```temperature.py``` dont le notebook correspondant est ```Sarima_tempperature.ipynb```. 
- Pour améliorer l'experience utilisateur, nous avons aussi codé un suggesteur automatique de texte dans le cas où ce dernier ferait une faute d'ortographe mineure lorsqu'il rentre le nom de la ville ou de la rue. Ce dernier repose sur la minimisation de la distance de Levenstein. Le code se trouve dans le module ```levenstein.py```

### Code Principal

Le code principal se trouve dans ```main.ipynb``` le notebook demande en un premier lieu d'entrer une addresse puis calcule les différents risques immobiliers liés à cette addresse, et donne une note finale. Le code fait appelle à 6 modules que nous avons codé pour chaque risque. A chaque module est associé un notebook pour l'utilisateur (le correcteur typiquement...) qui souhaiterait les executer de manière indépendante 
- ```Nucleaire.py``` dont le notebook correspondant est ```Nucléraire.ipynb```
- ```Pollution.py``` dont le notebook correspondant est ```Polluant.ipynb```
- ```secheresse.py``` dont le notebook correspondant est ```get_secheresse.ipynb```
- ```glissement_terrrain.py``` dont le notebook correspondant est ```get_glissement_terrain.ipynb```
- ```inondation.py``` dont le notebook correspondant est ```get_risque_inondations.ipynb```
- ```temperature.py``` dont le notebook correspondant est ```Sarima_tempperature.ipynb```

### Données

Lors de ce projet, nous avons utilisé les données suivantes :
- ```mouvement_terrain_dep.csv``` fournit un historique (date de lieu) des mouvements de terrain par département. 
- ```temperature_dep.csv``` fournit un historique des temperature (série temporelle) à la maille journalière et sur une profondeur d'historique de 10 ans.
- ```Inondation``` (gpd file) fournit un zonage des risques d'inondation en france (classées sur une échelle de risque allant de 1 à 4)
- ```AleaRGdep_L93``` (gpd gile) fournit un zonage des retrait d'argiles en france, permet d'estimer la sécheresse des sols d'une région et donc de quaitifier les risques potentiels sur une habitation (fissure, écroulement...)
- ```centrales_nucleaires.csv``` fournit les coordonnées GPS de toutes les centrales nucléaires de la métropole
- ```CO.csv```, ```PM10.csv```, ```SO2.csv``` fournit un historique des niveau de pollution en monoxide de carbone, particules fines et dioxyde de souffre. 
- ```adresses-dep.csv``` resence toutes les adresses de la métropole et leur coordonnées GPS
- ```INSEE.ipynb``` resence l'ensemble des risques auxquels est soumis le territoire français. 

<!-- CONTACT -->
## Contact

Grégoire Brugère - gregoire.brugere@ensae.fr  
Corentin Pla - corentin.pla@ensae.fr   
Sophie Bataille - sophie.bataille@ensae.fr  






<!-- Bibliographie -->
## Bibliographie
ecrire la bibliographie, j'ai mis un exemple au hasard faut juste reproduire la forme

* [1] [Changement climatique et assurance : quelles conséquences sur la sinistralité à l’horizon 2050 ?](https://www.covea.eu/sites/default/files/2022-02/202202_Livre_Blanc_Covéa_Risques_Climatiques.pdf), Covéa, rapport publié en janvier 2022

* [2] [Changement climatique : quel impact sur l’immobilier ?](https://www.traace.co/post/real-estate-and-climate-change-what-impact), Traace, avril 2022

* [3] [Ensemble-face-aux-risques](https://ensemble-face-aux-risques.generali.fr), Generali (outil développé par l’organisme d’assurance Generali pour l’évaluation de l’exposition aux risques naturels des habitations)



