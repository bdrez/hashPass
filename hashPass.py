import hashlib
from collections import defaultdict
'''
 take in the username and pasword then hash the password to store for
first time user and then ask the user to enter the username and password and double check with the hash
'''

#create out dict that we will use to store email/password
#create out dict that we will use to store email/password
db=defaultdict(str)
db={'b@gmail.com': '202cb962ac59075b964b07152d234b70' }#test case


def user_status():
    #here we will see if its a first time user and were storing the data or if its an old user logging in 
    #maybe do something abt if they enter nonsense that doesnt start with y or n
    resp=input("Are you a new user? Enter yes or no ")
    while resp[0].lower()!='y' and resp[0].lower()!='n':
            resp=input("Invalid response. Enter yes for new user or no for exisiting account log in.")
            #resp=input("Are you a new user? ")
    if resp[0].lower()=='y' :
        #since were converting the response to .lower will be good no matter if they put upper or lower so only check once
        input_new_user()
    else :
        #can do else bec at the top we made sure only two possible answers here 
        verify_user()
        #OKAY THIS WORKS
        #print('input checking function')
    
        

def input_new_user():
    user_email =input("enter your email ") #do the string regex to make sure it ends in @gmail @email @yahoo etc .com
    #do something to make sure they cannot enter nothing-for both 
    if user_email in db:
        resp=input('Account already created. Enter yes to sign in and no to exit.')
        while resp[0].lower()!='y' and resp[0].lower()!='n':
                print("Invalid response. Enter yes to log in and no to leave.")
        if resp[0].lower()=='y' :
            verify_user()
        else:
            print("bye bye")
            return 
    user_pass=input("enter your password ")
    double_pass=input("please enter your password again to verify ")
    hashCheck(user_email, user_pass, double_pass)


def hashCheck(em, a, b):
    md5_pass1=hashlib.md5()
    md5_pass2=hashlib.md5()
    md5_pass1.update(a.encode()) #we need to encode to convert from string to byte so we can hash
    md5_pass2.update(b.encode())
    digest1=md5_pass1.hexdigest()
    digest2=md5_pass2.hexdigest()
    if digest1==digest2:
        #if the user enter the password correct both times we store in dict if its a new user/email wasnt used before 
        if em not in db:
            db[em]=digest1
            print("user entered into date base")
            print(db) #iterate over it to print better 
            #now give them the opportunity to log in 
            resp=input("Would you like to log in? Enter Y or N ")
            while resp[0].lower()!='y' and resp[0].lower()!='n':
                print("Invalid response. Enter yes to log in and no to leave.")
                resp=input("Are you a new user? ")
            if resp[0].lower()=='y' :
                verify_user()
            else:
                print("bye bye")
                # only be used inside of a loop break  
                return 

    else:
        print("passwords dont match") 
        input_new_user() #go back to allow them to enter new information?
    #loop back to reenter password?

def verify_user():
    user_email =input("enter your email ") 
    user_pass=input("enter your password ")
    #they enter username and password check if the email ad the hash of the password are in and match 
    md5_ver=hashlib.md5()
    md5_ver.update(user_pass.encode())
    hex_ver=md5_ver.hexdigest()
    flag=False #will use this to flag 
    for k, v in db.items(): #somethings wrong here
        if k==user_email and v==hex_ver:
            print("user logged in sucsesful")
            flag=True
        if k==user_email and v!=hex_ver:
            print("Password incorrect")
            flag=True
            input_new_user() #maybe make a new one so doesnt ask twice 
    if flag==False:
        print("User not found in system.")
        resp=input("Press y to create and account. Press n to exit program.")
        while resp[0].lower()!='y' and resp[0].lower()!='n':
            resp=input("Invalid response. Enter yes or no.")
        if resp[0].lower()=='y' :
            input_new_user()
        else :
            print("bye bye")
            return

user_status()

