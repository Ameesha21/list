# list[(2,5),(1,2),(4,4),(2,3),(2,1)]
# i=0
# while i<len(list):
#     list.reverse()
#     print(list)
#     i=i+1
# print(list)


# list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
# i=0
# while i<len(list):
#     list.reverse()
#     i=i+1
# print(list)



# list=[[4,[5,[10],[12]]]]
# print(list[0][0])      
# print(list[0][1][0])
# print(list[0][1][1][0])
# print(list[0][1][2][2][1])



# list=[4,10,20]
# print(list[1])

# list=[[30,40,50]]
# print(list[0][2])



# list=[18,[2,3,4],14,15,[6,11,18,9,[2,10,6]]]
# print(list[1][0])
# print(list[3])
# print(list[4][2])
# print(list[4][4][1])

name=int(input("enter the index"))
list=["manpreet","nishu","karisma","ameesha"]
i=0
b=[]
while i<len(list):
    a=list[0][1]
    b.append(a)
    i=i+1
print(b)        
