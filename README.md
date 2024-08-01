# Python

### EI 1_BonjourPython
Objectif : Affichier Bonjour/Bonsoir `Prénom` en fonction de l'heure qu'il est. Prompt l'utilisateur pour lui demander son prénom et l'heure qu'il est.
- Premier code : 
  - Utilisation de la fonction `print` pour afficher dans la console une chaine de caractère stockée dans une variable. (un prénom)
  - Concaténation de deux chaînes de caractères
- Dans une fonction :
  - Creer une fonction avec nos instructions du dessus, et appel de cette fonction.
- Ajout d'un paramètre :
  - Creation d'une fonction qui prend en paramètre une chaîne de caractère
  -> de cette façon `sayHello2("Elodie")` retournera dans la console `Bonjour Elodie !`
- Ajout d'un second paramètre :
  - Creation d'une fonction qui prend en paramètre une chaîne de caractère et un nombre pour que lorsque l'utilsateur indique une heure après 18h, la console print `bonsoir` au lieu de `bonjour` 
  -> De cette façon `sayHello3("Elodie", 17)` retournera `Bonjour Elodie !` dans la console et `sayHello3("Elodie", 20)` retournera `Bonsoir Elodie !`

### Découverte_tkinter

Tkinter est la bibliothèque graphique libre d'origine pour le langage Python, permettant la création d'interfaces graphiques. Executer `python -m tkinter` depuis une ligne de commande ouvre une fenêtre de démonstration d'une interface simple.

Utilisation de quelques instructions de base dans tkinter.py :
- ligne 3 : importation des modules `Tk, Button, Label` de la bibliothèque tkinter.
- ligne 5 : instanciation de la fenêtre graphique
- ligne 7 : injection d'un label contenant le texte "Hello World" dans la fenêtre
- ligne 11 : définition d'une fonction (gestionnaire d'événement) qui écrit dans la console "clicked"
- ligne 16 : Injection d'un bouton qui executera la fonciton ci-dessus lorsque l'on clique dessus
- ligne 20 : Injection d'un bouton qui executera la commande `.quit` : fermera la fenêtre quand on clique dessus.
- ligne 23 : Permet d'amorcer la gestion d'événement au sein de la fenêtre

