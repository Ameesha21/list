d=[[2,4,5],[6,4]]
i=0
b=[]
while i<len(d):
    j=0
    c=0
    while j<len(d[i]):
        c+=d[i][j] 
        j=j+1
    b.append(c)
    i=i+1
print(b)



