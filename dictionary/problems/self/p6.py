# 6️⃣ Delete key safely

# User se key lo.
# ➡️ Agar key exist karti hai → delete karo
# ➡️ Nahi karti → error ke bina message print karo

d={
    "Names":["A","B","C"],
    "Branch":["CS","IT","Civil"],
    "Rollno.":[10,20,30]
}
k=input("Enter key : ")
if k in d:
    print("Key found deleting it")
    d.pop(k)
    print("New dictionary : ",d)
else:
    print("Key not found")    
