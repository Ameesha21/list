magic_square=[[8,3,4],[1,5,9],[6,7,2]]
i=0
while i<len(magic_square):
    j=0
    row=0
    c=0
    d=0
    while j<len(magic_square[i]):
        row=row +magic_square[i][j]
        c=c+magic_square[j][i]
        d=d+magic_square[j][j]
        j=j+1
    i=i+1
if row==c==d:
    print("magic_square")   
else:
    print("not a magic_square") 
print(c)          
print(row)
print(d)




 

# list=[
#      [8,3,4],
#      [1,5,9],
#      [6,7,2]
#      ]
# i=0
# a=0
# b=0
# c=0
# d=0
# e=0
# f=0
# g=0
# h=0
# while i<len(list):
#     a=a+list[0][i]
#     b=b+list[1][i]
#     c=c+list[2][i]
#     d=d+list[i][0]
#     e=e+list[i][1]
#     f=f+list[i][2]
#     g=g+list[i][i]
#     h=h+list[i][2-i]
#     i=i+1
# if a==b==c==d==e==f==g==h:
#     print("magic square") 
# else:
#     print("not magic square")


# list=[
#     [5,3,7],
#     [1,8,9],
#     [6,4,2]
# ]
# i=0
# a=0
# b=0
# c=0
# d=0
# e=0
# f=0
# g=0
# h=1
# while i<len(list):
#     a=a+list[0][i]
#     b=b+list[1][i]
#     c=c+list[2][i]
#     d=d+list[i][0]
#     e=e+list[i][1]
#     f=f+list[i][2]
#     g=g+list[i][i]
#     h=h+list[i][2-i]
# if a==b==c==d==e==f==g==h:
#     print("magic square") 
# else:
#     print("not magic square")  
         
           
    


           
    