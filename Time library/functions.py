import time
a=time.time()               #1970 (Epoch time) se ab tak ke seconds return karta hai(Float number hota hai)
print("time : ",a)


b=time.ctime()             #Current time ko readable format mein show karta hai
print("ctime : ",b)


print("Hello")
time.sleep()      #Program ko diye gaye seconds ke liye pause karta hai
print("Jaat Sahab")

d=time.localtime()    #Current time ko tuple format mein deta hai
print("Local time : ",d)

t = time.localtime()
print(time.strftime("%d-%m-%Y-%H:%M:%S", t))



print(time.gmtime())     #UTC (Greenwich) time return karta hai



