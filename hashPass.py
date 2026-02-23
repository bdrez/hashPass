import hashlib
from regexRegulator import email_ending
import getpass
'''
 take in the username and pasword then hash the password to store for
first time user and then ask the user to enter the username and password and double check with the hash
'''

#create out dict that we will use to store email/password
db={'b@gmail.com': 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3' }#test case
#{'b@gmail.com': '202cb962ac59075b964b07152d234b70', 'a@gmail.com': 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'}
print("Welcome!")

def user_status():
    #give a menu option 
    #show welcoming message and menu 
    while True:
        print("\nEnter the number to choose an option: \n")
        resp=input("1) Create account \n2) Login  \n3) Exit\n")
        if resp=="1" or resp=="2" or resp=="3":
            #valid response break out
            out=menu_choice(resp)
            if out==False: #we get from choosing option 3
                break
        else:
            print('Invalid response please enter a number! ')

def menu_choice(resp):
    if resp=="1":
        input_new_user()
    elif resp=="2":
        verify_user()
    elif resp=="3":
        print("Bye, bye!")
        return False
    else:
        print("Invalid response")
        #should not get here
       
def hasher(a): #create a fucntion to hash
    sha_pass=hashlib.sha256()
    sha_pass.update(a.encode()) #we need to encode to convert from string to byte so we can hash
    digest=sha_pass.hexdigest()
    return digest

def input_new_user():
    user_email =input("Enter your email: ") 
    em_flag=email_ending(user_email)#REGEX IMPORTED FUNCTION FROM REGEXREGULATOR
    while em_flag==False:
        print("Invalid email address! ")
        user_email =input("Enter your email: ")
        em_flag=email_ending(user_email)
    #do something to make sure they cannot enter nothing-for both 
    if user_email in db:
        resp=input('Account already created. Enter yes to sign in and no to exit: ')
        
        while not resp or resp[0].lower() not in ("y","n"):
            resp=input("Invalid response. Enter yes to log in and no to leave: ")
            if resp[0].lower()=='y' :
                verify_user()
                return #do this to get rid of bug if they press yes new account but enter exisiting email
            else:
                print("Bye Bye!")
                return 
    user_pass = getpass.getpass("Enter Password: ")
    #user_pass=input("Enter your password: ")
    double_pass = getpass.getpass("Password: ")
    #double_pass=input("Please enter your password again to verify: ")
    #we are going to check if the password match before we pass it on and hash them
    #checking the plain text veirison
    while user_pass!=double_pass:
        print("Password does not match!")
        user_pass = getpass.getpass("Enter Password: ")
        double_pass = getpass.getpass("Password: ")

    register_User(user_email, user_pass)


def register_User(em,a):
    #get the hash of user_pass/a
    digest=hasher(a)
   
    #if the user enter the password correct both times we store in dict if its a new user/email wasnt used before 
    if em not in db:
        db[em]=digest
        print("User entered into datebase.")
        #print(db) print db for testing
            #now give them the opportunity to log in 
        resp=input("Would you like to log in? Enter yes or no: ")
        #so were gonna check if the string exist if "" aka press enter the string is False
        while not resp or resp[0].lower() not in ("y", "n"): #so here where checking if nots true (false/doesnt exist) or didnt enter Y/N
            print("Invalid response. Enter yes to log in and no to leave: ")
            resp=input("Are you a new user? ")
        if resp[0].lower()=='y' :
            verify_user()
        else:
            print("Bye Bye!")
            # only be used inside of a loop break  
            return  

def verify_user():
    user_email =input("enter your email ")
    login_attempt=5
    em_flag=email_ending(user_email)#REGEX IMPORTED FUNCTION FROM REGEXREGULATOR
    while em_flag==False:
         print("Invalid email address ")
         user_email =input("enter your email ")
         em_flag=email_ending(user_email)

    #once we check if its a legal email address we need to even check if it exist before we ask for password
    if user_email not in db:
            print("Invalid login!")
            #dont tell them what the issue is - more secure
            resp=input("Press y to create and account. Press n to exit program: ")
            while not resp or resp[0].lower() not in ("y", "n"):
                resp=input("Invalid response. Enter yes or no.")
            if resp[0].lower()=='y' :
                input_new_user()
            else :
                print("bye bye")
                return
    while login_attempt>0: #still have tries left 
        user_pass=getpass.getpass("enter your password ")
    #they enter username and password check if the email and the hash of the password are in and match 
        #go get the hash of user_pass
        hex_ver=hasher(user_pass)
        #now that we know the user exists we dont have to loop through dictionary
        #we can just check if thats the value
        if db[user_email]==hex_ver: # if teh dictionary key of the input users email euqals the value/password entered
            print("user logged in successful")
            return
        elif db[user_email]!=hex_ver:
            login_attempt-=1
            print("Password incorrect.")
                    
    print("Too many log in attempts!")
    print("Bye, bye!")
    return

user_status()