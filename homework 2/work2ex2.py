list1= [11,  7, 5,  8, 5,  37,  11, 5]
list2= [22, 8, 10, 1, 11]
list3=[ 71, 3, 22, 8, 2, 14, 1]
lists=[]
no_dup_Lists=[]

for list in list1, list3, list2:
   noDup=set(list)
   if len(noDup)<len(list):
       lists.append(list)
   else:
        no_dup_Lists.append(list)
print(lists)
# print(nodupLIsts)

common=[]
for list in no_dup_Lists:
    if common==[]:
        common=set(list)
    common=set(list).intersection(common)
print(common)