# Dictionary already filled hai.
# User se input lo:

# 1 → dictionary clear karo

# 2 → dictionary ko as-it-is print karo

# Clear karne ke baad check karo:
# ➡️ Agar empty hai → "Dictionary is empty"
d={
    "Names":["A","B","C"],
    "Branch":["CS","IT","Civil"],
    "Rollno.":[10,20,30]
}

k=int(input("Press 1️⃣ to clear , 2️⃣ to print as it is : "))
if k==1:
    print("Clearing dictionary.......")
    d.clear()
    if d==dict():
        print("Dictionary is empty")
elif k==2:
    print("d : ",d)
else:
    print("Invalid input")            
