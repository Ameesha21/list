n=[2,4,6,7,8]
p=int(input("enter the number"))
i=0
a=[]
while i<len(n):
    j=0
    b=[]
    while j<len(n):
        if n[i]+n[j]==p and n[j]>n[i]:
            b.append(i)
            b.append(j)
            a.append(b)
        j=+j+1
    i=i+1
print(a)            