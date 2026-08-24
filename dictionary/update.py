Records={
    "Names":["Rathi","Choudhary","Jaat"],
    "Branch":["CS","IT","Civil"],
    "Rollno.":[10,20,30]

}

print("Before update : ",Records)
k=eval(input("Enter key : "))
v=eval(input("Enter the value"))
Records.update({k:v})
print("After update : ",Records)
