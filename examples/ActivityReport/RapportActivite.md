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

+ **Doctorat** dirigé par M. Besancon et F. Couderc (2008-2011)
+ **Master2** NPAC, Paris XI (2007-2008)
+ **Agrégation de sciences physiques** ENS Cachan (2006-2007)


# Recherche scientifique

Mes travaux de recherche effctués entre décembre 2015 et juin 2018 s'articulent autour de deux axes principaux:  (1) l'analyse de données ainsi que les interpretations associées et (2) le développement de détecteur avec un volet *R&D* et un volet *production*. Les activités de ces deux axes sont décrites ci-dessous, puis une liste détaillée des publications ainsi que des intervention en conférence est donnée.

## Analyse de données et interpretations associées

Lors de mon arrivé au LPC en octobre 2014, j'ai repris l'activité d'analyse de recherche de nouveaux phénomènes dans les collisions produisant au moins une paire de lepton de même charge électrique en association avec des jets provenant de quarks beaux. L'étude de cet état final est motivée par le vaste spectre de modèles au dela du modèle standard (SM) qui conduisent à une telle signature (quark top et/ou boson de Higgs composite, dimensions supplémentaires, boson de Higgs additionel, etc...). Par ailleurs, le potentiel de découverte de la production standard de quatre quark top $t\bar{t}t\bar{t}$ - encore jamais observée à ce jour - est le plus important dans ce cannal. Étudier ce processus est particulièrement intéressant puisqu'il implique la production de la particule la plus lourde avec la plus haute multiplicité, et donc ouvre une fenêtre sur de nouveaux phénomènes à haute énergie encore inexplorée.


### Recherche de phénomènes nouveaux {#BSM}

Mon implication dans cette analyse a été multiple. J'ai co-coordonée l'analyse dès le début du Run 2 ainsi que contribué à diverses tâches  telles que l'estimation des fonds, l'obtention de distributions de contrôle, l'analysis statistique ou encore l'édition des notes et papiers. Un premier résultat préliminaire basé sur les données enregistrées en 2015 est sorti en 2016 [@ATLAS-CONF-2016-032] et un papier est soumis au journal *JHEP* [@EXOT-2016-16].

J'ai également porté l'interpretation de ces résultats dans un modèle dans matière noire couplé au quark top, analyse complémentaire à la recherche $t+E^{\text{miss}}_T$. Ce résultat sera publié dans un papier résumant toutes les recherches de matière noire d'ATLAS. Ce projet, initié avec des théoriciens de l'IPNL, avait commencé avec un stage de M2 (Théo Megy, actuellement en thèse à Fribourg en Brisgau) avec une contribution au *LHC Dark Matter Report* [@LHCDMreport], et a été continué grâce au projet region *Nouveau Chercheur*.

Enfin, la sensibilité a la production stantard $t\bar{t}t\bar{t}$ de cette analyse a été combinée avec l'analyse de l'état final $\ell+$jets et $\ell^{\pm}\ell^{\mp}$ pour atteindre un sensibilté attendue de 2 fois la prediction du MS. Cette combinaison sera publiée dans le papier de l'analyse $\ell+$jets/$\ell^{\pm}\ell^{\mp}$, qui devrait être soumis d'ici la fin de l'été.

### Focus sur la production standard $\boldsymbol{t\bar{t}t\bar{t}}$ avec toutes les données Run 2

