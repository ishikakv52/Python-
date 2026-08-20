import random
color=["Red","Yellow","Green","Blue"]
comp=random.choice(color)
user=input("Enter your choice from RED,YELLOW,GREEN,BLUE : ")
print("Computer's choice : ",comp)

if user==comp:
    print("You win")
else:
    print("You lose")    
