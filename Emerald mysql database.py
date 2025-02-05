import mysql.connector as sql
from time import sleep
import csv
a=input('Enter MySQL Password:')
conn= sql.connect(host="localhost",user="root",passwd=a)
print('Creating. . . ')
sleep(1)
print('Almost there. . . .')
sleep(1)


cursor=conn.cursor()

#dropping database if already exists
cursor.execute("DROP DATABASE IF EXISTS Emerald_Courier_Service")

#creating database
cursor.execute("CREATE DATABASE Emerald_Courier_Service")

#creating tables
cursor.execute("use Emerald_Courier_Service")

cursor.execute("create table courier (SENDER_NAME varchar(100), SENDER_PHONENO char(10), SENDER_ADDRESS varchar(50), RECEIVER_NAME varchar(20), RECEIVER_PHONENO char(10), RECEIVER_ADDRESS varchar(50), ORDER_DATE varchar(50), ORDER_TIME varchar(50), ORDER_STATUS varchar(50)) ")

cursor.execute("create table bill (WEIGHT_in_kgs varchar(100), PRICE varchar(100) ) ")

cursor.execute("create table login_customer(USERNAME varchar(100), PASSWORD varchar(100)) ")

cursor.execute("create table login_staff(USERNAME varchar(100), PASSWORD varchar (100)) ")

#inserting some initial values in courier
cursor.execute("insert into courier values('Krishna','7011143358','sarojini nagar','divya','9268706808','laxmi bai nagar','2022-01-16','04: 24: 34 PM','Delivered')")
conn.commit()

cursor.execute("insert into courier values('Rahul','9311880612','navy house','Prabhat','8929475761','hudco place','2022-01-20','05: 54: 10 PM','Delivered')")
conn.commit()

cursor.execute("insert into courier values('Nikhil ','9422549931','palam','nikhil punia','8108434441','tihar jail','2022-01-21','08: 18: 34 AM','Delivered')")
conn.commit()

cursor.execute("insert into courier values('Pranav','8743869914','shankar vihar','priyanshu','8547744357','haryana','2022-01-31','10: 26: 47 AM','Delivered')")
conn.commit()

cursor.execute("insert into courier values('Bittu','8448815639','chanakyapuri','arohi','9869691721','satya marg','2022-02-03','07: 36: 03 PM','Delivered')")
conn.commit()

#inserting some initial values in bill
cursor.execute("insert into bill values('less than 10','200.0/-')")
conn.commit()

cursor.execute("insert into bill values('10-20','500.0/-')")
conn.commit()

cursor.execute("insert into bill values('20-30','1000.0/-')")
conn.commit()

cursor.execute("insert into bill values('30-40','1500.0/-')")
conn.commit()

cursor.execute("insert into bill values('40-50','2000.0/-')")
conn.commit()

cursor.execute("insert into bill values('50-60','2500.0/-')")
conn.commit()

cursor.execute("insert into bill values('60-70','3000.0/-')")
conn.commit()

cursor.execute("insert into bill values('70-80','3500.0/-')")
conn.commit()

cursor.execute("insert into bill values('80-90','4000.0/-')")
conn.commit()

cursor.execute("insert into bill values('90-100','5000.0/-')")
conn.commit()

#inserting some initial values in login_customer
cursor.execute("insert into login_customer values('Krishna','2903')")
conn.commit()

cursor.execute("insert into login_customer values('Rahul','2803')")
conn.commit()

cursor.execute("insert into login_customer values('Nikhil','1710')")
conn.commit()

cursor.execute("insert into login_customer values('Pranav','2203')")
conn.commit()

cursor.execute("insert into login_customer values('Bittu','0411')")
conn.commit()

#inserting some initial values in login_staff
cursor.execute("insert into login_staff values('STAFF1','staff@111')")
conn.commit()

cursor.execute("insert into login_staff values('STAFF2','staff@222')")
conn.commit()

cursor.execute("insert into login_staff values('STAFF3','staff@333')")
conn.commit()

cursor.execute("insert into login_staff values('STAFF4','staff@444')")
conn.commit()

cursor.execute("insert into login_staff values('STAFF5','staff@555')")
conn.commit()

#entering some initial values in the customer_details csv file
file1=open('Customer_Details.csv','w',newline='')
custwriter=csv.writer(file1)
custwriter.writerow(["CUSTOMER NAME","CUSTOMER EMAIL"])

custrec=[['Krishna','krishna2903@gmail.com'],
         ['Rahul','rahul2803@gmail.com'],
         ['Nikhil','nikhil1710@gmail.com'],
         ['Pranav','pranav2203@gmail.com'],
         ['Bittu','bittu0411@gmail.com']]
custwriter.writerows(custrec)

#entering some initial values in the order_details csv file
file2=open('Order_Details.csv', 'w',newline='')
ordwriter=csv.writer(file2)
ordwriter.writerow(["SENDER NAME","SENDER PHONE NO","SENDER ADDRESS","RECEIVER NAME","RECEIVER PHONE NO","RECEIVER ADDRESS"])

ordrec=[['Krishna','7011143358','sarojini nagar','divya','9268706808','laxmi bai nagar'],
        ['Rahul','9311880612','navy house','Prabhat','8929475761','hudco place'],
        ['Nikhil ','9422549931','palam','nikhil punia','8108434441','tihar jail'],
        ['Pranav','8743869914','shankar vihar','priyanshu','8547744357','haryana'],
        ['Bittu','8448815639','chanakyapuri','arohi','9869691721','satya marg']]
ordwriter.writerows(ordrec)


file1.close()
file2.close()

print("Successfully Added all Tables and Values")
