import random
nombreRandom = random.randint(0,100)
compteur = 0

while True:
    a = int(input("a votre avis quel est le bon nombre???"))
    if a == nombreRandom:
        print("vous avez trouvé le bon nombre ")
        compteur = compteur +1
        print("votre nombre d'essaie est de {}".format(compteur))
        break
    elif a != nombreRandom:
        compteur = compteur +1
        print("essayez à nouveau !")
        if nombreRandom < a:
            print("le nombre est plus petit\n")
        else:
            print("le nombre est plus grand\n")


