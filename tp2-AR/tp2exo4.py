BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue :"))

fromageConv = fromage * nbConvives / BASE
eauConv= eau * nbConvives / BASE
ailConv = ail * nbConvives / BASE
painConv = pain * nbConvives / BASE

print("Pour faire une fondue fribourgeoise pour {} personnes, il vous faut: ".format(nbConvives))
print("{} gr de fromage".format(fromageConv))
print("{} dl d'eau".format(eauConv))
print("{} gousse(s) d'ail".format(ailConv))
print("{} gr de pain".format(painConv))