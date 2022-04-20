numbers=[50,39,27,40,23,70,56,12,5,10,37,30,31,28,22,]
i=0
count=[]
while i<len(numbers):
    if numbers[i]>=20 and numbers[i]<=40:
        count.append(numbers[i])
    i=i+1
print(count)
