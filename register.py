def kregister():
    import auth
    import login
    import db
    firstName=input("*** FIRST NAME ***\n")
    lastName= input("*** LAST NAME ***\n")
    email=input("*** EMAIL ADDRESS ***\n")
    password=input("*** PASSWORD ***\n")
    balance=0
    accountNumber=auth.generateAccountNumber()
    
    balanceOption=int(input("Do you wish to deposit any Amount? \n 1.Yes\n 2.No \n"))
    if balanceOption==1:
          amount=int(input("Enter Amount: "))
          balance=amount
       
    elif balanceOption==2:
        balance
    db.create(accountNumber,firstName,lastName,email,password,balance)
    print(f"Thank you for Registering with us\n Your Account Number is: {accountNumber}")
    print("You can now login")
    login.login()