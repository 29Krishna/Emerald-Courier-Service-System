def create_account() :
    print('Enter your Details....\n')
    name=input('Enter Name:')
    email=input('Enter Email-id:')
    custrec=[name,email]
    custwriter.writerow(custrec)
    while True:
        username=input('Create Username:')
        cust1.execute('select USERNAME from login_customer where USERNAME="{}" '. format(username))
        if cust1.fetchone() is None:
            pwd=input('Create a STRONG Password:')
            while True:
                pwd1=input('Confirm Password:')
                if pwd==pwd1:
                    break
                else:
                    print("!! Password doesn't Match !!")
            cust1.execute("insert into login_customer values( '"+username+"', '"+pwd+"')")
            conn.commit()
            print('Account Successfully Created')
            print('Opening Courier Menu...\n\n')
            sleep(2)
            courier_menu()
        else:
            print("This username already exists!!")
            print("Please create a different username.")
            
def login_account() :
    username=input('Enter your Username:')
    pwd=input('Enter your Password:')
    if username[:5]=='STAFF':
        cust1.execute('select * from login_staff where USERNAME="{}" and PASSWORD="{}"  '. format(username,pwd) )
        if cust1.fetchone() is None:
            print('Incorrect Credentials')
            print('Please Try Again')
            login_account()
        else:
            print('Login Successful !!')
            print('Opening Staff Menu...\n\n')
            sleep(2)
            staff_menu()
    else:
        cust1.execute('select * from login_customer where USERNAME="{}" and PASSWORD="{}"  '. format(username,pwd) )
        if cust1.fetchone() is None:
            print('Incorrect Credentials')
            print('Please Try Again')
            login_account()
        else:
            print('Login Successful !!')
            print('Opening Menu...\n\n')
            sleep(2)
            courier_menu()

def courier_menu():
    print("WELCOME !!")
    print('1. Place Order')
    print('2. Existing Order Details')
    print('3. Check Status of Order')
    print('4. Modify Order')
    print('5. Billing Procedure')
    print('6. Exit')
    choice=int(input('Enter your choice:'))
    if choice==1:
        place_order()
    elif choice==2:
        existing_order()
    elif choice==3:
        check_status()
    elif choice==4:
        modify_order()
    elif choice==5:
        billing_procedure()
    elif choice==6:
        exit()
    else:
        print('!! Choice',choice,'is not valid....','Please enter valid choice !!\n')
        sleep(2)
        courier_menu()

def place_order() :
    print('COURIER ORDER')
    a=input("Sender's Name:")
    while True:
        b=int(input("Sender's Phone Number:"))
        if str(b).isdigit() and len(str(b)) ==10:
            break
        else:
            print('Phone Number not valid!!')
            print('Please enter a valid Number')
    c=input("Sender's Address:")
    d=input("Receiver's Name:")
    while True:
        e=int(input("Receiver's Phone Number:"))
        if str(e).isdigit() and len(str(e)) ==10:
            break
        else:
            print('Phone Number not valid!!')
    f=input("Receiver's Address:")
    ordrec=[a,b,c,d,e,f]
    ordwriter.writerow(ordrec)
    Confirmed=str('Confirmed')
    cust1.execute("insert into courier values('"+a+"','"+str(b)+"','"+c+"','"+d+"','"+str(e)+"','"+f+"','"+str(today)+"','"+str(currtime)+"','"+Confirmed+"')")
    conn.commit()
    print("Order from (",a,",",c,") to (",d,",",f,") has been placed on DATE:" ,today,", TIME:",currtime)
    print('Please note the above details')
    print('Returning to Menu...\n\n')
    sleep(2)
    courier_menu()

def existing_order():
    phone=input("Enter Sender's Phone Number:")
    cust1.execute('select* from courier where SENDER_PHONENO="{}" '. format(phone))
    order=cust1.fetchone()
    if order is None:
        print("There is no existing order on this Phone Number")
        print('Returning to menu...')
        sleep(2)
        courier_menu()
    else:
        for j in order:
            print(j)
        print('Returning to Menu...\n')
        sleep(2)
        courier_menu()
        
def billing_procedure() :
    print('Billing Procedures')
    cust1.execute('select * from bill')
    bill=cust1.fetchall()
    print('(WEIGHT_in_kgs, PRICE in Rupees)')
    for x in bill:
        print(x)
    print('Returning to Menu...\n')
    sleep(2)
    courier_menu()

def modify_order():
    sender_ph=input("Enter sender's phone number: ")
    cust1.execute('select* from courier where SENDER_PHONENO="{}" '. format(sender_ph))
    order=cust1.fetchone()
    if order is None:
        print("There is no existing order on this Phone Number")
        print('Returning to menu...\n')
        sleep(2)
        courier_menu()
    else:
        print('Select the detail field you want to chnage')
        print('1. SENDER NAME\n2. SENDER PHONE NO\n3. SENDER ADDRESS')
        print('4. RECEIVER NAME\n5. RECEIVER PHONE NO\n6. RECEIVER ADDRESS')
        lst=['SENDER_NAME','SENDER_PHONENO','SENDER_ADDRESS','RECEIVER_NAME','RECEIVER_PHONENO','RECEIVER_ADDRESS']
        choice=int(input("Enter your choice: "))
        field_change=lst[choice-1]
        new_field=input("Enter the details: ")
        cust1.execute("UPDATE courier set {}='{}' where SENDER_PHONENO='{}'". format(field_change,new_field,sender_ph))
        conn.commit()
        print("Order Updated!!")
        print('Returning to menu...\n')
        sleep(2)
        courier_menu()

