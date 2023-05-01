import mysql.connector

connection = mysql.connector.connect(
    user= 'root', 
    database= 'bankc2c', 
    password= 'x770948Boolaid!', autocommit = True
    )

cursor = connection.cursor()
cursor = connection.cursor(buffered=True)

def make_account(acct, pin, startAmt):
    addAcc = (f'INSERT INTO bank_accounts (account, pin, money) VALUES ("{acct}", {pin}, {startAmt})')
    cursor.execute(addAcc)
    
def deposit(acct, pin, dep):
    #pull acc data from database
    
    cursor.execute(f'SELECT account FROM bank_accounts WHERE account = "{acct}"')
    account = cursor.fetchone()

    while(account == None):
        print('Not a real account. ')
        name = input('name of account? ')
        cursor.execute(f'SELECT account FROM bank_accounts WHERE account = "{name}"')
        account = cursor.fetchone() 
    
    cursor.execute(f'SELECT pin FROM bank_accounts WHERE account = "{account[0]}"')
    realPin = cursor.fetchone()
        
    cursor.execute(f'SELECT money FROM bank_accounts WHERE account = "{account[0]}"')
    curAmt = cursor.fetchone()
    
    addition = dep + curAmt[0]
        
    #check if entered pin match pin in data
    if(pin == realPin[0]):
        #add to current amt in bank depo
        query = (f'UPDATE bank_accounts SET money = {addition} WHERE account = "{account[0]}"')
        cursor.execute(query)
    else:
        print('Wrong pin or acct.')
            

def withdraw(acct, pin, amt):
    cursor.execute(f'SELECT account FROM bank_accounts WHERE account = "{acct}"')
    account = cursor.fetchone()

    while(account == None):
        print('Not a real account. ')
        name = input('name of account? ')
        cursor.execute(f'SELECT account FROM bank_accounts WHERE account = "{name}"')
        account = cursor.fetchone() 
    
    cursor.execute(f'SELECT pin FROM bank_accounts WHERE account = "{account[0]}"')
    realPin = cursor.fetchone()
        
    cursor.execute(f'SELECT money FROM bank_accounts WHERE account = "{account[0]}"')
    curAmt = cursor.fetchone()
    
    difference = curAmt[0] - amt
    
    if(pin == realPin[0] and difference >= 0):
        #subtract to current amt in bank
        query = (f'UPDATE bank_accounts SET money = {difference} WHERE account = "{account[0]}"')
        cursor.execute(query)
        
    elif((curAmt[0] - amt) < 0):
        print('Not enough money.')
    
    else:
        print('Wrong pin or acct.')

def edit_pin(acct, pin, newPin):
    cursor.execute(f'SELECT account FROM bank_accounts WHERE account = "{acct}"')
    account = cursor.fetchone()

    while(account == None):
        print('Not a real account. ')
        name = input('name of account? ')
        cursor.execute(f'SELECT account FROM bank_accounts WHERE account = "{name}"')
        account = cursor.fetchone() 
    
    cursor.execute(f'SELECT pin FROM bank_accounts WHERE account = "{account[0]}"')
    realPin = cursor.fetchone()
    
    if(pin == realPin[0]):
        query = (f'UPDATE bank_accounts SET pin = {newPin} WHERE account = "{account[0]}"')
        cursor.execute(query)
        
    else:
        print('Wrong pin or acct.')
        
'''
cursor.execute(f'SELECT account FROM bank_accounts WHERE account = "sdlkfjsdklf"')
account = cursor.fetchone()
if(account == None):
    print('Not a real account. ')
    
deposit('sldkjfsdlf',111,11)



addData = 'INSERT INTO bank_accounts (account, pin, money) VALUES ("bethany", 1234, 1)'
cursor.execute(addData)
'''
#gui
ans = input('Welcome, what would you like to do?\n make new account (new_acc) \n deposit (dep) \n withdraw (with)\n edit pin (edit)\n say STOP to end. \n')

while(ans.upper() != 'STOP' ):
    if ans.lower() == 'new_acc':
        #add restrictions on size of pin, name, and amt
        name = input('name? ')
        
        while(True):
            try:     
                pin = int(input('pin? '))

            except ValueError:
                print('Can only be positive numbers. ')
            
            if(len(str(pin)) > 4):
                print('Can only be 4 digits. ')
            
            else:
                if(isinstance(pin, int) and len(str(pin)) == 4):
                    break

        while(True):
            try:     
                amt = int(input('starting amount? '))

            except ValueError:
                print('Can only be positive numbers.')
            
            else:
                if(isinstance(amt, int)):
                    break
            
        make_account(name, pin, amt)
        
    elif ans.lower() == 'dep':
        name = input('name of account? ')
        
        while(True):
            try:     
                pin = int(input('pin? '))

            except ValueError:
                print('Can only be positive numbers.')
            
            else:
                if(isinstance(pin, int)):
                    break

        while(True):
            try:     
                amt = int(input('depositing how much? '))

            except ValueError:
                print('Can only be positive numbers.')
            
            else:
                if(isinstance(amt, int)):
                    break
                
        deposit(name, pin, amt)
        
    elif ans.lower() == 'with':
        name = input('name of account? ')
        
        while(True):
            try:     
                pin = int(input('pin? '))

            except ValueError:
                print('Can only be positive numbers.')
            
            else:
                if(isinstance(pin, int)):
                    break

        while(True):
            try:     
                amt = int(input('withdrawing how much? '))

            except ValueError:
                print('Can only be positive numbers.')
            
            else:
                if(isinstance(amt, int)):
                    break
        withdraw(name, pin, amt)
        
    elif ans.lower() == 'edit':
        #take in old pin to change to new pin
        name = input('name of account? ')
        while(True):
            try:     
                oldPin = int(input('old pin? '))

            except ValueError:
                print('Can only be positive numbers.')
            
            else:
                if(isinstance(oldPin, int)):
                    break

        while(True):
            try:     
                newPin = int(input('new pin? '))

            except ValueError:
                print('Can only be positive numbers.')
            
            else:
                if(isinstance(newPin, int)):
                    break

        edit_pin(name, oldPin, newPin)
        
    else:
        print('\nOnly use commands listed.\n')
        
    ans = input('Continue?\n make new account (new_acc) \n deposit (dep) \n withdraw (with)\n edit pin (edit)\n say STOP to end. \n')

connection.commit()
cursor.close()
connection.close()