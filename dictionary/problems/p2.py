c=eval(input("Press 1 for update,2 for clear : "))
x={
    "Name":"Ishika"
    }
if c==1:
    k=eval(input("Enter key : "))
    v=eval(input("Enter the value"))
    x.update({k:v})
    print("New updated dictionary : ",x)
elif c==2:
    x.clear()

    if len(x)==0:  
        print("There is no data in dictionary")
    else :
       print("X:",x)
else:
    print("Invalid choice")





