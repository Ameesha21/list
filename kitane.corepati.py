m = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
crorepati=0
lakhpati=0
dilwale=0
while i<len(m):
    if m[i]>=100 and m[i]<100000:
        crorepati+=1
    elif m[i]>=100000 and m[i]<100000000:
        lakhpati+=1
    else:
        dilwale+=1
    i=i+1
print("totel number avobe crorepati are:",crorepati)
print("totel number of lakhpati:",lakhpati) 
print("totel number of dilwale:",dilwale)               
