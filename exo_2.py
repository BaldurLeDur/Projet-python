salaire = int(input("quelle est votre salaire ? : "))
fonction = int(input("pour fonction publique, tapez 1 et pour fonction privé tapez 2 : "))
if fonction == 1:
    print("votre salaire net est de " , salaire - salaire * 0.15, " euro")
else:
    print("votre salaire net est de " , salaire - salaire * 0.25, " euro")
