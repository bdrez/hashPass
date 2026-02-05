import hashlib
from regexRegulator import email_ending
'''
use a struct or a dict with key values maybe take in the username and pasword then hash the password to store for
first time user and then ask the user to enter the username and password and double check with the hash
so enter a user name and store enter a password hash and store hash ask to double check password and hash and double 
check then once in system user can enter infroamtion check if the hash they enter matches and log in
'''

#maybe make one function to check them
#change the hash from md5 to a more secure verison 

#create out dict that we will use to store email/password
db={'b@gmail.com': 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3' }#test case
#{'b@gmail.com': '202cb962ac59075b964b07152d234b70', 'a@gmail.com': 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'}


def user_status():
    #here we will see if its a first time user and were storing the data or if its an old user logging in 
    #maybe do something abt if they enter nonsense that doesnt start with y or n
    resp=input("Are you a new user? Enter yes or no: ")
    while resp[0].lower()!='y' and resp[0].lower()!='n':
            resp=input("Invalid response. Enter yes for new user or no to log into an existing account: ")
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
    user_email =input("Enter your email: ") 
    em_flag=False #flag set to check the email
    em_flag=email_ending(user_email)#REGEX IMPORTED FUNCTION FROM REGEXREGULATOR
    while em_flag==False:
        print("Invalid email address! ")
        user_email =input("Enter your email: ")
        em_flag=email_ending(user_email)
    #do something to make sure they cannot enter nothing-for both 
    if user_email in db:
        resp=input('Account already created. Enter yes to sign in and no to exit: ')
        while resp[0].lower()!='y' and resp[0].lower()!='n':
                print("Invalid response. Enter yes to log in and no to leave: ")
        if resp[0].lower()=='y' :
            verify_user()
        else:
            print("Bye Bye!")
            return 
    user_pass=input("Enter your password: ")
    double_pass=input("Please enter your password again to verify: ")
    hashCheck(user_email, user_pass, double_pass)


def hashCheck(em, a, b):
    sha_pass1=hashlib.sha256()
    sha_pass2=hashlib.sha256()
    sha_pass1.update(a.encode()) #we need to encode to convert from string to byte so we can hash
    sha_pass2.update(b.encode())
    digest1=sha_pass1.hexdigest()
    digest2=sha_pass2.hexdigest()
    
    if digest1==digest2:
        #if the user enter the password correct both times we store in dict if its a new user/email wasnt used before 
        if em not in db:
            db[em]=digest1
            print("User entered into date base.")
            print(db) #iterate over it to print better 
            #now give them the opportunity to log in 
            resp=input("Would you like to log in? Enter yes or no: ")
            while resp[0].lower()!='y' and resp[0].lower()!='n':
                print("Invalid response. Enter yes to log in and no to leave: ")
                resp=input("Are you a new user? ")
            if resp[0].lower()=='y' :
                verify_user()
            else:
                print("Bye Bye!")
                # only be used inside of a loop break  
                return 

    else:
        print("Password does not match!") 
        input_new_user() #go back to allow them to enter new information?
    #loop back to reenter password?

def verify_user():
    user_email =input("enter your email ")
    login_atempt=5
    #flag=False #will use this to flag 
    em_flag=False
    em_flag=email_ending(user_email)#REGEX IMPORTED FUNCTION FROM REGEXREGULATOR
    while em_flag==False:
         print("Invalid email address ")
         user_email =input("enter your email ")
         em_flag=email_ending(user_email)

    #once we check if its a legal email address we need to even check if it exist before we ask for password
    if user_email not in db:
            print("User not found in system")
            resp=input("Press y to create and account. Press n to exit program: ")
            while resp[0].lower()!='y' and resp[0].lower()!='n':
                resp=input("Invalid response. Enter yes or no.")
            if resp[0].lower()=='y' :
                input_new_user()
            else :
                print("bye bye")
                return
    while login_atempt>0: #still have tries left 
        user_pass=input("enter your password ")
    #they enter username and password check if the email and the hash of the password are in and match 
        sha_ver=hashlib.sha256()
        sha_ver.update(user_pass.encode())
        hex_ver=sha_ver.hexdigest()
        #now that we know the user exists we dont have to loop through dictionary
        #we can just check if thats the value
        if db[user_email]==hex_ver: # if teh dictionary key of the input users email euqals the value/password entered
            print("user logged in successful")
            return
        elif db[user_email]!=hex_ver:
            if login_atempt>0:
                login_atempt-=1
                print("Password incorrect.")
                #here ask again for password and check password with 
                    #flag=True
                    
    print("Too many log in attempts!")
    print("Bye, bye!")
    return

user_status()
