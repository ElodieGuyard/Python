from tkinter import Tk, Entry, Button, Label, StringVar
from tkinter.messagebox import showinfo

#Init fenêtre tkinter
window = Tk() # On instancie notre fenêtre graphique
window.title("Etape 1_Guess_a_Number") #Définit le titre de la fenêtre


## **Étape 1**
# Créer une fonction qui demande un nombre à l’utilisateur à l’aide d’un input. 
# Stocker sa réponse dans une variable de type adéquat nommée `givenNumber`.

def setupTextVarEntree():
      numberVar = StringVar() #Construit une variable STRING adaptée pour tkinter
      numberVar.set("texte par défaut")
      return numberVar

def getInput():
    showinfo("Alerte", entree.get()) #Fenêtre qui pop ayant pour titre "alert" et ayant pour contenu la valeur de retour de Entry() : le texte écrit par l'user

# Composition de la fenêtre
entree = Entry(window, textvariable=setupTextVarEntree)
entree.pack() # On injecte l'entrée dans la fenêtre.
bouton = Button(window, text="Valider", command=getInput)
bouton.pack() # On injecte le bouton dans la fenêtre. 

window.mainloop()