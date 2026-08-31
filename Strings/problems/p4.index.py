a='''I am Ishika Rathi
Currently doing my graduation in IMR college'''
s=input("Enter word to search : ")
if s in a:
    print("Exist")
    i=a.index(s)
    print(i)
else:
    print("No exist")    
