username=["Ishika","Rathi","Choudhary","A"]
password=[123,456,789,233]
u=eval(input("Enter username : "))
p=eval(input("Enter password : "))
if u in username:
    print("Username matched✅")
    if p in password:
        print("Login successful✅")
    else:
        print("Password not matched❌")    
else:
    print("Username not exist❌")   
           
