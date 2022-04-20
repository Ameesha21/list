name=input("enter the number")
a=["amesha","manprrit","devika","dars"]
i=0
b=[]
while i<len(a):
    if a[i][0] in name:
        b.append(a[i])
    i=i+1
print(b)

