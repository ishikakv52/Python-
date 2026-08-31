a='''I am Ishika Rathi
Currently doing my graduation in IMR college'''

s=input("Enter word which you want to search :")

if s not in a :
    print("Not found")  
    

else:
    
     print("Exist")
     x=0
     for i in a: 
         x=x+1
         if i is s[0]:
            
        #  if x is s[0:]:


            print(x)
            break
           
