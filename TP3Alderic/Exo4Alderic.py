facto = 1
fac = int(input("Entrez la valeur pour la factorielle"))
for i in range(fac +1):
    if i > 0:
       facto = facto*i
       print("la valeur de la factorielle est {}".format(facto))

