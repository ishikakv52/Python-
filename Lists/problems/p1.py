x=[]
# y=int(input("Number of entities: "))
# for i in range(5):
#  print("Enter entities of the list")
#  i=eval(input())
#  x.append(i)
while True:
    print("Enter any entity to add in the list")
    n=eval(input())
    print(x)
    if len(x)<=4 :
        x.append(n)
        print(x)
    else:
        print("❌ Not applicable ❌")  
        break  




