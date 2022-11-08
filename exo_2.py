def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def modulo(x,y):
    return x % y

# salire bordel
salaire = 2450

print("votre salire anuelle est de ",salaire," euro par an. Soit " ,divide(salaire,12), " euro par moi. Soit ", divide(divide(salaire,12),25), " euro par jour ouvrés. Soit ",divide(divide(divide(salaire,12),25),60), " euro par heure. Soit ", divide(divide(divide(divide(salaire,12),25),60),60), " euro par seconde")

#salaire net

print("votre slaire net est de ", sub(salaire,multiply(salaire,0.23)), " euro")

