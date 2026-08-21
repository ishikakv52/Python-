x=[]
for i in range(5):
    print("Enter entities of the list")
    i=eval(input())
   

    if type(i)==str:
        print("String is not allowed")
        # break
      
    else:
        x.append(i)
        print(x)    
 
