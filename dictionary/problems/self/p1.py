# User se key aur value input lo.
# ➡️ Agar key pehle se exist karti hai, to value update karo
# ➡️ Agar exist nahi karti, to new key-value add karo
d={
    "name": "Ishika", 
   "age": 20
   }
k=eval(input("Enter key : "))
v=eval(input("Enter value : "))
if k in d:
    print("Key already exists but we are updating value.......")
    d.update({k:v})
    print("New dictionary is : ",d)
else:
    print("Key doesn't exists, we are making new key to add value ")    
    d.update({k:v})
    print("New dictionary : ",d)