Depuis le début de l'année 2018, un nouveau groupe d'analyse est formé visant spécifiquement la première mise en évidence de la production standard $t\bar{t}t\bar{t}$, qui devrait être possible avec l'ensemble des données du Run 2. Ce nouveau projet d'analyse, dont je suis le co-coordinateur, regroupe tous les cannaux pertinents et sera fortement optimisé pour observer ce processus (au contraire de l'analyse dite *exotique* mentionée à la section [Recherche de phénomènes nouveaux] qui se focalisait sur un grande variété de signatures BSM).


## Développement de détecteur

Le profile du poste CR2 sur lequel j'ai été embauché avait une composante détecteur importante, et relativement nouvelle pour moi. J'ai commencé cette activité en m'impliquant sur une R&D en court, à savoir un ASIC (appelé *FATALIC*) dédié à la lecture des signaux du calorimètre hadronique d'ATLAS pour la phase haute luminosité du LHC (HL-LHC). Cette R&D n'a pas été sélectionnée parmis les trois options proposées et s'est donc achevée en juillet de 2017. La nature du projet instrumental a alors évolué vers une phase de production de 11000 cartes d'électronique décrite dans le TDR [@TDR], dont je suis naturellement auteur.

### Le projet FATALIC

Après mon arrivée au LPC en 2014, je suis assez vite devenu le coordinateur de ce projet commencé en 2008, du à un changement de fonction du chercheur en charge du projet. Le prototype disponible à ce moment là était la version 4. Un énorme travail a été fait sur 2016-2017 avec l'aide de post-doctorants (Stelios A., Sergey S.) et doctorants (William B., Emery N.), incluant cinq tests faisceaux, quatre notes internes, cinq conférences (posters et présentations) ainsi qu'une publication à venir fin 2018.


**Introduction au projet**\
Mes premières contributions à ce projet ont été d'effectuer les premières mesures de linéarité basées sur le signal analogique, ainsi que la réalisation d'une petite simulation d'un convertisseur analogique numérique incluant des imperfections. Ces deux points on permis de mieux identifier et palier les défauts de FATALIC4, dans le prototype suivant FATALIC4b.

**Reconstruction de l'énergie**\
Par la suite, j'ai débuté le développement de la reconstruction de l'amplitude du signal à partir des sept échantillons numériques (méthode d'*optimal filtering*). Cette activité était nouvelle pour moi ainsi que pour le groupe, et s'est étendue sur plusieurs deux ans avec la contribution de deux post-doctorants et deux doctorant. Nous avons réussi à appliquer la méthode à FATALIC dans une simulation (signal de sortie ayant une structure inhabituelle), puis dans les données collectées en test en faisceau. Enfin, le signal délivré par FATALIC a été implémenté dans *athena* (travail extrêmement technique), ce qui à permis de tester l'impact du *pile-up* sur la résolution en énergie au niveau de la cellule.

**Automatisation des mesures**\
Un autre point important de ce projet que j'ai développé, est d'avoir un code permettant de faire des mesures systématiques de bruit et de linéarité très rapidement. Ce code a ensuite été étendu pour inclure l'*optimal filtering* et pu être utilisé aussi bien en test faisceau que sur le banc test du laboratoire. Un certain nombre d'observation ont été obtenues dont les plus importantes sont la perte de linéarité pour des forte charge d'entrée, et surtout la très mauvaise précision du cannal de lecture dédié à l'étalonnage du détecteur. Ce dernier point, potentiellement rédibitoire, a nécessité un autre prototype *FATALIC5* dont j'ai coordonné le design et les tests.

**Test en faisceau et analyses correspondantes**\
Plusieurs tests en faisceaux ont été effectués au CERN. Un tournant du projet s'est produit lors d'un test de 2017 où des problèmes d'intégration bloquant ont été identifiés et résolus par la suite en laboratoire grâce à l'arrivé d'un ingénieur expert en firmeware, Alexandre Soulier. En juin 2017, le système était assez stable pour enregistrer des données de qualités et les premiers dépôts d'énergie reconstruits avec FATALIC ont été observés, ce qui a été la première démonstration que FATALIC4b fonctionnait très bien pour les signaux de physique.

