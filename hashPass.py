import hashlib
from collections import defaultdict
'''
 take in the username and pasword then hash the password to store for
first time user and then ask the user to enter the username and password and double check with the hash
'''

def user_status():
    #here we will see if its a first time user and were storing the data or if its an old user logging in 
    #maybe do something abt if they enter nonsense that doesnt start with y or n
    resp=input("Are you a new user? Enter yes or no ")
    while resp[0].lower()!='y' and resp[0].lower()!='n':
            print("Invalid response. Enter yes or no.")
            resp=input("Are you a new user? ")
    if resp[0].lower()=='y' :
        #since were converting the response to .lower will be good no matter if they put upper or lower so only check once
        input_new_user()
    else :
        #can do else bec at the top we made sure only two possible answers here 
        #call checking function
        print('input checking function')
    
        

def input_new_user():
    user_email =input("enter your email ") #do the string regex to make sure it ends in @gmail @email @yahoo etc .com
    user_pass=input("enter your password ")
    double_pass=input("please enter your password again to verify ")
    hashCheck(user_email, user_pass, double_pass)


def hashCheck(em, a, b):
    #create out dict that we will use to store email/password
    db=defaultdict(str)
    md5_pass1=hashlib.md5()
    md5_pass2=hashlib.md5()
    md5_pass1.update(a.encode()) #we need to encode to convert from string to byte so we can hash
    md5_pass2.update(b.encode())
    digest1=md5_pass1.hexdigest()
    digest2=md5_pass2.hexdigest()
    if digest1==digest2:
        #if the user enter the password correct both times we store in dict if its a new user/email wasnt used before 
        if em not in db:
            db[em]=md5_pass1
            print("enter in date base")
            print(db)
    else:
        print("passwords dont match") 
        input_new_user() #go back to allow them to enter new information?
    #loop back to reenter password?

user_status()



