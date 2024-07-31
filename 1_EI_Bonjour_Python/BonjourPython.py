
message = "Bonjour" #Crée une variable message dans lequel on va stocker le message : Bonjour !

firstName = "Beyonce" #Crée une seconde variable firstname dans lequel on va stocker un prénom. Exemple : Beyonce
#print(message) #Affiche dans la console le contenu de la viariable message

#Utilise la variable firstname dans message pour obtenir l’affichage du message : Bonjour Beyonce ! 
#Attention, ici il s’agit bien de modifier la variable message et non le console.log()

message = message + " " + firstName
#print(message)

def sayHello(): # déclaration d'une nouvelle fonction
      message = "Bonsoir"
      message = message + " " + firstName
      print (message) #EXPECTED OUTPUT = "Bonsoir Beyonce"

#sayHello() #Appel de la fonction sayHello

def sayHello2(prenom): # déclaration d'une fonction qui prend un paramètre
      message = "Bonjour"
      message = message + " " + prenom + " !"
      print (message) #EXPECTED OUTPUT = "Bonjour Elodie !"

#sayHello2("Elodie") 

def sayHello3(first_name, hour): # déclaration d'une fonction qui prend un paramètre
      if hour>=18:
            message = "Bonsoir"
      elif hour<18: #l'utilisation de else: correspond mieux puisqu'on a qu'une seule vérification à faire (avant ou après 18h)
                    #Note à moi même ELIF correspond à else if
            message = "Bonjour"
            
      message = message + " " + first_name + " !"
      print (message)

sayHello3("Elodie", 17) #EXPECTED OUTPUT = Bonjour Elodie !
sayHello3("Elodie", 18) #EXPECTED OUTPUT = Bonsoir Elodie !
sayHello3("Elodie", 19) #EXPECTED OUTPUT = Bonsoir Elodie !