**Dernier prototype FATALIC5**
L'élaboration de FATALIC5 a commencée fin 2016 avec l'objectif principale d'avoir une voix de lecture pour l'étalonnage bien plus précise que les ASIC précédent. Cette contrainte a nécessité de repenser assez profondément la structure de l'ASIC et de faire des compromis sur les performences d'autres fonctionalités. Ce travail a nécessité plusieurs itérations de simulations pour choisir le meilleur compromis, mais églament une clarification des contraintes imposées par la physique de ce détecteur. Sachant que la sélection finale de l'électronique frontale étaient prévue en Juillet 2017, lancer une fonderie en Février avec des modifications majeures représentait un gros facteur de risque mais également une nécessité.
    
**Mesures finales et decisions de la collaboration**
Les mesures effecutés en laboratoire sur FATALIC5 (juillet 2017) ont montré une précision amélioré d'un ordre de grandeur mais toujours d'un facteur 5 au dessus des spécifications, et des résultats de simulation pré-fonderie. Un des effets importants n'était en fait que partiellement pris en compte dans la simulation; une fois corrigée, la simulation étaient en accord avec les mesures. Quelques filtres évolués ont été testés (collaboration avec des collègues bréziliens) pour gagner le facteur 5 manquant. Même si les résultats étaient prometteurs, le temps à manquer pour finaliser cette approche. Par ailleurs, une des options concurrente à démontré une précision meilleure que les spécification par deux ordres de grandeur. Sachant que cette précision intervient aussi dans la mesure de la luminosité, il a été décidé de sélectionner cette option.

### La préparation de la production

La phase de production des cartes *3in1* se prépare pour un livraison prévue fin 2022. Durant la première moitié de 2018, nous avons importé la carte de Chicago (schéma et structure des PCB) afin de pouvoir faire une première production locale. Quelques modifications mineurs ont été apportées au design et une production de 50 cartes a été finalisé en Juillet afin de pouvoir être testé en faisceau en Novembre. Les tests en laboratoires de ces 50 cartes sont en cours.

## Publications et interventions en conférence


