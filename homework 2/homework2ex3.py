list=[98789,45456,345345,4670156,2342,6969,46456]
set1=set()
order="desc"
for num in list:
    list = [int(a) for a in str(num)]
    for number in list:
        set1.add(number)
res=sorted(set1)
if(order=="desc"):
    res.reverse()
print(res)
