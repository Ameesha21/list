numbers=[50,40,23,70,56,12,5,10,7]
i=0
s=0
while i<len(numbers):
    if numbers[i]>s:
        s=numbers[i]
    i=i+1
print(s)    
    