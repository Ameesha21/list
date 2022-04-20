# print("what is the capital of india")
# print("a-new delhi")
# print("b-kolkata")
# print("c-chandigarh")
# print("d-pune")

# option1="a"
# option2="b"
# option3="c"
# option4="d"

# q=input("please choose your answer")
# if q==str(option1):
#     print("you are right")
# elif q==str(option2):
#     print("you are worng")  
# elif q==str("you are worng"):
#     print("you are worng")
# else:
#     print("please choose a ralid option") 
    
# print("what is the capital of punjab")  
# print("who found microsott")  
# print("a -few delhi") 
# print("b-kolkata") 
# print("c-chandigarh") 
# print("d-pune")

# option1="A"
# option2="B"
# option3="C"
# option4="d"
# q=input("please choose youranswer")
# if q==str(option1):
#     print("you are right")
# elif q==str(option2):
#     print("you are worng")   
# elif q==str(option3):
#     print("you are worng") 
# elif q==str(option4):
#     print("you are worng")
# else:
#     print("please choose a valid option")  
# print("who founded micosoft?") 

# print("a-elonmusk")  
# print("b-jeff")   
# print("c mark")
# print("d bill gates")

# option1="A"
# option2="B"
# option3="C"
# option4="D"

# q=input("please choose your answers")
# if q==str(option1):
#     print("you are worng")
# elif q==str(option2):
#     print("you are worng")
# elif q==str(option3):
#     print("you are worng")  
# elif q==str(option4):
#     print("you are worng")
# else:
#     print("please choose a valid option") 




question=[
"How many continents are there?", 
"What is the capital of India?",
"NG mei kaun se course padhaya jaata hai?"
]
option=[
["Four", "Nine", "Seven", "Eight"],
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution = [3,4,1]
i=0
while i<len(question):
    print("Q",i+1,question[i])
    j=0 
    while j<=len(option):
        print(j+1,option[i][j])
        j=j+1
    b=int(input("enter your choices:"))
    if b==solution[i]:
        print("yes")
    else:
        print("no")
        print("sorry try again")
        break
    print()
    i=i+1
    







      
      
       

     
   
    

      

