list=[1,2,3],[3,5,6,],[1,4,8,]
i=0
b=[]
while i<len(list):
    j=0
    c=[]
    while j<len(list[i]):
        c=c+(list[i][j])
        j=j+1
        b.append(c)
        i=i+1
print(b)    