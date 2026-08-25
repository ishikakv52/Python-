# 4️⃣ Count total elements
# Dictionary di hui hai.
# ➡️ len() use karke batao kitni key-value pairs hain
# ➡️ Agar zero ho → "No data found"

d={
    "Names":["A","B","C"],
    "Branch":["CS","IT","Civil"],
    "Rollno.":[10,20,30]
}
l=len(d)
if l==0:
    print("No data found")
else:
    print("Total number of key value pairs : ",l)    
