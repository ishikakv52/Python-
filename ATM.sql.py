import mysql.connector
import datetime
# MySQL se connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jaat@2010",
    database="da"
)

cursor = con.cursor() 
cursor.execute("create table passbook(id int,Amount float,Debit float,Credit float,t varchar(220))")
amount=1000000
id=input("Account no :")
k=int(input("Press 1 for deposit,2 for withdrawl,3 for checking balance : "))
def deposit():
    a=eval(input("Enter amount to deposit :"))
    o=a+amount
    debit=0
    credit=a
    #to create file
    x=str(id)
    file=x
    f=open(file+".txt","a")
    a=str(o)
    d=str(debit)
    c=str(credit)
    f.write("ID:"+x+"\nTotal Amount "+a+"\nDebit : "+d+"\nCredit : "+c)           
    it=datetime.datetime.now()      
    t=str(it)      
        # To insert in table of SQL 
    sql='''insert into passbook 
    values(%s,%s,%s,%s,%s)'''
    values=(id,o,debit,credit,it)
    cursor.execute(sql,values)
    con.commit()
    print("Data inserted successfully✅")   
def withdrawl():
        a=eval(input("Enter amount to withdraw :"))
        if a>amount:
              print("Insufficient balance")
        else:
              o=amount-a
              debit=a
              credit=0
        it=datetime.datetime.now()      
        t=str(it)      
        #to create file
        x=str(id)
        file=x
        f=open(file+".txt","a")
        a=str(o)
        d=str(debit)
        c=str(credit)
        f.write("ID:"+x+"\nTotal Amount "+a+"\nDebit : "+d+"\nCredit : "+c)                 
         # To insert in table of SQL 
        sql='''insert into passbook 
        values(%s,%s,%s,%s,%s)'''
        values=(id,o,debit,credit,it)
        cursor.execute(sql,values)
        con.commit()
        print("Data inserted successfully✅")      
def checkbalance():
        print("Total amount : ",amount)   
        debit=0
        credit=0
        it=datetime.datetime.now()      
        t=str(it)      
        #to create file
        x=str(id)
        file=x
        f=open(file+".txt","a")
        a=str(amount)
        d=str(debit)
        c=str(credit)
        f.write("ID:"+x+"\nTotal Amount "+a+"\nDebit : "+d+"\nCredit : "+c)           
         # To insert in table of SQL 
        sql='''insert into passbook 
        values(%s,%s,%s,%s,%s)'''
        values=(id,amount,debit,credit,it)
        cursor.execute(sql,values)
        con.commit()
        print("Data inserted successfully✅")   
if k==1:
    deposit()
elif k==2:
      withdrawl()
elif k==3:
      checkbalance()
else:
      print("Invalid input")                
