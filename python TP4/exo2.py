nombreEtudiants = int(input("Donnez le nombre d'etudiants : \n"))
moyenne = 0.0
i=1
notes = []
for i in range(0,nombreEtudiants):
    x = input("note de l'étudiant {} :".format(i))
    x=int(x)


    if x < 20 and x > 0:
        notes.append(x)
        i=i+1
    else:
        i=i-1
        print("cette valeur ne peut pas marcher")
       
moyenne = sum(notes) / nombreEtudiants
print("Moyenne de classe : {}".format(moyenne))
