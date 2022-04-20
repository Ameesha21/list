# list=[1,2,3,4]
# i=0
# sum=0
# b=[]
# while i<len(list):
#     sum=sum+list[i]
#     b.append(sum)
#     i=i+1
# print(b) 
   
   
n=[[0],[1,3],[5,7],[9,11],[13,15,7]]
i=0
while i<len(n):
    j=0
    lar=0
    small=0
    p=[] 
    while j<len(n[i]):
        if len(n[i])>len(n[j]):
            lar=n[i]
        elif len(n[i])<len(n[j]):
            small=n[j] 
        j=j+1
    p.append(small) 
    i=i+1
print(lar,"maximum list") 
print(p,"minimum list")             
              