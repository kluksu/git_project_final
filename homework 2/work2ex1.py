s="eeerrrffddhhhhhggggggyyy"
obj={}
obj2={}
sorted=[]
for letter in s:
 obj[letter]=obj.get(letter,0)+1
 
list=list(obj.items())
list.sort()
print(list)

for pair in obj.items():
 if(pair[1] not in obj2 ):
     obj2[pair[1]]=[]

 obj2[pair[1]].append(pair[0])

print(obj2)