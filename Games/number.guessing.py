import random
x=random.randint(1,10)
# print("Our Result : ",x)

n=int(input("Enter guessed number between 1 and 10 : "))
if n==x:
    print("You win!🏆")
else:
    print("Game over❌")    
