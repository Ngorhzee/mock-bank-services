import db
def bankOperation(accountNumber,user,users):
    import login
    print(f"Welcome {user} {users} ")
    selectedOption=int(input("What would you like to do today \n 1. WITHDRAWAL \n 2. DEPOSIT \n 3. LOGOUT \n 4.EXIT "))
    if selectedOption==1:
        withdrawal(accountNumber,amount=int(input("Enter Amount: \n")))
    elif selectedOption==2:
        deposit(accountNumber,amount=int(input("Enter Amount: \n")))
        
    elif selectedOption==3:
        login.login()
    elif selectedOption==4:
        exit()
    else:
        print("invalid option")
        bankOperation()
        
def withdrawal(accountNumber,amount):
    import auth
    user=str.split(str(db.read(accountNumber)),",")
    if int(user[4])>amount:
        balance=int(auth.getBalance(user))-amount
        currentBalance= auth.setBalance(user,balance)
        print(f"Your Account Balance is {user[4]}")
        db.create(accountNumber,user[0],user[1],user[2],user[3],user[4])
        return currentBalance
    else:
        #currentBalance= setBalance(user,balance)
        print("insufficient amount")
        print(f"Your Account Balance is {user[4]}")
        db.create(accountNumber,user[0],user[1],user[2],user[3],user[4])
        #return currentBalance
        
def deposit(accountNumber,amount):
    import auth
    user=str.split(str(db.read(accountNumber)),",")
    balance=int(auth.getBalance(user))+amount
    currentBalance= auth.setBalance(user,balance)
    db.create(accountNumber,user[0],user[1],user[2],user[3],user[4])
    print(f"Your Account Balance is {user[4]}")
    return currentBalance