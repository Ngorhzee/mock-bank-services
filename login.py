def login():
    import db
    import bankOperations
    print("*** login ***")
    accountNumber=input(" Enter Your Account Number \n")
    db.accountNumberValidation(accountNumber)
    if db.read(accountNumber):
        password=input("Password \n")
        if db.authenticateUser(accountNumber,password):
            user=str.split(str(db.read(accountNumber)),",")
            bankOperations.bankOperation(accountNumber,user[0],user[1])
        else:
            print("wrong Password")
    else:
        print("You do not have an Account with us please Register")