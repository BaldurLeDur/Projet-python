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
#import time
#import random
#caracteres = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN0123456789"

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
#elif jouer == "non":
#    print("bah dis le si je te fais chier")
#else:
 #   print("azy écris bien aussi batard !")

#exercice 1
#faire une fonnction qui concatene 2 chaine de caractère, les séparent par une virgule
#def char (charUn,CharDeux):
#    return charUn + ", " + CharDeux
#print(char("hello","world"))
#exercie 2
#fire une fonction qui itere sur tous les index d'un tableau renvoyant une chaine de caractere
#avec l'ensembles des occurence d'un chiffre e.g.:
tableau = [0,1,1,1,0,1,1,0,1]
#la fonction(tableau, 0) doit renvoyez "0, 4, 7" n'hésitez pas a implanter la première fonction
#Définir un boolen tels que firstTurn est true
firstTurn = True
def concatWithComma(strA,strB):
    strAChange = str(strA)
    strBChange = str(strB)
    return strAChange + ', ' + strBChange
#definir la fonctio findIndex qui itere sur tableau, cherchant l'index des différentes occurences de x
def findIndex(tableau,x):
    #Definir l'index de départ i
    i = 0
    #Definir chaineRetour telle qu'une chaine de caractère vide
    chaineRetour = ''
    #Tant que i est différent du nombre d'élément dans le tableu
    while i != len(tableau):
        #Alors j'attribue une variable la valeur de tableau à l'index i
        selected = tableau[i]
        #Si selected est égal à x ET que firstTurn
        if selected == x and selected == firstTurn:
            #Alors on assigne à chaineRetour le retour de str(i)
            chaineRetour = str(i)
            #Changer la valeur de firstTurn a false
            firstTurn = False
        #Si selected = x
        if selected == x:
            #Alors j'assigne le retour de concatWithComma tel que : concatWithComma(chaineRetour, i) à chaineRetour
            chaineRetour = concatWithComma(chaineRetour,i)
        i = i + 1
    return chaineRetour






#exercice 3
#renvoyer / afficher un message




