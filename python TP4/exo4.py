L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
    Completez le programme a partir d'ici.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /"""

fonction= {}
for i in L1:
    if i in fonction:
        fonction[i]+=1
    else:
        fonction[i]=1
max=0
nombre=0
for i in fonction:
    if fonction[i]>max:
        max=fonction[i]
        nombre=i
print("Le nombre le plus frequent dans la liste est le :",nombre,"(",max,"x)")

""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
