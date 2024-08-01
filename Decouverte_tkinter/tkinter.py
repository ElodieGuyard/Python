# coding: utf-8
 
from tkinter import Tk, Button, Label

fenetre = Tk() # On instancie notre fenêtre graphique

label = Label(fenetre, text="Hello World") # On injecte un premier label dans la fenêtre
label.pack()

# On définit un gestionnaire d'événements pour le bouton ci-dessous.
def do_something():
    print("Clicked")
    
# Puis, on injecte un bouton dans la fenêtre. Il est connecté à la
# fonction do_something qui déclenchera au clic sur le bouton.
button = Button(fenetre, text="Push me !", command=do_something)
button.pack()

# bouton de sortie
boutonExit=Button(fenetre, text="Fermer", command=fenetre.quit)
boutonExit.pack()

fenetre.mainloop()  # Permet d'amorcer la gestion des événements au sein de la fenêtre. 
