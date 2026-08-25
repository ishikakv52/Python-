# User se key input lo.
# ➡️ Agar key dictionary me already hai → "Key already exists" print karo
# ➡️ Nahi hai → add karo

d={
    "name":"Ishika",
    "rollno.":38
}
k=input("Enter key : ")
v=input("Enter value: ")
if k in d:
    print("Key already exists")
else:
    d.update({k:v}) 
    print("New dictionary : ",d)   
