import hashlib
'''
 take in the username and pasword then hash the password to store for
first time user and then ask the user to enter the username and password and double check with the hash
'''

user_email =input("enter your email ") #do the string regex to make sure it ends in @gmail @email @yahoo etc .com
user_pass=input("enter your password ")
double_pass=input("please enter your password again to verify ")
md5_pass1=hashlib.md5()
md5_pass2=hashlib.md5()
md5_pass1.update(user_pass.encode()) #we need to encode to convert from string to byte so we can hash
md5_pass2.update(double_pass.encode())
digest1=md5_pass1.hexdigest()
digest2=md5_pass2.hexdigest()
if digest1==digest2:
    print("passwords match")
else:
    print("passwords dont match")
    #loop back to reenter password?

