#DEBUT
#Definir une fonction withdrawFees qui retire un pourcentage qui retire un pourcentage a un total en fonction d'un total et d'un pourcentage
def withdrawFees(total, pourcentage):
    #definir fees en fpnction d'un total et d'un pourcentage
    fees = total * (pourcentage/100)
    #soustraire fees au total
    result = total - fees
    #retourner la valeur obtenue
    return result

#Définir une fonction qui retourne le salaire net en fonction du salaire brut (float) et du secteur d'activité (isPublic > booleen)
def calculBrutEnNet(salaireBrut, isPublic):
    #Si je suis travailleur du secteur publique
    if isPublic:
        #Alors je soustrais 15 % de mon salaire brut et je l'assigne a la variable salaireNet
        #salaireNet = salaireBrut - (salaireBrut * (15/100))
        salaireNet = withdrawFees(salaireBrut, 15)
    #Sinon : je suis travailleur du secteur privé
    else:
        #Aloprs je soustrait 23 % de mon salaire brut a mon slaire brut et je l'assigne à la variable salaireNet
        salaireNet = withdrawFees(salaireBrut, 15)
    #Retourner salaireNet
    return salaireNet
#FIN