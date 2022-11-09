#Importer le module random
#Importer le module time
#créer une liste avec pierre feuille ciseaux
#Créer variable winPlayerUn et la mettre à 0
#Créer variable winPlayerDeux et la mettre à 0
#Créer variable winPlayerRobot et la mettre à 0
#Demander combien de joueur entre 1 et 2
#Demander avec la variable round combien de round à gagner
#Demender avec la variable typeJeu si il veut jouer au jeu classique (1) au jeu clasique mais à personalisé (2) au jeu à personalisé (3)
#Si typeJeu est égal à 1
    #Alors : tant que winPlayerUn < round ou winRobot < round
        #Demander avec la variable choixJoueur que veut jouer le joueur
        #Créer une variable choixRobot qui prend un string  au hasars dans la liste listeClassique
        #Dormir 1 seconde
        #Ecrire pierre
        #Dormir 1 seconde
        #Ecrire fueille
        #Dormir 1 seconde
        #Ecrire ciseuax
        #dormir 1 seconde
        #Ecrire "Choix robot : ",choixRobot," VS Choix joueur : ",choixJoueur
        #dormir 1 seconde
        #Si choixRobot == choixJoueur
            #Alors : ecrire "égalité"
        #Sinon si choixRobot == "pierre" et choixJoueur == "feuille"
            #Alors : ecrire "le robot à gagner et tu a perdue"
            #Incrementer 1 à winRobot
            #Dormir 0.5 seconde
            #Ecrire "le robot est à ",winRobot, "victoire et le joueur est à ",winJoueur
    #Si winPLayerUn == 5
        #Alors : écrire "tu as gagner"
    #Sinon : écrire "tu as perdu"
    #ld