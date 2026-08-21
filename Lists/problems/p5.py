marks=(10,11,12,13)
l=list(marks)
x=eval(input("Enter the data which u want to update : "))
if x not in marks:
    print("Data not found!❌")
else:
    print("Data found!✅") 
    i=l.index(x)
    l.remove(x)
    d=eval(input("Enter data to insert : "))
    l.insert(i,d)  
print(l)    

marks=tuple(l)
print(marks)
