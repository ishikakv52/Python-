# 5️⃣ Search value by key
# User se key input lo.
# ➡️ Agar key present hai → uski value print karo
# ➡️ Nahi hai → "Key not found"

d={
    "Names":["A","B","C"],
    "Branch":["CS","IT","Civil"],
    "Rollno.":[10,20,30]
}

k=eval(input("Enter key : "))
if k in d:
    print(d.get(k))
else:
    print("Key not found")    
