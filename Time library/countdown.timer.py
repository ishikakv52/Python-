import time 
sec=int(input("Enter seconds : "))
while sec>0:
    print("Time left : ",sec)
    time.sleep(1)
    sec=sec-1
print("Time's Up")    
