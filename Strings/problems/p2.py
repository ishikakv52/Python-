a=input("Enter the string : ")
def forupper():
    
    if a.isupper():
        print("Already in upper case")
    else:
        x=a.upper()
        print("In Upper case : ",x)    

def forlower():
    if a.islower():
        print("Already in lowercase")
    else:
        x=a.lower()
        print(x)      

def forsearch():
    s=input("Enter word to search : ")
    if s in a:
        print("Exist")
        i=a.index(s)
        print(i)
    else:
       print("No exist")            
