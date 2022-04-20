
["How many continents are there?", 
"What is the capital of India?",
"NG mei kaun se course padhaya jaata hai?"
]
question=[
["Four", "Nine", "Seven", "Eight"],
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution = [3,4,1]

i=0
while i<len(question):
    print("Q",i+1,question[i])
    j=0 
    while j<(len(question)+1):
        print(j+1,question[i][j])
        j=j+1
    b=int(input("enter your choices:"))
    if b==solution[i]:
        print("correct")
    else:
        print("wrong")
        print("sorry try again")
        break
    print()
    i=i+1
    
    