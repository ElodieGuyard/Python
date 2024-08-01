# Python

## EI 1_BonjourPython

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

## Découverte_tkinter

Tkinter est la bibliothèque graphique libre d'origine pour le langage Python, permettant la création d'interfaces graphiques. Executer `python -m tkinter` depuis une ligne de commande ouvre une fenêtre de démonstration d'une interface simple.

Utilisation de quelques instructions de base dans tkinter.py :
- ligne 3 : importation des modules `Tk, Button, Label` de la bibliothèque tkinter.
- ligne 5 : instanciation de la fenêtre graphique
- ligne 7 : injection d'un label contenant le texte "Hello World" dans la fenêtre
- ligne 11 : définition d'une fonction (gestionnaire d'événement) qui écrit dans la console "clicked"
- ligne 16 : Injection d'un bouton qui executera la fonciton ci-dessus lorsque l'on clique dessus
- ligne 20 : Injection d'un bouton qui executera la commande `.quit` : fermera la fenêtre quand on clique dessus.
- ligne 23 : Permet d'amorcer la gestion d'événement au sein de la fenêtre

## E2_Guess_a_Number

### Fichier Etape_1_Guess_a_Number.py
Consigne : Créer une fonction qui demande un nombre à l’utilisateur à l’aide d’un input. Stocker sa réponse dans une variable de type adéquat nommée `givenNumber`.

- Ligne 5/6 Instanciation de la fenêtre graphique et définition du titre
- Ligne 13 déclaration de la fonction `setupTextVarEntree` qui déclare la variable `numberVar` en tant que str, set le texte par défaut de l'input où la fonction va être appelée et retourn cette variable.
- Ligne 18 déclaration de la variable `getInput` qui génèrera une fenêtre popup avec la valeur de l'input `entree`
- Line 22 instanciation de l'input dans la fenêtre `window`, textvariable est définit par la fonction `setupTextVarEntree` ligne 13
- Ligne 24 : Instanciation du bouton "valider" qui, lors d'un clic, executera la fonction `getInput`

### Fichier Etape_2_Guess_a_Number.py

Clarification de l'entrée `entry` :
à partir de la ligne 39
Ressources utiles :
https://www.pythontutorial.net/tkinter/tkinter-validation/
https://pythonassets.com/posts/textbox-entry-validation-in-tk-tkinter/

Le premier argument validate dit à la textbox quel type de validation on veut : "key" = Valider chaque fois qu’une frappe modifie le contenu du widget.
Deuxieme argument de validation : on passe un tuple qui contient la fonction qui va prendre soin de valider le texte (validate_entry(),
qu'on doit d'abord inscrire dans le pool via window.register()) et ensuite une chaîne de caractère désignant quelle information on veut recevoir comme arguement dans cette fonction("%S" means the text entered by the user).

Definitions : "The pool distributes the tasks to the available processors using a FIFO scheduling register() methode allows to register class in the pool on demand. You need only pool instance and class."


