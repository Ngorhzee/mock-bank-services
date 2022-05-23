
import random


def init():
    import login
    import register
    print("Welcome to ABN Bank")
    user_input=int(input("Do you have an account with us \n 1. YES\n 2.NO\n"))
    if user_input==1:
        login.login()
    elif user_input==2:
       register. kregister()
    else:
        print("Invalid option try again")
        init()  
    
def generateAccountNumber():
    return random.randrange(1111111111,9999999999)

def getBalance(userDetails):
    return userDetails[4] 
def setBalance(userDetails,balance):
    # userDetails=int(userDetails[4])
    userDetails[4]=balance

def accountNumberValidation(accountNumber):
    convert=int(accountNumber)
    if convert:
        if len(str(accountNumber))<10 or len(str(accountNumber))>10:
            print("Account number cannot be less than or greater than 10 digit")
    else:
        print("Account Numbers can only be digits")
        




    

       
#deposit(1125655637,100)  
init()
    