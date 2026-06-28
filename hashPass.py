import hashlib
import getpass #to block the keys the user enters when typing in a password
import secrets #to help generate salt
from regexRegulator import email_ending #import to ensure they enter an email
from passwordRules import pssWrd
import sqlite3

#create out dict that we will use to store email/password
'''db={ }#test case
#{'b@gmail.com': '202cb962ac59075b964b07152d234b70', 'a@gmail.com': 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'}
print("Welcome!")
#opening to read it, we dont need to write r just makes it more clear 
for line in open('hashPassdb.txt'):
    #we need to loop to get everything
    em_word,em_salt,em_hash=line.strip().split() #were striping any access space and splitting by a space
    db[em_word]=(em_salt, em_hash)
print("transfer complete")

#build the dictionary here - open the db file and store it into dictionary so we have o(n) search '''

#creating our db and opening a connection to it 
con=sqlite3.connect("hashPass.db")

#creating a cusor to move around our db
curs=con.cursor()

#creating our db table user and the column names flexible typing no declartion
#created it once dont need to recreate it each time
#curs.execute("CREATE TABLE user(email, salt, hash)")

#set up test data 
#curs.execute("""
    #INSERT INTO user VALUES
   # ('b@gmail.com', 'b31b8737a83b3aaffab511ae58c281d7', '2f2627c998d2b6e341b29bbf4d1b936e774b5e6d0b45724b582bc435391f1346')
#""")

#commit change to db to be saved
con.commit()

#see if the info went in the db
#print(resul.fetchall())

#add account lock out timer

def user_status(): 
    
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
        print("Bye!")
        return False
    else:
        #need a way to get out of her if they decide 
        print("Invalid response")
        #should not get here

def salter(): #create a function to add salt to password
    salt=secrets.token_bytes(16)
    return salt

def hasher(password, salt): #create a fucntion to hash
    #we need to encode the password to convert from string to bytes for hashing
    sha_pass=hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    #we need to encode to convert from string to byte so we can hash
    return sha_pass.hex() #return the hexadecimal verision

def input_new_user():
    user_email =input("Enter your email: ") 
    em_flag=email_ending(user_email)#REGEX IMPORTED FUNCTION FROM REGEXREGULATOR
    while em_flag==False:
        print("Invalid email address! ")
        user_email =input("Enter your email: ")
        em_flag=email_ending(user_email)
    #do something to make sure they cannot enter nothing-for both 
    result= curs.execute("SELECT * FROM user WHERE email=?",
    (user_email,))
    row=result.fetchone()
    if row!=None:
        #print("Account already exist, yay you did it")
        resp=input('Account already created. Enter yes to sign in and no to exit: ')
        while not resp or resp[0].lower() not in ("y","n"):
            resp=input("Invalid response. Enter yes to log in and no to leave: ")
        if resp[0].lower()=='y' :
            verify_user()
            return #do this to get rid of bug if they press yes new account but enter exisiting email
        else:
            print("Bye!")
            return 
    print("Password must contain: \n-8 Charchters \n-1 Uppercase letter \n-1 Lowercase letter \n-1 number \n-1 Special charchter")
    #display password rules, enter password and check if follows rule, if fails loop until sucseeds, exit loop and make sure enter same thing twice
    user_pass = getpass.getpass("Enter Password: ")
    pa_flag=pssWrd(user_pass)#IMPORTED FROM PASS RULES checking the password follows policy for storng password
    #print("Password must be 8 charchters minimum.")
    #user_pass = getpass.getpass("Enter Password: ")
    while pa_flag==False:
        print("Invalid Password\n")
        user_pass = getpass.getpass("Enter Password: ")
        pa_flag=pssWrd(user_pass)
    double_pass = getpass.getpass("Confirm password: ")
    #check if the password (plain text verision) match before we pass it on and hash them
    #check if the two passwords entered are the same, we dont need to check if it matches the policy bec the first password does
    #and we wouldnt be able to get out of the loop
    while user_pass!=double_pass:
        print("Password does not match! \nPlease re-enter password.")
        double_pass = getpass.getpass("Confirm Password: ")

    register_User(user_email, user_pass)


#passing user email, and user password
def register_User(em,a):
    #get a random salt to make it more secure, we need to keep track of this salt to use 
    #for the pbkdf2 and to store it in the db so we can access it
    salt=salter()
    #send the password and the salt to get the hasher
    digest=hasher(a, salt)
     

    #if the user enter the password correct both times we store in dict 
    #if its a new user/email wasnt used before 
    # okay so we generate a salt , then we take the salt and password to the hash
    #then we open up the db and we store the salt in hex and the hasher in hex 
    #so then we to compate we need to take the stored salt with the entered password send that to hasher and see 
    #if the two match up
    #CHANGE TO DB
    result= curs.execute("SELECT * FROM user WHERE email=?",
    (em,))
    row=result.fetchone()
    if row==None:
        #use a place holder and pass the python variable seperatly
        #to bind python values to sql statements to avoid sql injection attacks
        curs.execute(""" 
        INSERT INTO user VALUES
        (?, ?, ?)""",
        (em, salt.hex(), digest))
        con.commit() #commit to db
        #we need to pass the salt from previous
        #we need to make it from bytes to string, we passed digest as a hash
        #db[em]= salt.hex(), digest
        #OPEN FILE AND WRITE TO OUR DB
        #a will append to end of the file (w will overwrite everything)
        #with open ('hashPassdb.txt', "a") as file_object:
            #we need to write the information in our file/"db" now that we used dictionary and know it doesnt exist
            #.hex will convert the byte to a prinatble string
            #file_object.write("\n" + em +" "+salt.hex()+" "+digest)
        print("User entered into database.")
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
            print("Bye!")
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
            resp=input("Press y to create an account. Press n to exit program: ")
            while not resp or resp[0].lower() not in ("y", "n"):
                resp=input("Invalid response. Enter yes or no.")
            if resp[0].lower()=='y' :
                input_new_user()
            else :
                print("Bye!")
                return
    while login_attempt>0: #still have tries left 
        user_pass=getpass.getpass("enter your password ")
        #now we take the password they enter and pass along the stored salt to hasher
        #then we compare if the two are the same
    #they enter username and password check if the email and the hash of the password are in and match 
        #go get the hash of user_pass
        #we need to pass this salt which is the second element in our db
        #since we have our email as the key in the db and the salt and hash as a tuple we do this
        #we have to encode the salt bec we stored it as a hex string in our dictionary
        #we are getting the inver back to byte
        #getting first element of the tuple
        salt_hex=db[user_email][0]
        #we convert the salt back to byte (hex in doc easier to read)
        salt_byte=bytes.fromhex(salt_hex)
        #were passing out password string and our salt in byte to get hashed
        hex_ver=hasher(user_pass, salt_byte)
        #now we compare if the hash above is equal to the stored has
        #we are getting the second element of the tuple which is the hash of the salt and password
        #and we comapre it with the newly generated hash
        #DO WE NEED TO CHANGE BYTE/HEX
        if db[user_email][1]==hex_ver:
            print("user logged in successful")
            return
        #now that we know the user exists we dont have to loop through dictionary
        #we can just check if thats the value
        #if db[user_email]==hex_ver: # if teh dictionary key of the input users email euqals the value/password entered
            #print("user logged in successful")
            #return
        else:
         #db[user_email]!=hex_ver:
            login_attempt-=1
            print("Password incorrect.")

    print("Too many log in attempts!")
    print("Bye!")
    return

user_status()