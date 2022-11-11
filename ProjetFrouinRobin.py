#DEBUT
#Importer le module random
import random
#Importer le module time
import time

#Définir jouer qui retourne une foction input qui demande si l'utilisateur veut jouer où oui = 1 et non =2
jouer = int(input("Souhaitez-vous jouez au pierre feuille ciseaux ? Si oui tapez 1. Si non tapes 2. : "))
#Si jouer est égale à 1
if jouer == 1:
    #tant que jouer est égal à 1
    while jouer == 1:
        #Alors :
        #Définir nbJoueur qui retourne une fonction input qui demande combien y a-t-il de joueur
        nbJoueur = int(input("Veuillez choisir le nombre de joueur entre 1 et 2 joueur. : "))
        #Définir typeJeu qui retourne une fonction input qui demande à quel type de jeu l'utilisateur veut jouer : jeu classique (1) ou jeu personalisé (2)
        typeJeu = int(input("Nous vous proposons 2 type de jeu. Le jeu clasique, et le jeu personalisé. Dans ce dernier, vous pouvez nommer comme les élément comme vous le voulez. Tapez 1 pour le mode classique et tapez 2 pour le mode personalisé"))
        #Définir round qui retourne une fonction input qui demande combien de round sont nécessaire pour gagner le match
        round = int(input("Combien de round seront nécaissaire pour gagner le match ? : "))
        #Créer variable winPlayerUn et la mettre à 0
        winPlayerUn = 0
        #Créer variable winPlayerDeux et la mettre à 0
        winPlayerDeux = 0
        #Créer variable winPlayerRobot et la mettre à 0
        winRobot = 0
        #Créer variable winJoueur et la mettre à 0
        winJoueur = 0
        #Si typeJeu est égal à 1 et nbJoueur est égal à 1
        if typeJeu == 1 and nbJoueur == 1:
            #Alors :
            #créer une liste listeClassique avec "pierre" "feuille" "ciseaux"
            listeClassique = ["pierre","feuille","ciseaux"]
            #Définir round qui retourne une fonction input qui demande combien de round sont nécessaire pour gagner le match
            round = int(input("Combien de round seront nécaissaire pour gagner le match ? : "))
            while winRobot < round and winJoueur < round:
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
        elif typeJeu == 1 and nbJoueur == 2:
            #Alors :
            #Définir pseudoJoueurUn qui retourne une fonction input qui demande quel pseudo veut le joueur 1
            pseudoJoueurUn = str(input("Joueur 1 comment souhaitez vous vous apeller ? : "))
            #Définir pseudoJoueurDeux qui retourne une fonction input qui demande quel pseudo veut le joueur 2
            pseudoJoueurDeux = str(input("Joueur 2 comment souhaitez vous vous apeller ? : "))
            # tant que winPlayerUn < round ou winPlayerDeux < round
            while winPlayerUn < round and winPlayerDeux < round:
                #Définir choixJoueurUn qui retourne une fonction input qui demande ce que veut jouer le joueur 1
                choixJoueurUn = str(input(pseudoJoueurUn + " choisissez entre pierre feuille et ciseaux. Attention à bien écrire ! : "))
                #Définir choixJoueurDeux qui retourne une fonction input qui demande ce que veut jouer le jouer 2
                choixJoueurDeux = str(input(pseudoJoueurDeux + " choisissez entre pierre feuille et ciseaux. Attention à bien écrire ! : "))
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
                #Ecrire "Choix ",pseudoJoueurUn," : ",choixJoueurUn," VS Choix ",pseudoJoueurDeux," : ",choixJoueurDeux
                print(pseudoJoueurUn," à choisi ",choixJoueurUn," et ",pseudoJoueurDeux," à choisi ",choixJoueurDeux)
                #dormir 1 seconde
                time.sleep(1)
                #Si choixJoueurUn == choixJoueurDeux
                if choixJoueurUn == choixJoueurDeux:
                    #Alors : ecrire "égalité"
                    print("égalité")
                #Sinon si choixJoueurUn == "pierre" et choixJoueurDeux == "ciseaux"
                elif choixJoueurUn == "pierre" and choixJoueurDeux == "ciseaux":
                    #Alors : ecrire pseudoJoueurUn," a gagner"
                    print(pseudoJoueurUn," a gangé")
                    #Incrementer 1 à winPlayerUn
                    winPlayerUn = winPlayerUn + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire pseudoJoueurUn," est à ",winPlayerUn, "manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux " manche(s) remporté(s)."
                    print(pseudoJoueurUn," est à ",winPlayerUn," manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux," manche(s) remporté(s).")
                #Sinon si choixJoueurUn == "ciseaux" et choixJoueurDeux == "pierre"
                elif choixJoueurUn == "ciseaux" and choixJoueurDeux == "pierre":
                    #Alors : écrire pseudoJoueurDeux," à gagner"
                    print(pseudoJoueurDeux," à gagner")
                    #Incrementer 1 à winPlayerDeux
                    winPlayerDeux = winPlayerDeux + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire pseudoJoueurUn," est à ",winPlayerUn, "manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux " manche(s) remporté(s)."
                    print(pseudoJoueurUn," est à ",winPlayerUn," manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux," manche(s) remporté(s).")
                #Sinon si choixJoueurUn == "feuille" et choixJoueurDeux == "pierre"
                elif choixJoueurUn == "feuille" and choixJoueurDeux == "pierre":
                    #Alors : ecrire pseudoJoueurUn," a gagner"
                    print(pseudoJoueurUn," a gangé")
                    #Incrementer 1 à winPlayerUn
                    winPlayerUn = winPlayerUn + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire pseudoJoueurUn," est à ",winPlayerUn, "manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux " manche(s) remporté(s)."
                    print(pseudoJoueurUn," est à ",winPlayerUn," manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux," manche(s) remporté(s).")
                #Sinon si choixJoueurUn == "pierre" et choixJoueurDeux == "feuille"
                elif choixJoueurUn == "pierre" and choixJoueurDeux == "feuille":
                    #Alors : écrire pseudoJoueurDeux," à gagner"
                    print(pseudoJoueurDeux," à gagner")
                    #Incrementer 1 à winPlayerDeux
                    winPlayerDeux = winPlayerDeux + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire pseudoJoueurUn," est à ",winPlayerUn, "manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux " manche(s) remporté(s)."
                    print(pseudoJoueurUn," est à ",winPlayerUn," manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux," manche(s) remporté(s).")
                #Sinon si choixJoueurUn == "ciseaux" et choixJoueurDeux == "feuille"
                elif choixJoueurUn == "ciseaux" and choixJoueurDeux == "feuille":
                    #Alors : ecrire pseudoJoueurUn," a gagner"
                    print(pseudoJoueurUn," a gangé")
                    #Incrementer 1 à winPlayerUn
                    winPlayerUn = winPlayerUn + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire pseudoJoueurUn," est à ",winPlayerUn, "manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux " manche(s) remporté(s)."
                    print(pseudoJoueurUn," est à ",winPlayerUn," manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux," manche(s) remporté(s).")
                #Sinon si choixJoueurUn == "feuille" et choixJoueurDeux == "ciseaux"
                elif choixJoueurUn == "feuille" and choixJoueurDeux == "ciseaux":
                    #Alors : écrire pseudoJoueurDeux," à gagner"
                    print(pseudoJoueurDeux," à gagner")
                    #Incrementer 1 à winPlayerDeux
                    winPlayerDeux = winPlayerDeux + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire pseudoJoueurUn," est à ",winPlayerUn, "manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux " manche(s) remporté(s)."
                    print(pseudoJoueurUn," est à ",winPlayerUn," manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux," manche(s) remporté(s).")
                else:
                    print("une erreur de frappe est survenue. Veuillez réessayer")
        #Sinon si typeJeu est égal à 2 et nbJoueur est égal à 1
        elif typeJeu == 2 and nbJoueur == 1:
            #Alors:
            #Définir variable pierre qui retourne une fonction input qui demande par quelle nom l'utilisateur veut remplacer la pierre
            pierre = str(input("Comment voulez vous renommer la pierre"))
            #Définir variable feuille qui retourne une fonction input sui demande par quelle nom l'utilisateur veut remplacer la feuille
            feuille = str(input("Comment voulez vous renommer la feuille"))
            #Définir variable ciseaux qui retourne une fonction input qui demande par quelle nom l'utilsateur veut remplacer le ciseaux
            ciseaux = str(input("Comment voulez vous renommer la ciseaux"))
            #créer une liste listePerso avec les variables pierre feuille ciseaux
            listePerso = [pierre,feuille,ciseaux]
            #Tant que winJoueur < round ou winRobot < round
            while winRobot < round and winJoueur < round:
                #Définir choixJoueur qui retourne une fonction input qui demande le choix du jouer
                choixJoueur = str(input("choisissez entre" + pierre + ", " + feuille + ", et " +  ciseaux + ". Attention à bien écrire ! : "))
                #Créer une variable choixAleatoire qui retourne avec une fonction random un élément aléatoire dans la liste listeClassique
                choixAleatoire = random.choice(listePerso)
                #Définir choixRobot qui retourne une fonnction random dans la liste listePerso
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
                elif choixRobot == pierre and choixJoueur == ciseaux:
                    #Alors : ecrire "le robot à gagner et tu a perdue"
                    print("le robot à gagner et tu a perdue")
                    #Incrementer 1 à winRobot
                    winRobot = winRobot + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur " manche(s) remporté(s)."
                    print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur, " manche(s) remporté(s).")
                #Sinon si choixRobot == ciseaux et choixJoueur == pierre
                elif choixRobot == ciseaux and choixJoueur == pierre:
                    #Alors : écrire "bravo tu as gagnés cette manche"
                    print("bravo tu as gagnés cette manche")
                    #Incrementer 1 à winJoueur
                    winJoueur = winJoueur + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur " manche(s) remporté(s)."
                    print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur, " manche(s) remporté(s).")
                #Sinon si choixRobot == "feuille" et choixJoueur == "pierre"
                elif choixRobot == feuille and choixJoueur == pierre:
                    #Alors : ecrire "le robot à gagner et tu a perdue"
                    print("le robot à gagner et tu a perdue")
                    #Incrementer 1 à winRobot
                    winRobot = winRobot + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur " manche(s) remporté(s)."
                    print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur, " manche(s) remporté(s).")
                #Sinon si choixRobot == "pierre" et choixJoueur == "feuille"
                elif choixRobot == pierre and choixJoueur == feuille:
                    #Alors : écrire "bravo tu as gagnés cette manche"
                    print("bravo tu as gagnés cette manche")
                    #Incrementer 1 à winJoueur
                    winJoueur = winJoueur + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur " manche(s) remporté(s)."
                    print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur, " manche(s) remporté(s).")
                #Sinon si choixRobot == "ciseaux" et choixJoueur == "feuille"
                elif choixRobot == ciseaux and choixJoueur == feuille:
                    #Alors : ecrire "le robot à gagner et tu a perdue"
                    print("le robot à gagner et tu a perdue")
                    #Incrementer 1 à winRobot
                    winRobot = winRobot + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire "le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur " manche(s) remporté(s)."
                    print("le robot est à ",winRobot, "manche(s) remporté(s) et le joueur est à ",winJoueur, " manche(s) remporté(s).")
                #Sinon si choixRobot == "feuille" et choixJoueur == "ciseaux"
                elif choixRobot == feuille and choixJoueur == ciseaux:
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
                    print("erreur, vous avez écris ",choixJoueur," au lieu de pierre, feuille ou ciseaux")
            #Si winJoueur == round
            if winJoueur == round:
                #Alors : écrire "tu as gagner"
                print("tu as gagner")
            #Sinon
            else:
                #Alors : écrire "tu as perdu"
                print("tu as perdu")
            #Dormir 1 seconde
            time.sleep(1)
            #Assigner à jouer le retour de la fonction input qui demande su l'utilisateurs veut rejouer où oui = 1 et non = 2
            jouer = int(input("Souhaitez-vous rejouer ? Tapez 1 pour oui et 2 pour non. : "))
        #Sinon si typeJeu est égal à 2 et nbJoueur est égal à 2
        elif typeJeu == 2 and nbJoueur == 2:
            #Alors :
            #Définir pseudoJoueurUn qui retourne une fonction input qui demande quel pseudo veut le joueur 1
            pseudoJoueurUn = str(input("Joueur 1 comment souhaitez vous vous apeller ? : "))
            #Définir pseudoJoueurDeux qui retourne une fonction input qui demande quel pseudo veut le joueur 2
            pseudoJoueurDeux = str(input("Joueur 2 comment souhaitez vous vous apeller ? : "))
            #Définir variable pierre qui retourne une fonction input qui demande par quelle nom l'utilisateur veut remplacer la pierre
            pierre = str(input("Comment voulez vous renommer la pierre"))
            #Définir variable feuille qui retourne une fonction input sui demande par quelle nom l'utilisateur veut remplacer la feuille
            feuille = str(input("Comment voulez vous renommer la feuille"))
            #Définir variable ciseaux qui retourne une fonction input qui demande par quelle nom l'utilsateur veut remplacer le ciseaux
            ciseaux = str(input("Comment voulez vous renommer la ciseaux"))
            # tant que winPlayerUn < round ou winPlayerDeux < round
            while winPlayerUn < round and winPlayerDeux < round:
                #Définir choixJoueurUn qui retourne une fonction input qui demande ce que veut jouer le joueur 1
                choixJoueurUn = str(input(pseudoJoueurUn + " choisissez entre " + pierre + ", " + feuille + " et " + ciseaux + ". Attention à bien écrire ! : "))
                #Définir choixJoueurDeux qui retourne une fonction input qui demande ce que veut jouer le jouer 2
                choixJoueurDeux = str(input(pseudoJoueurDeux + " choisissez entre " + pierre + ", " + feuille + " et " + ciseaux+". Attention à bien écrire ! : "))
                #Dormir 1 seconde
                time.sleep(1)
                #Ecrire pierre
                print(pierre)
                #Dormir 1 seconde
                time.sleep(1)
                #Ecrire fueille
                print(feuille)
                #Dormir 1 seconde
                time.sleep(1)
                #Ecrire ciseuax
                print(ciseaux)
                #dormir 1 seconde
                time.sleep(1)
                #Ecrire "Choix ",pseudoJoueurUn," : ",choixJoueurUn," VS Choix ",pseudoJoueurDeux," : ",choixJoueurDeux
                print(pseudoJoueurUn," à choisi ",choixJoueurUn," et ",pseudoJoueurDeux," à choisi ",choixJoueurDeux)
                #dormir 1 seconde
                time.sleep(1)
                #Si choixJoueurUn == choixJoueurDeux
                if choixJoueurUn == choixJoueurDeux:
                    #Alors : ecrire "égalité"
                    print("égalité")
                #Sinon si choixJoueurUn == "pierre" et choixJoueurDeux == "ciseaux"
                elif choixJoueur == pierre and choixJoueurDeux == ciseaux:
                    #Alors : ecrire pseudoJoueurUn," a gagner"
                    print(pseudoJoueurUn," a gangé")
                    #Incrementer 1 à winPlayerUn
                    winPlayerUn = winPlayerUn + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire pseudoJoueurUn," est à ",winPlayerUn, "manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux " manche(s) remporté(s)."
                    print(pseudoJoueurUn," est à ",winPlayerUn," manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux," manche(s) remporté(s).")
                #Sinon si choixJoueurUn == "ciseaux" et choixJoueurDeux == "pierre"
                elif choixJoueurUn == ciseaux and choixJoueurDeux == pierre:
                    #Alors : écrire pseudoJoueurDeux," à gagner"
                    print(pseudoJoueurDeux," à gagner")
                    #Incrementer 1 à winPlayerDeux
                    winPlayerDeux = winPlayerDeux + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire pseudoJoueurUn," est à ",winPlayerUn, "manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux " manche(s) remporté(s)."
                    print(pseudoJoueurUn," est à ",winPlayerUn," manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux," manche(s) remporté(s).")
                #Sinon si choixJoueurUn == "feuille" et choixJoueurDeux == "pierre"
                elif choixJoueurUn == feuille and choixJoueurDeux == pierre:
                    #Alors : ecrire pseudoJoueurUn," a gagner"
                    print(pseudoJoueurUn," a gangé")
                    #Incrementer 1 à winPlayerUn
                    winPlayerUn = winPlayerUn + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire pseudoJoueurUn," est à ",winPlayerUn, "manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux " manche(s) remporté(s)."
                    print(pseudoJoueurUn," est à ",winPlayerUn," manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux," manche(s) remporté(s).")
                #Sinon si choixJoueurUn == "pierre" et choixJoueurDeux == "feuille"
                elif choixJoueurUn == pierre and choixJoueurDeux == feuille:
                    #Alors : écrire pseudoJoueurDeux," à gagner"
                    print(pseudoJoueurDeux," à gagner")
                    #Incrementer 1 à winPlayerDeux
                    winPlayerDeux = winPlayerDeux + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire pseudoJoueurUn," est à ",winPlayerUn, "manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux " manche(s) remporté(s)."
                    print(pseudoJoueurUn," est à ",winPlayerUn," manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux," manche(s) remporté(s).")
                #Sinon si choixJoueurUn == "ciseaux" et choixJoueurDeux == "feuille"
                elif choixJoueurUn == ciseaux and choixJoueurDeux == feuille:
                    #Alors : ecrire pseudoJoueurUn," a gagner"
                    print(pseudoJoueurUn," a gangé")
                    #Incrementer 1 à winPlayerUn
                    winPlayerUn = winPlayerUn + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire pseudoJoueurUn," est à ",winPlayerUn, "manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux " manche(s) remporté(s)."
                    print(pseudoJoueurUn," est à ",winPlayerUn," manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux," manche(s) remporté(s).")
                #Sinon si choixJoueurUn == "feuille" et choixJoueurDeux == "ciseaux"
                elif choixJoueurUn == feuille and choixJoueurDeux == ciseaux:
                    #Alors : écrire pseudoJoueurDeux," à gagner"
                    print(pseudoJoueurDeux," à gagner")
                    #Incrementer 1 à winPlayerDeux
                    winPlayerDeux = winPlayerDeux + 1
                    #Dormir 0.5 seconde
                    time.sleep(0.5)
                    #Ecrire pseudoJoueurUn," est à ",winPlayerUn, "manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux " manche(s) remporté(s)."
                    print(pseudoJoueurUn," est à ",winPlayerUn," manche(s) remporté(s) et ",pseudoJoueurDeux," est à ",winPlayerDeux," manche(s) remporté(s).")
            #Si winPLayerUn == round
            if winPlayerUn == round :
                #Alors : écrire pseudoJoueurUn," à gagner"
                print(pseudoJoueurUn," à gagner")
            #Sinon
            else:
                #Alors : écrire pseudoJoueurDeux," à gagner"
                print(pseudoJoueurUn," à gagner")
        #Dormir 1 seconde
        time.sleep(1)

        #Assigner à jouer le retour de la fonction input qui demande su l'utilisateurs veut rejouer où oui = 1 et non = 2
        jouer = int(input("Souhaitez-vous rejouer ? Tapez 1 pour oui et 2 pour non. : "))
        #Sinon si typeJeu est égal à 1 et nbJoueur est égal à 2
    #Ecrire "merci d'avoir jouer a la prochaine fois"
    print("merci d'avoir jouer. A la prochaine fois")
#Sinon si jouer == 2
elif jouer == 2:
    #Alors : écrire "d'accord au-revoir"
    print("d'accord au revoir")
#Sinon
else:
    #Alors: écrire "t'es con ou...1 ou 2 c'est pas compliqué pourtant"
    print("t'es con ou...1 ou 2 c'est pas compliqué pourtant!")
#FIN