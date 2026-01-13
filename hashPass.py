import hashlib
'''f
use a struct or a dict with key values maybe take in the username and pasword then hash the password to store for
first time user and then ask the user to enter the username and password and double check with the hash
so enter a user name and store enter a password hash and store hash ask to double check password and hash and double 
check then once in system user can enter infroamtion check if the hash they enter matches and log in
'''

user_email =input("enter your email ")
user_pass=input("enter your password ")
double_pass=input("please enter your password again to verify")
md5_pass1=hashlib.md5()
md5_pass2=hashlib.md5()
md5_pass1.update(user_pass)
md5_pass2.update(double_pass)
digest1=md5_pass1.hexdigest()
digest2=md5_pass2.hexdigest()
if digest1==digest2:
    print("passwords match")
else:
    print("passwords dont match")
    #loop back to reenter password?