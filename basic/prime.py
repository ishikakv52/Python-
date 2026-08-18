def pr(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        return True
    else:
        return False  
def left_nearest(n):
    n=n-1
    while n>1:
        if pr(n):
            return n
        n=n-1
    return None    
def right_nearest(n):
    n=n+1
    while True:
        if pr(n):
            return n
        n=n+1


    

n=int(input("Enter Number : "))
x=pr(n)            
print("IsPrime : ",x)
print("Left nearest : ",left_nearest(n))
print("Right nearest : ",right_nearest(n))
# q=left_nearest()
# print(q)    



# find nearest left and right prime number of the entered