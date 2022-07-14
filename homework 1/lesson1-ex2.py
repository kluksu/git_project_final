lst1 = ["a", "b", "c"]
lst2 = ["x", "y", "z"]

range2=range(len(lst2)-1,-1, -1)
revers=[]
res=[]
for index in range2:
    revers.append(lst2[index])
for i,letter in enumerate(lst1) :

    res.append(letter + revers[i])
print(res)

