import os
import re
link="data/users/"
def create(accountNumber,firstName,LastName,email,password,balance):
    try:
        f=open(link + str(accountNumber)+".txt","x")
        user_detail=firstName+","+LastName+","+email+","+password+","+str(balance)
        f.write(user_detail)
        f.close()
    except FileExistsError:
        f=open(link + str(accountNumber)+".txt","w+")
        user_detail=firstName+","+LastName+","+email+","+password+","+str(balance)
        f.write(user_detail)
        f.close()

def read(accountNumber):
    try:
        f=open(link + str(accountNumber)+".txt","r")
        return f.readline()
       
     #return True
    except:
        print("Account Not Found")
        return False
    
def delete(accountNumber):
    try:
        links=link + str(accountNumber)+".txt"
        os.path.exists(links)
        os.remove(links)
    except:
        print("Record Not Found")  

def authenticateUser(accountNumber,password):
    user=str.split(str(read(accountNumber)),",")
    #user=read(accountNumber)
    if password==user[3]:
         return True
    else:
        return False 
def update(accountNumber):
    # links=link + str(accountNumber)+".txt"
    # os.path.exists(links)
    # os.set
    f=open(link + str(accountNumber)+".txt","x")
         
authenticateUser(1125655637,12345)   