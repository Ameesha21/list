list=[1,2,3,4]
i=0
b=[]
while i<len(list):
    j=0
    while j<len(list):
        c=list[i]+list[j]
        b.append(c)
        j=j+1
        i=i+1
print(b)