def check_status():
    sender_phone=input("Enter Sender's Phone number:")
    cust1.execute('select ORDER_STATUS from courier where SENDER_PHONENO ="{}"'. format(sender_phone))
    order=cust1.fetchone()
    if order is None:
        print('No order is associated with this Phone Number.')
        print('Returning to Menu....\n')
        sleep(2)
        courier_menu()
    else:
        for i in order:
            print("Status of the order is : '",i,"'")
        print('Returing to Menu...\n')
        sleep(2)
        courier_menu()
    
def staff_menu():
    print('WELCOME !!')
    print('1.Existing Orders')
    print('2.Remove Order')
    print('3.Customer Details')
    print('4.Modify Current order details')
    print('5.Change Order Status')
    print('6.Exit')
    choice=int(input('Enter your choice:'))
    if choice==1:
        all_order()
    elif choice==2:
        remove_order()
    elif choice==3:
        customer_details()
    elif choice==4:
        modify_order()
    elif choice==5:
        change_status()
    elif choice==6:
        exit()
    else:
        print('!! Choice',choice,'is not valid....','Please enter valid choice !!\n')
        sleep(2)
        staff_menu()
        
def all_order() :
    cust1.execute('select * from courier')
    resultset=cust1.fetchall()
    if cust1.rowcount !=0:
        print('Order details are...')
        for x in resultset:
            print(x)
    else:
        print('There are no current orders...')
    
    print('Number of Pending Couriers are', cust1.rowcount)
    print('Returning to Menu...\n')
    sleep(2)
    staff_menu()

def remove_order():
    phone=input("Enter Sender's Phone Number which is to be removed:")
    cust1.execute('select * from courier where SENDER_PHONENO ="{}"'. format(phone))
    if cust1.fetchone() is None:
        print('No order is associated with this Phone Number.')
        print('Returning to Staff Menu....\n')
        sleep(2)
        staff_menu()
    else:
        cust1.execute('delete from courier where SENDER_PHONENO ="{}"'. format(phone))
        conn.commit()
        print("The order associated with Phone Number ",phone," has been removed.")
        print('Returing to Staff Menu...\n')
        sleep(2)
        staff_menu()

def customer_details() :
    print('CUSTOMER DETAILS ARE AS FOLLOWS: ')
    file3=open('Customer_Details.csv','r')
    custreader=csv.reader(file3)
    for i in custreader :
        print(i)
    print('Returning to Menu...\n')
    sleep(2)
    staff_menu()

def change_status():
    phone=input("Enter Sender's Phone Number whose order status has to be changed :")
    cust1.execute('select * from courier where SENDER_PHONENO ="{}"'. format(phone))
    if cust1.fetchone() is None:
        print('No order is associated with this Phone Number.')
        print('Returning to Staff Menu....\n')
        sleep(2)
        staff_menu()
    else:
        print("What do you want to change the status to?")
        print("1. Confirmed")
        print("2. Packed")
        print("3. Shipped")
        print("4. Out for Delievery")
        print("5. Delievered")
        print("6. Exit to Staff Menu")
        lst=['Confirmed','Packed','Shipped','Out for Delivery','Delievered']
        choice=int(input("Enter your choice:"))
        if choice==6:
            print("Returing to Staff Menu")
            sleep(2)
            staff_menu()
        elif choice >=7 :
            print("Please Enter a valid choice!!")
        else:
            status=lst[choice-1]
            cust1.execute("UPDATE courier set ORDER_STATUS='{}' where SENDER_PHONENO='{}'". format(status,phone))
            conn.commit()
            print("The status of order has been changed to '",status,"'")
            print('Returing to Staff Menu...\n')
            sleep(2)
            staff_menu()
    
def exit() :
    print('Thank you for using our services. :))')
    conn. close()
    file1. close()
    file2. close()
    sleep(2)
    


import mysql.connector as sql
import csv
from time import *
from datetime import date

today=date.today()
conn=sql.connect(host="localhost",user="root",passwd='sql12345', database="emerald_courier_service")
cust1=conn.cursor()

file1=open('Order_Details.csv','a+',newline='')
ordwriter=csv.writer(file1)

file2=open('Customer_Details.csv','a+',newline='')
custwriter=csv.writer(file2)

print("\t\t\t\tHi There!!")
print('\t\tWelcome to Emerald Courier Management System\n')

print("Your login time is :")
localtime=localtime()
currtime=strftime("%I: %M: %S %p",localtime)
print(currtime)

o=input("Press Enter to Continue\n")
print('1. Signup to create a new customer account')
print('2. Login to existing staff or customer account')
print("3. Exit")
while True:
    choose=int(input('Enter your choice:'))
    if choose==1:
        create_account()
        break
    elif choose==2:
        login_account()
        break
    elif choose==3:
        break
    else:
        print('Choice (',choose,')is invalid')
        