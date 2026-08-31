a=input("enter the string")
def forcount():
    d=input("Enter the word to be counted : ")
    if d in a:
        print("Found")
        z=a.count(d)
        print(z)
    else:
        print("Not found")    
forcount()        
