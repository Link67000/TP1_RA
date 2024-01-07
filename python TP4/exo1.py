table=float(input("de quel nombre vous cherchez la table de multiplication?"))
z= table
i=0
print(table)
for i in range(9):
 
    i = i+1
    table = table*i
    print("{} * {} = {}".format(z,i,round(table,1)))
    table = z
