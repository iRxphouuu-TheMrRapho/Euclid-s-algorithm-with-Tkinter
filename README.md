# Algorithme d'Euclide avec Tkinter

Ce projet est un Algorithme d'Euclide avec FLask créé par iRxphouuu sur demande en cours de maths expertes, cours d'option de spé maths en terminale. 

Ce projet permet de calculer le PGCD de deux nombres et de montrer la liste de tous les diviseurs communs des deux nombres à l'aide d'une interface graphique de Tkinter

## Répartition des Taches

Interface graphique : iRxphouuu
Code Liste des diviseurs : iRxphouuu
Code PGCD : iRxphouuu

## Etapes de Réalisations

En premier temps : réalisation de la partie calculatoire avec le PGCD et les divisuers.
Réalisation en second temps de l'interface graphique avec la librairie Tkinter.
Finalement liaison de l'interface avec la partie calculatoire.

## Fonctionnement de l'interface graphique

``` Nombre a ``` : Permet d'entrer la valeur du nombre a
``` Nombre b ``` : Permet d'entrer la valeur du nombre b
``` Calculer ``` : Calcule le PGCD et la liste des diviseurs communs
``` Petite barre horizonatale en haut à droite ``` : Diminue la fenêtre
``` Carré en haut à droite ``` Met la fenêtre en grand
``` Croix en haut à droit ``` Ferme totalement la fenêtre et quitte le logiciel

## Fonctions notables

dans le fichier ```main.py``` il y a toutes les fonctions pour le PGCD, les diviseurs et l'interface TKinter

``` pgcd ``` : calcul du PGCD
``` diviseurs``` : calcul de la liste des diviseurs
``` calculer_diviseurs ``` : récupération des valeurs entrer par l'utilisateur, calcul du PGCD via l'algorithme d'Euclide et calcul de la liste de tous les diviseurs et intersiection de la liste des diviseurs afin de ne garder que les diviseurs communs

Le reste des fonctions sont les fonctions TKinter permettant de créer l'interface graphique comprenant l'affichage des résultats dans les labels ``` entre les lignes 30 et 32 ```; la création de la fenêtre principale ``` entre les lignes 34 et 36 ```; la création des différents widgets ``` entre les lignes 38 et 45 ```; le placement des widgets dans la fenêtre ``` entre les lignes 47 et 54 ``` et la lancement de la boucle principale de la fenêtre ``` à la ligne 57 ```.

## Installation
Le projet requière Python en version 3.10.2
Le projet requiere les différentes librairies suivantes : 
```
Tkinter
```
Après avoir executé le fichier nommé ``main.py``, suivez les instructions et cliquer sur le lien affiché sur la console.

## Autres précisions 
Vous pouvez utilisez ce projet librement

