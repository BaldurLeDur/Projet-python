#salaire = int(input("quelle est votre salaire ? : "))
#fonction = int(input("pour fonction publique, tapez 1 et pour fonction privé tapez 2 : "))
#if fonction == 1:
 #   print("votre salaire net est de " , salaire - salaire * 0.15, " euro")
#else:
 #   print("votre salaire net est de " , salaire - salaire * 0.25, " euro")

#___________________________________________________________________________________________

#Définir une fonction qui retourne la division de x et y
#def divide(x,y):
    #Si y est égale à zero
    #if y == 0:
        #Alors ecrire " division par zéro impossible : y = 0"
    #   print("division par zéro impossible : y = 0")
    #Sinon : y est supérieur à 0
    #else:
        #diviser x par y
    #    print(x/y)

#importer le module temps
import time
import random
caracteres = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789"

#def input():
    #Renvoie un caractère de type string au hasard


#Créer une variable "jouer" qui demander si le joueur veut jouer "règles" (oui ou non)
#Si oui
    #Alors
    #tant que jouer est oui
        #Créer la variable caractères qui demande quelle caractère le joueur veut utiliser
        #Si le caractère de la fonction input est différent du caractère de la variable caractère
            #Alors : écrire "le caractère du robot", écrire le caractère de la fonction input, "est différent du tiens" écrire le caractère du joueur "tu as perdu"
            #Dormir 500 miliseconde
            #Ecrire la variable jouer qui dit "veut tu rejouer ?"

        #Sinon 
            #Alors : écrire "bravo vos caractère sont les mêmes tu as gagner"
            #Dormir 500 miliseconde
            #Ecrire la variable jouer qui dit "veut tu rejouer ?"
#Sinon
    #Alors ecrire "dis le si je te fais chier"

jouer = str(input("Veuxt tu joueur au DEVINE OU TU PERDS ? Le but est simple un robot choisie un carcatèrealéatoire, tu dois le deviner. Réponds oui si tu veux jouer et non si tu ne veux pas. : "))
if jouer == "oui":
    while jouer == "oui":
        charJoueur = str(input("Devine quelle caractère le robot vas choisir : "))
        h = caracteres[random.randint(0, len(caracteres)-1)]
        if charJoueur != h:
            print("Le caractère que le robot a choisi est : ",h, ", alors que le tiens est : ",charJoueur,". Tu as perdu")
            time.sleep(1.5)
            print("T'es une merde")
            time.sleep(1)
            jouer = str(input("Tu veux rejouer. Repond oui ou non ? : "))
        else:
            print("bien ouèj batard t'as trouvé")
            time.sleep(1)
            jouer = str(input("Tu veux rejouer. Repond oui ou non ? : "))
elif jouer == "non":
    print("bah dis le si je te fais chier")
else:
    print("azy écris bien aussi batard !")

#exercice 1
#faire une fonnction qui concatene 2 chaine de caractère, les séparent par une virgule

#exercie 2
#fire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere
#avec l'ensembles des occurence d'un chiffre e.g.:
#pour tableau = [0,1,1,1,0,1,1,0,1]
#la fonction(tableau, 0) doit renvoyez "0, 4, 7" n'hésitez pas a implanter la première fonction

#exercice 3
#renvoyer / afficher un message