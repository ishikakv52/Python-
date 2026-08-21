x=[9,11,12]
i=int(input("enter index : "))
d=eval(input("enter data to insert : "))
if x[i]==d:
    print("Already exists at same index number✅")
else:
    x.insert(i,d)
    print(x)    