#Si winJoueur == round
                if winJoueur == round:
                    #Alors : écrire "tu as gagner"
                    print("tu as gagner")
                    #Dormir 1 seconde
                    time.sleep(1)
                    #Assigner à jouer le retour de la fonction input qui demande su l'utilisateurs veut rejouer où oui = 1 et non = 2
                    jouer = int(input("Souhaitez-vous rejouer ? Tapez 1 pour oui et 2 pour non. : "))
                #Sinon
                elif winRobot == round:
                    #Alors : écrire "tu as perdu"
                    print("tu as perdu")
                    #Dormir 1 seconde
                    time.sleep(1)
                    #Assigner à jouer le retour de la fonction input qui demande su l'utilisateurs veut rejouer où oui = 1 et non = 2
                    jouer = int(input("Souhaitez-vous rejouer ? Tapez 1 pour oui et 2 pour non. : "))
                else:
                    #Définir choixJoueur qui retourne une fonction input qui demande le choix du jouer
                    choixJoueur = str(input("choisissez entre pierre feuille et ciseaux. Attention à bien écrire ! : "))
                    #Créer une variable choixAleatoire qui retourne avec une fonction random un élément aléatoire dans la liste listeClassique
                    choixAleatoire = random.choice(listeClassique)
                    #Définir choixRobot qui retourne une fonnction random dans la liste listeClassique
                    choixRobot = choixAleatoire
                    #Dormir 1 seconde
                    time.sleep(1)
                    #Ecrire pierre
                    print("pierre")
                    #Dormir 1 seconde
                    time.sleep(1)
                    #Ecrire fueille
                    print("feuille")
                    #Dormir 1 seconde
                    time.sleep(1)
                    #Ecrire ciseuax
                    print("ciseaux")
                    #dormir 1 seconde
                    time.sleep(1)
                    #Ecrire "Choix robot : ",choixRobot," VS Choix joueur : ",choixJoueur
                    print("le robot à choisi : ",choixRobot," et vous avez choisi : ",choixJoueur,)
                    #dormir 1 seconde
                    time.sleep(1)
                    #Si choixRobot == choixJoueur
                    if choixRobot == choixJoueur:
                        #Alors : ecrire "égalité"
                        print("C'est une égalité !")
                    #Sinon si choixRobot == "pierre" et choixJoueur == "ciseaux"
                    elif choixRobot == "pierre" and choixJoueur == "ciseaux":
                        #Alors : ecrire "le robot à gagner et tu a perdue"
                        print("le robot à gagner et tu a perdue")
                        #Incrementer 1 à winRobot
                        winRobot = winRobot + 1
                        #Dormir 0.5 seconde
                        time.sleep(0.5)
                        #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur " manche(s) remporté(s)."
                        print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur, " manche(s) remporté(s).")
                    #Sinon si choixRobot == "ciseaux" et choixJoueur == "pierre"
                    elif choixRobot == "ciseaux" and choixJoueur == "pierre":
                        #Alors : écrire "bravo tu as gagnés cette manche"
                        print("bravo tu as gagnés cette manche")
                        #Incrementer 1 à winJoueur
                        winJoueur = winJoueur + 1
                        #Dormir 0.5 seconde
                        time.sleep(0.5)
                        #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur " manche(s) remporté(s)."
                        print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur, " manche(s) remporté(s).")
                    #Sinon si choixRobot == "feuille" et choixJoueur == "pierre"
                    elif choixRobot == "feuille" and choixJoueur == "pierre":
                        #Alors : ecrire "le robot à gagner et tu a perdue"
                        print("le robot à gagner et tu a perdue")
                        #Incrementer 1 à winRobot
                        winRobot = winRobot + 1
                        #Dormir 0.5 seconde
                        time.sleep(0.5)
                        #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur " manche(s) remporté(s)."
                        print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur, " manche(s) remporté(s).")
                    #Sinon si choixRobot == "pierre" et choixJoueur == "feuille"
                    elif choixRobot == "pierre" and choixJoueur == "feuille":
                        #Alors : écrire "bravo tu as gagnés cette manche"
                        print("bravo tu as gagnés cette manche")
                        #Incrementer 1 à winJoueur
                        winJoueur = winJoueur + 1
                        #Dormir 0.5 seconde
                        time.sleep(0.5)
                        #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur " manche(s) remporté(s)."
                        print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur, " manche(s) remporté(s).")
                    #Sinon si choixRobot == "ciseaux" et choixJoueur == "feuille"
                    elif choixRobot == "ciseaux" and choixJoueur == "feuille":
                        #Alors : ecrire "le robot à gagner et tu a perdue"
                        print("le robot à gagner et tu a perdue")
                        #Incrementer 1 à winRobot
                        winRobot = winRobot + 1
                        #Dormir 0.5 seconde
                        time.sleep(0.5)
                        #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur " manche(s) remporté(s)."
                        print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur, " manche(s) remporté(s).")
                    #Sinon si choixRobot == "feuille" et choixJoueur == "ciseaux"
                    elif choixRobot == "feuille" and choixJoueur == "ciseaux":
                        #Alors : écrire "bravo tu as gagnés cette manche"
                        print("bravo tu as gagnés cette manche")
                        #Incrementer 1 à winJoueur
                        winJoueur = winJoueur + 1
                        #Dormir 0.5 seconde
                        time.sleep(0.5)
                        #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur " manche(s) remporté(s)."
                        print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur, " manche(s) remporté(s).")
                    #Sinon
                    else:
                        #Alors : écrire "erreur, vous avez écris",choixJoueur,"au lieu de pierre, feuille, ciseaux"
                        print("erreur, vous avez écris",choixJoueur,"au lieu de pierre, feuille ou ciseaux")