**Revues à comité de lecture**

   1. *Search for new phenomena in events with same-charge leptons and b-jets in pp collisions at 13 TeV with the ATLAS detector*, soumis à JHEP, [arXiv:1807.11883](https://arxiv.org/abs/1807.11883)

   1. *Search for four-top-quark production in the single-lepton and opposite-sign dilepton final states in pp collisions at 13 TeV with the ATLAS detector*, va être soumis à *PRD*, [arXiv:XXX.XXX](LinkToCome)

   1. *FATALIC: a fully integrated electronics readout for the ATLAS tile calorimeter at the HL-LHC*, soumis à *NIMA*, [ATL-TILECAL-PROC-2018-005](https://cds.cern.ch/record/2626873)

   1. *Performance of a remote High Voltage power supply for the Phase II upgrade of the ATLAS Tile Calorimeter*, [JINST **11** C02050](http://iopscience.iop.org/article/10.1088/1748-0221/11/02/C02050/meta;jsessionid=3B2348842E1C31A6212C04E3941F08F7.c2.iopscience.cld.iop.org)


   
**Notes publiques ATLAS**

  1. *Technical Design Report for the ATLAS Tile Calorimeter Phase-II Upgrade*, [CERN-LHCC-2017-019](https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/UPGRADE/CERN-LHCC-2017-019/)

  1. *Search for new physics using events with b-jets and a pair of same charge leptons in 3.2 fb-1 of pp collisions at 13 TeV with the ATLAS detector* [ATLAS-CONF-2016-032](https://cds.cern.ch/record/2161545)
 
  1. *Searches for new physics with lepton flavors and multi-lepton final states in ATLAS* [EPJ Web of Conf 126, 04028 (2016)](https://www.epj-conferences.org/articles/epjconf/abs/2016/21/epjconf_icnfp2016_04028/epjconf_icnfp2016_04028.html)

**Notes internes ATLAS**
  
  1. *Combined search for four-top quarks production with in 36 fb-1 of pp collisions* [ATL-COM-PHYS-2018-269](https://cds.cern.ch/record/2310185)

  1. *Constraint on a top-coupled dark matter model combining searches in $t+E^{\text{miss}}_T$ and $tt$ final state* [ATL-COM-PHYS-2017-1710](https://cds.cern.ch/record/2294626)

  1. *Performance of FATALIC v5* [ATL-TILECAL-INT-2018-003](https://cds.cern.ch/record/2621128) 

  1. *Simulation of FATALIC Frond-end Electronics in the ATLAS Tile Calorimeter Software* [ATL-TILECAL-INT-2018-004](https://cds.cern.ch/record/2624425)

  1. *Simulation of FATALIC for signal reconstruction* [ATL-TILECAL-INT-2018-002](https://cds.cern.ch/record/2310569)

  1. *Signal Reconstruction with FATALIC* [ATL-TILECAL-INT-2017-002](https://cds.cern.ch/record/2259452)

  1. *Search for new phenomena using events with b-jets and a pair of same charge leptons in 36.1 fb-1 of pp collisions* [ATL-COM-PHYS-2016-1474](https://cds.cern.ch/record/2224335)
  

**Conférences invitées dans des congrès**

  1. *Searches for new physics in the top quark sector with ATLAS detector*, session plénière (45min), [LIO conference](https://indico.in2p3.fr/event/12972/), [diapositives](https://indico.in2p3.fr/event/12972/contributions/12391/attachments/10530/13042/LIO2016_Madar.pdf)
  

**Communications à des congrès symposium**
  
  1. *Search for Vector-Like Quarks in ATLAS*, session parallèle (15min), [SUSY2018](https://susy2018.ifae.es/), [diapositives](https://indico.cern.ch/event/689399/contributions/3005459/attachments/1692679/2723751/SUSY2018_VLQ_Madar.pdf)

  1. *FATALIC: a fully integrated electronics readout for the ATLAS tile calorimeter at the HL-LHC*, poster, [PM2018](https://agenda.infn.it/conferenceDisplay.py?confId=13450), [poster](https://agenda.infn.it/getFile.py/access?contribId=63&sessionId=18&resId=0&materialId=poster&confId=13450)
 
 
 
# Enseignement, formation et diffusion scientifique


## Formation

**Encadrement de deux post-doctorants**

1. *Stylianos Angelidakis (50%)* 
   
   > finalisation de la reconstruction du signal pour FATALIC, analyse des données de test en faisceau, écriture de la publication finale sur FATALIC.

2. Sergey Senkin (100%)
   
   > Premières études de reconstruction de signal pour FATALIC, recherche de matière noire couplée au quark top dans des collisions produisant deux quark top de même charge électrique

**Encadrement de trois doctorants**
   
1. Lennart Rustigue (100%)
   
   > Évaluation des performences du calorimètre hadronique pour le HL-LHC, recherche et première évidence de la production standard de quatre quark tops.
   
2. Emery Nibigira (50%)
   
   > Implémentation de FATALIC dans la simulation d'ATLAS et impact du pile-up sur la résolution de l'énergie déposée dans une cellule.
   

3. William Barbe (50%)

   > Impact des imperfections d'électronique sur la résolution de l'énergie reconstruite par FATALIC.
   

**Encadrement d'un stagiaire de L3**


1. Mikaël Leroy (100%)

   > Étude de la topologie des collisions produisant quatre quark tops.
  
    

## Diffusion de la culture scientifique

Après l'écriture d'un livre illustré sur le boson de Higgs [@Badaud:2128589], couvrant les implications conceptuelles et la découverte experimentale, j'ai donnée une série de conférences sur le boson de Higgs vulgarisée pour un public de physicien non spécialiste de physique des particules:

  + UTINAM, laboratoire INSU à Besancon
  + ENS Cachan, magistère de physique fondamentale
  + Lycée Chateaubriand, classes préparatoires à Rennes
  + LPC (à venir)



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

