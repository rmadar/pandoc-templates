---
title: "Rapport d'activité -- Romain Madar"
subtitle: "Décembre 2015 — Juin 2018"
...

# Curriculum vitæ

 - *État civil:* MADAR Romain
 - *email:* [romain.madar@cern.ch](mailto:romain.madar@cern.ch)
 - *web:* [romain-madar.com](http://romain-madar.com) -- [twitter](https://twitter.com/RomainMadar) -- [linkedin](https://fr.linkedin.com/in/romainmadar/en) -- [github](https://github.com/rmadar)
 
## Parcours scientifique

+ **Chargé de Recherche - ATLAS, CNRS** (2014-auj)
    + Recherche de phénomènes nouveaux dans l'état final $t\bar{t}t\bar{t}$ 
    + R&D/production d'électronique de lecture pour le calorimètre hadronique du HL-LHC

+ **Chercheur associé - ATLAS, Université de Fribourg en Brisgau** (2011-2014)
    + Mise en évidence du couplage de Yukawa entre le boson de Higgs et le lepton $\tau$
    + Amélioration de la simulation rapide du calorimètre
    
+ **Doctorant - DO, CEA Saclay** (2008-2011 )
    + Recherche du boson du Higgs dans des collisions produisant un muon et un lepton $\tau$
    + Amélioration de l’identification des leptons $\tau$
    
## Responsabilités

+ **Physique et analyse**
    + co-coordinateur de la recherche de production standard de $t\bar{t}t\bar{t}$ (2018-auj)
    + éditeur de la documentation in interne de la combination $t\bar{t}t\bar{t}$ ($36\text{fb}^{-1}$) (2018)
    + membre d'un comité éditorial interne d'ATLAS (2018-auj)
    + co-coordinateur de recherche BSM avec 2 leptons de même signe (2014-2018)
    + co-coordinateur de la recherche/évidence de $H\to\tau\tau$ (2011-2014)

+ **Développement de détecteur**
    + co-coordinateur de simulation/performence du calorimètre phase-II (2018-auj)
    + co-responsable de la production des 11000 cartes d'électronique de lecture (2018-auj))
    + coordinateur de la R&D d'un ASIC pour l'électronique de lecture frontale  (2016-2018)

+ **Opération de détecteur**
    + permanences de qualité de données dans ATLAS (2016-auj)
    + permanences d'acquisition de données dans DO (2009)
    
## Fincancements

+ **CAPES/COFECUB program** (2018-2022)
    + projet sur la calorimétrie hadronique et électromagnétique
    + projet sur 4 ans entre la France et le Brézil
    + en partenariat avec le LPNHE

+ **Projet Nouveau Chercheur**  (2015-2017)
    + projet de recherche de matère noire couplée au quark top
    + financement régionale (avant la fusion des régions)
    + deux ans de CDD chercheur

## Formation et diplômes

+ **Doctorat** dirigé par M. Besan\c{c}on et F. Couderc (2008-2011)
+ **Master2** NPAC, Paris XI (2007-2008)
+ **Agrégation de sciences physiques** ENS Cachan (2006-2007)


# Recherche scientifique

Mes travaux de recherche effctués entre décembre 2015 et juin 2018 s'articulent autour de deux axes principaux:  (1) l'analyse de données ainsi que les interpretations associées et (2) le développement de détecteur avec un volet *R&D* et un volet *production*. Les activités de ces deux axes sont décrites ci-dessous, puis une liste détaillée des publications ainsi que des intervention en conférence est donnée.

## Analyse de données et interpretations associées

Lors de mon arrivé au LPC en octobre 2014, j'ai repris l'activité d'analyse de recherche de nouveaux phénomènes dans les collisions produisant au moins une paire de lepton de même charge électrique en association avec des jets provenant de quarks beaux. L'étude de cet état final est motivée par le vaste spectre de modèles au dela du modèle standard (SM) qui conduisent à une telle signature (quark top et/ou boson de Higgs composite, dimensions supplémentaires, boson de Higgs additionel, etc...). Par ailleurs, le potentiel de découverte de la production standard de quatre quark top $t\bar{t}t\bar{t}$ - encore jamais observée à ce jour - est le plus important dans ce cannal. Étudier ce processus est particulièrement intéressant puisqu'il implique la production de la particule la plus lourde avec la plus haute multiplicité, et donc ouvre une fenêtre sur de nouveaux phénomènes à haute énergie.


### Recherche de phénomènes nouveaux {#BSM}

Mon implication dans cette analyse a été multiple. J'ai co-coordonée l'analyse dès le début du Run 2 ainsi que contribué à diverses tâches  telles que l'estimation des fonds, l'obtention de distributions de contrôle, l'analysis statistique ou encore l'édition des notes et papiers. Un premier résultat préliminaire basé sur les données enregistrées en 2015 est sorti en 2016 [@ATLAS-CONF-2016-032] et un papier est soumis au journal *JHEP* [@EXOT-2016-16].

J'ai également porté l'interpretation de ces résultats dans un modèle dans matière noire couplé au quark top, analyse complémentaire à la recherche $t+E^{\text{miss}}_T$. Ce résultat sera publié dans un papier résumant toutes les recherches de matière noire d'ATLAS. Ce projet, initié avec des théoriciens de l'IPNL, avait commencé avec un stage de M2 (Théo Megy, actuellement en thèse à Fribourg en Brisgau) avec une contribution au *LHC Dark Matter Report* [@LHCDMreport], et a été continué grâce au projet region *Nouveau Chercheur*.

Enfin, la sensibilité a la production stantard $t\bar{t}t\bar{t}$ de cette analyse a été combinée avec l'analyse de l'état final $\ell+$jets et $\ell^{\pm}\ell^{\mp}$ pour atteindre un sensibilté attendue de 2 fois la prediction du MS. Cette combinaison sera publiée dans le papier de l'analyse $\ell+$jets/$\ell^{\pm}\ell^{\mp}$, qui devrait être soumis d'ici la fin de l'été.

### Focus sur la production standard $\boldsymbol{t\bar{t}t\bar{t}}$ avec toutes les données Run 2

Depuis le début de l'année 2018, un nouveau groupe d'analyse est formé visant spécifiquement la première mise en évidence de la production standard $t\bar{t}t\bar{t}$, qui devrait être possible avec l'ensemble des données du Run 2. Ce nouveau projet d'analyse, dont je suis le co-coordinateur, regroupe tous les cannaux pertinents et sera fortement optimisé pour observer ce processus (au contraire de l'analyse dite *exotique* mentionée à la [Recherche de phénomènes nouveaux] qui visait un grande variété de signatures BSM).


## Développement de détecteur

Le profile du poste CR2 sur lequel j'ai été embauché avait une composante détecteur importante, et relativement nouvelle pour moi. J'ai commencé cette activité en m'impliquant sur une R&D en court, à savoir un ASIC (appelé *FATALIC*) pour l'électronique de lecture frontale du calorimètre hadronique d'ATLAS pour la phase haute luminosité du LHC (HL-LHC). Cette R&D n'a pas été sélectionnée et s'est achevée en juillet de 2017. La nature du projet instrumental a alors évolué vers une phase de production de 11000 cartes d'électronique décrite dans le TDR [@TDR], dont je suis auteur.

### La R&D de FATALIC

Après mon arrivée au LPC, je suis assez vite devenu le coordinateur du projet du à un changement de fonction du chercheur en charge du projet. Le prototype disponible à ce moment là était la version 4, qui avait déjà quelques problemes.

+ **simulation d'un ADC** pour tenter de comprendre un comportement inattendu
    + information utilisée pour la fonderie du prototype 4b

+ **mesures sur l'ASIC** (linéarité, bruit)
    + toutes premières mesures sur un banc test local (sans reconstruction du signal)
    + à permis d'identifier un certain nombres de points forts et faibles pour la version 5
    + plus gros problème: la précision de la voix de mesure dédié à l'étalonnage (origine comprise après simulation)
    
+ **reconstruction de l'énergie**
    + rien n'existait sur ce sujet à mon arrivée
    + le signal de sortie de l'ASIC est assez complexe (changement de gain dynamique échantillon par échantillon)
    + une étude dédiée était absoluement nécessaire
	    1. preuve de principe de filtrage optimal avec l'impulsion de FATALIC
	    2. simulation de la structure du signal de sortie de FATALIC et adaptation de la methode
	    3. implementation de FATALIC et sa reconstruction dans *ATHENA* (travail très technique)

+ **test en faisceau et analyses correspondantes**
    + 5 tests en faisceaux, dont seulement les 2 derniers ont été un succès
    + mesure des pulses anlogiques (important pour la reconstruction de signal)
    + mise en place d'un code de reconstruction des données de test faisceau (repris/finalisé par Stelios A. - CDD)
    + beaucoup d'effort et de temps pour l'intégration du système
    
+ **itérations avec les ingénieurs** 
    + comprendre les instabilités des premiers tests faisceaux
    + problèmes de firmware et d'adaptation d'impédance

+ **nouvelle fonderie FATALIC5** et cartes associées
    + corréler les mesures des prototypes précédents avec les simulations
    + travail de clarification des spécifications pour la physique
    + décider des compromis à faire en terme de performance
    + deux améliorations simultanée: voix lente (critique & difficile) et meilleure linéarité 
    + facteur de risque important, mais echéance imposée par le calendrier
    
+ **mesures finales et decisions de la collaboration**
    + test de la voix lente: précision meilleur d'un facteur 10 mais il manque toujours un facteur 5
    + erreur dans la simulation pre-FATALIC5: apres correction les nouvelles mesures sont comprises
    + plusieurs approches de filtrages ont ete testé et un facteur
    + test faisceau final avec performances conforme aux attentes (signal de physique OK, calibration: mauvaise précisions)

+ **documentation**
    + 2 notes internes (revues) pour la reconstruction de signal
    + 1 note interne (revue) pour l'implémentation dans *Athena* et l'impact du pile-up
    + 1 note interne (revue) pour l'analyse des tests faisceaux (pions, electrons, muons, réponse du calorimètre)
    + 1 publication à venir combinant l'ensemble de ces résultats, plus le design micro-élecronique de l'ASIC
    

### La préparation de la production

La phase de production des cartes *3in1* se prépare pour un livraison prévue fin 2022. Durant la première moitié de 2018, nous avons importé la carte de Chicago (schéma et structure des PCB) afin de pouvoir faire une première production locale. Quelques modifications mineurs ont été apportées au design et une production de 50 cartes a été finalisé en Juillet afin de pouvoir être testé en faisceau en Novembre. Les tests en laboratoires de ces 50 cartes sont en cours.

## Publications et intervention en conférence

**Revues à comité de lecture**

   + SSbjets exotics (submitted)
   + Combination 4top (to be submitted)
   + FATALIC proceedings (submitted)
   + Performance of a remote High Voltage power supply for the Phase II upgrade of the ATLAS Tile Calorimeter
   
**Notes publiques ATLAS**

  + SSbjets
  + TDR
  
**Notes internes ATLAS**

  + Signal reco
  + Simulation FATALIC
  + FATALIC in Athena and pile-up
  + Test beam analysis FATALIC5

   
**Conférences invitées dans des congrès**

  + LIO conference
  

**Communications à des congrès symposium**
  
  + SUSY2018
  + Pisa Meeting
 
 
 
# Enseignement, formation et diffusion de la culture scientifique

## Formation

+ Emergy
+ William
+ Stelios
+ Sergey
+ Lennart

## Diffusion de la culture scientifique

Conférences vulgarisées sur le boson de Higgs:

  - ENS Cachan (licence/master)
  - Lycée Chateaubriand de Rennes (classes préparatoires)

# Transfert technologique, relations industrielles et valorisation

Néant

# Encadrement, animation et management de la recherche

**Niveau LPC**

+ organisation des séminaires


**Niveau ATLAS-LPC**

+ responsable de l'activité upgrade jusqu'en Juin 2018, co-responsable depuis.
+ responsable de l'activité $t\bar{t}t\bar{t}$


**Niveau ATLAS**

+ co-responsable du groupe simulation et performence du calorimètre hadronique pour la phase-II
+ membre du comité de pilotage du calorimètre hadronique pour la phase-II
+ co-responsable de l'analyse $t\bar{t}t\bar{t}$ SM
+ membre d'un comité éditorial interne d'ATLAS


# Références

