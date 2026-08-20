import random
char="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvnbm0123456789#$@"
password=" "
for i in range(8):
    x=random.choice(char)
    password=password+x

print("Generated password : ",password)    
