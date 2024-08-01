from tkinter import Tk, Entry, Button, Label, IntVar
from tkinter.messagebox import showinfo

#Init fenêtre tkinter
window = Tk() # On instancie notre fenêtre graphique
#window.geometry("150x150") #Définit la taille de la fenêtre
window.title("Jeu : Guess a Number") #Définit le titre de la fenêtre


## **Étape 2** : Consigne
# Pour le moment nous allons considérer que le nombre à deviner est 22.

#- Écrire une fonction qui prend en paramètre `givenNumber` et qui se nommera `didIWin`
#- Si le nombre est plus petit que 22, on affichera à l’utilisateur *“Plus grand”*.
#- Si le nombre est plus quand que 22 on affichera à l’utilisateur *“Plus petit”*.
#- Si le nombre est 22 on affichera *“Bravo ! Vous avez deviné le nombre”.*    
#L’ordre dans lequel vous ferez vos conditions est important, le but est d’exécuter le moins de code possible. Demandez-vous ce qu’il faut vérifier en premier.

def validate_entry(text): # fonction qui prend en paramètre du texte
    return text.isdecimal() # retourne true ou false si le texte est décimal ou non

def getNumber():
    inputNumber = int(entry.get())
    return inputNumber #return le contenu la valeur de retour de Entry() : le texte écrit par l'user

def DidIWin():
      Number = getNumber()
      if Number < 22 :
            showinfo("Alerte", "plus grand")
      elif Number > 22 :
            showinfo("Alerte", "plus petit")
      else :
            showinfo("Alerte", "Bravo ! Vous avez deviné le nombre")

#Construction de la fenêtre
label = Label(window, text="Ecrire ici le nombre que vous souhaitez soumettre") # On injecte un premier label dans la fenêtre
label.pack() # On injecte le label dans la fenêtre.

#Définition de l'entrée avec validation de l'input ( déciamal only )
numberVar = IntVar() #Construit une variable Int adaptée pour tkinter
entry = Entry( #input avec vérification que ce qui est écrit est bien des chiffres
    validate="key",
    validatecommand=(window.register(validate_entry), "%S"),
    textvariable = numberVar
)
entry.pack() # On injecte l'entrée dans la fenêtre.

bouton = Button(window, text="Valider", command=DidIWin)#Déclanche la vérification du nombre au click
bouton.pack() # On injecte le bouton dans la fenêtre. 

window.mainloop()