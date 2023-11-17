def a():
    N = input("entrez votre nombre ICI !")
    N = int(N)
    val = 0
    while val <= N:
        print("la valeur de N est {}".format(val))
        val = val + 1


def b():
    i = 0
    for i in range(1000):
        nombre = int(input("Entrez votre valeur"))
        if nombre == 100:
            break
        else:
            nombre = int(input("Entrez votre valeur"))



def c():
    i = 0
    while i != 10:
        i = i+1
        val = int(input("Entrez votre valeur "))
        if val > 20 and val < 0:
            i=i-1
            val = int(input("Entrez votre valeur "))
        else:
            if val < 10:
                print("la valeur est inférieur strictement à 10")
            elif val >= 10 and val < 15:
                print("le nombre est supérieur ou égal à 10 et inférieur à 15")
            elif val >= 15:
                print("le nombre est supérieur ou égal à 15")


def d():
    print("nul")





exo = input("quel exercice voulez vous ??")
if exo == "a":
    a()
if exo == "b":
    b()
if exo == "c":
    c()
if exo == "d":
    d()
