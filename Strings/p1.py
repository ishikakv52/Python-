x=("A","B","C","D","E")
y=list(x)
# i=int(input("Enter the index number : "))
while True:
    k=int(input("Press 0 to stop,1 to enter name : "))
    if k==0:
        break
    else:   
        a=eval(input("Enter name  : "))
        if a in y:
                print("Already exists")
        else:
                # i=y.index(a)
                # y.remove(a)
                d=eval(input("Enter the data : "))
                y.append(d)
        x=tuple(y)
        print(x)
    
