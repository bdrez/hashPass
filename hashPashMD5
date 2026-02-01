import hashlib
from collections import defaultdict
from regexRegulator import email_ending
'''
 take in the username and pasword then hash the password to store for
first time user and then ask the user to enter the username and password and double check with the hash
'''

#maybe make one function to check them
#change the hash from md5 to a more secure verison 

#create out dict that we will use to store email/password
db=defaultdict(str)
db={'b@gmail.com': '202cb962ac59075b964b07152d234b70' }#test case


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
    pass_Atempt=3 #number of times they can try to log in with incorrect passw0rd
    user_email =input("Enter your email: ")
    em_flag=False
    em_flag=email_ending(user_email)#REGEX IMPORTED FUNCTION FROM REGEXREGULATOR
    while em_flag==False:
         print("Invalid email address! ")
         user_email =input("Enter your email: ")
         em_flag=email_ending(user_email)
    pass_flag=False #set this to ensure dont have unlimited password attempts 
    while pass_flag==False:
        user_pass=input("Enter your password: ")
    #they enter username and password check if the email ad the hash of the password are in and match 
        md5_ver=hashlib.md5() #hash object
        md5_ver.update(user_pass.encode()) #we update it and send the password the user enter to hash it 
        hex_ver=md5_ver.hexdigest() #and then we get the hexidigest of that hash
    flag=False #will use this to flag 
    for k, v in db.items(): #somethings wrong here
    #error bec we are iterating over a dictionary that changes sizes
        if k==user_email and v==hex_ver:
            print("User successfully logged in! ")
            flag=True
        if k==user_email and v!=hex_ver:
            pass_Atempt-=1 #counting down once 0 log out
            print("Password is incorrect! ")
            flag=True
            if pass_Atempt>0:
                verify_user() #maybe make a new one so doesnt ask twice 
            else:
                print("Bye Bye!")
                return  
    if flag==False:
        print("User not found in system. ")
        resp=input("Press yes to create and account. Press no to exit the program: ")
        while resp[0].lower()!='y' and resp[0].lower()!='n':
            resp=input("Invalid response. Enter yes or no:")
        if resp[0].lower()=='y' :
            input_new_user()
        else :
            print("Bye Bye!")
            return

user_status()
