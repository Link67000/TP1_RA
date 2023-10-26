nb = int(input("Entrez un nombre entier :"))
if nb%2 == 0:
    if nb > 0:
        print("Le nombre est positif et pair")
    elif nb < 0:
        print("Le nombre est inférieur à 0 et pair ")
    elif nb == 0:
        print("Le nombre est zéro à 0 et pair ")
else:
    if nb > 0:
        print("Le nombre est positif et impair")
    elif nb < 0:
        print("Le nombre est inférieur à 0 et impair ")
    elif nb == 0:
        print("Le nombre est zéro à 0 et pair ")