import random
while True:
    c=["rock","paper","scissor"]
    computer=random.choice(c)
    print("Enter stop to finish game")
    user=input("Enter your choice : ")
    if user=="stop":
        break
    
    else:
        print("Computer's choice : ",computer)
        if computer==user:
            print("Match Tie❌")
        elif user=="rock" and computer=="scissor":
            print("You win")
        elif user=="paper" and computer=="rock":
            print("You win")
        elif user=="scissor" and computer=="paper" :
            print("You win") 
        else:
            print("Computer win")         
