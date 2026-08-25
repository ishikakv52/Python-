Records={
    "Names":["A","B","C"],
    "Branch":["CS","IT","Civil"],
    "Rollno.":[10,20,30]

}
d=eval(input("Enter key : "))

if d in Records:
    print("Key found✅")
    g=Records.get(d)
    print(g)
else:
    print("Key not found❌")    


