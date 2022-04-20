x=[4,2,10,5]
i=0
b=[]
c=x[i+1]
while i<len(x)-1:
    c=x[i+1]
    d=(x[i]-c)
    b.append(d)
    i=i+2
print(b)    