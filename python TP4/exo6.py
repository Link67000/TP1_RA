n = [5, 2, 4, 8, 1, 3]
print(n)


for i in range(0, len(n)):
    for j in range(i+1, len(n)):
        if n[i] > n[j]:
            n[i], n[j] = n[j], n[i]
            print(n)

#: print(sorted(tab))  ordre des croissant
#tab.sort() on remet la liste principale