import re
#regex regulations to ensure the user only enters a proper email address domain 

def email_ending(ema):
    #the patter will be the email address domain and the em will be the email were searching 
    pattern="^[a-zA-Z0-9]+[a-zA-Z0-9!#$%&'*+-/=?^_`{|}~]*@[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*\.com$"
    #(email.com|gmail.com|yahoo.com|aol.com|hotmail.com|icloud.com)
    #took the allowed charchters in an email address from stack overflow 
    ending=re.search(pattern, ema)
    #result = find_first('Harker$')
    if ending!=None:
        return #valid email we return
    if ending==None: #means the search was unsucsesful is value is None
        #print("Invalid email address")
        return False
        #go back to enter an email? to log in a user 
        #gmail.com, email.com, yahoo.com hotmail.com, aol.com  use top five popular ones

#set a flag to false and loop though keep asking to enter proper email
#loop untill enter a correct email switch the flag and send it back to other code
#the other code will have a vairbale and fall this code so we use that for the email 