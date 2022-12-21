# Impact du réchauffement climatique sur les prix de l'immobilier
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
      <li><a href="#Code-Principal">Code principal</a></li>
     </ul>
    <li><a href="#Contact">Contact</a></li>
    <li><a href="#Bibliographie">Bibliographie</a></li>
  </ol>
</details>



<!-- IDEE PRINCIPALE -->
## Idée principale


Les organismes d’assurance réfléchissent depuis plusieurs années à la manière dont il faut intégrer les risques liés au changement climatique dans leurs contrats. Un grand nombre d’entre eux ont récemment publié de nouvelles études et développé de nouveaux outils pour ne pas prendre de retard sur la situation qui évolue très vite. En effet, le consensus scientifique est clair et les dérèglements climatiques sont d’ores et déjà une réalité. En ce qui concerne l’intégration de la problématique par les organismes d’assurance, l’enjeu en leurs conséquences potentielles. D’autant plus que les disparités sont fortes sur le territoire français. Plus les risques auxquels est exposé une habitation sont élevés, plus la prime d’assurance (habitation) sera élevée. Il est donc important de bien les cartographier, à la fois pour l’assureur qui doit être solvable mais aussi pour les particuliers qui doivent être informés et qui pourraient être amené à considérer ces risques dans leur choix de mobilité.


À la suite de nos lectures de quelques rapports d’assureurs sur la question ([1] [2]), nous avons décidé d’orienter notre projet autour de la cartographie des risques naturels en France métropolitaine. Nous nous somme inspirés d’un outil récemment développé par l’assureur Italien Generali ([3]) qui dresse une évaluation simple du degré d’exposition aux risques d’une habitation.


L’objectif de notre travail est donc de proposer une évaluation des risques naturels auxquels est soumis une habitation. Pour des raisons de taille des données nous nous avons limité notre travail aux départements des Bouches du Rhône (13), de la Haute Garonne (31) et de la Loire Atlantique (44). Ces trois departements sont, à notre sens représentatifs de l'ensemble des risques auxquels sont soumises les habitations en France. 


<!-- UTILISATION -->
## Utilisation

Notre projet se décompose en deux parties :  
    · Une partie dédiée aux statistiques descriptives  
    · Une partie contenant le code principal de notre projet  


### Statistiques Descriptives

Les notebooks ```INSEE.ipynb```, ```Etude_Base_Argiles.ipynb``` et ```Stats_Nucleaire.ipynb``` effectuent des statistiques descriptives. 

### Code Principal

Le code principal se trouve dans ```main.ipynb``` le notebook demande en un premier lieu d'entrer une addresse puis calcule les différents risques immobiliers liés à cette addresse, et donne une note finale. Le code fait appelle à 6 modules externes consacrés à chaque thématiques abordés (Nucléaire, Température, ...), les codes de ces modules sont détaillés dans leurs notebooks respectifs.  
Additionelement le module ```levenstein.py``` permet de trouver plus facilement l'addresse entré.



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



