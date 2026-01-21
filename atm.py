# ATM Simulation Program
# This program simulates basic ATM operations using random library to generate otp
# Author: Ishika Rathi

import random
for i in range(100):
    
    amount=100000
    x=random.randrange(0000,9999)
    print("your OTP is : ",x)
    print("Press 1 for deposit,2 for withdrawl,3 for checking balance : ")
    OTP=int(input("Enter OTP : "))
    if OTP==x:
        print("OTP verified✅")
        k=int(input("Enter choice : "))
        if k==1:
            a=eval(input("Enter amount to deposit : "))
            amount=amount+a
            print("Total balance : ",amount) 
        elif k==2:
            a=eval(input("Enter amount to withdraw : "))
            if a>amount:
                print("❌Insufficient balance❌")
            else:
                amount=amount-a
                print("Withdraw amount : ",a)
                print("Total balance : ",amount)
               
        else:
            print("Total balance : ",amount)    
    else:
        print("Invalid OTP")         

   
