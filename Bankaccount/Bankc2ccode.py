import mysql.connector

connection = mysql.connector.connect(
    user= 'root', 
    database= 'bankc2c', 
    password= 'x770948Boolaid!', autocommit = True
    )

cursor = connection.cursor()

def make_account(acctType, pin, startAmt):
    addAcc = (f'INSERT INTO bank_accounts (account, pin, money) VALUES ({acctType}, {pin}, {startAmt})')
    cursor.execute(addAcc)
    
def deposit(acct, pin, dep):
    #pull acc data from database
    realPin = (f"SELECT pin FROM bank_accounts WHERE account = {acct}") 
    curAmt = (f"SELECT money FROM bank_accounts WHERE account = {acct}") 
    
    #check if entered pin match pin in data
    if(pin == realPin):
        #add to current amt in bank depo
        query = (f'UPDATE bank_account SET money = {dep + curAmt} WHERE account = {acct}')
        cursor.execute(query)
    else:
        print("wrong pin!")

def withdraw(acct, pin, amt):
    realPin = (f"SELECT pin FROM bank_accounts WHERE account = {acct}") 
    curAmt = (f"SELECT money FROM bank_accounts WHERE account = {acct}")
    
    if(pin == realPin & (curAmt - amt) > 0):
        #add to current amt in bank depo
        query = (f'UPDATE bank_account SET money = {curAmt - amt} WHERE account = {acct}')
        cursor.execute(query)
        
    elif((curAmt - amt) < 0):
        print('Not enough money.')

def edit_pin(newPin, acct, pin):
    realPin = (f"SELECT pin FROM bank_accounts WHERE account = {acct}")
    
    if(pin == realPin):
        query = (f'UPDATE bank_account SET pin = {newPin} WHERE account = {acct}')

#make_account('beth', 1234, 100)
addData = ('INSERT INTO bank_accounts (account, pin, money) VALUES ("beth", 7, 11)')

cursor.execute(addData)

#gui
ans = input('Welcome, what would you like to do?\n make new account (new_acc) \n deposit (dep) \n withdraw (wd)\n edit pin (edit)\n')

if ans == 'new_acc':
    #add restrictions on size of pin, name, and amt
    name = input('name?')
    pin = input('pin?')
    amt = input('starting amount?')
    make_account(name, pin, amt)
    
elif ans == 'dep':
    name = input('name of account?')
    pin = input('pin?')
    amt = input("depositing how much?")
    #check if pin and acc match in database

"""   
elif ans == 'with':
    #check if pin and acc match in database
elif ans == 'edit':
    #take in old pin
    #check if pin and acc match in database
    #change old pin to new pin
else:
    print('Only use commands listed')
"""
connection.commit()
cursor.close()
connection.close()