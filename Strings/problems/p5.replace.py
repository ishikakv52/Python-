def forreplace():
    a=input("Enter the complete string: ")
    c=input("Enter the old word : ")
    if c in a:
        print("Found")
        d=input("Enter the new word : ")
        b=a.replace(c,d)      
        print(b) 

    else:
        print("Word not found")    
forreplace()        
