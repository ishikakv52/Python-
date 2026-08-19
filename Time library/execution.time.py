import time
#to find execution time of program
start=time.time()
for i in range(5):
    print(i)
    time.sleep(1)
end=time.time()
print("Execution time : ",start-end)    
