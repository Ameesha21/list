deci=[155]
strings=[str(deci)for deci in deci]
a="".join(strings)
b=int(a)
ab=0
power=0
while b>0:
    ab+=10**power*(b%2)
    b//=2
    power+=1
print("the binary number is ",ab)
