import re
#regex regulations to ensure the user only enters a proper email address domain 

def email_ending(ema):
    #the patter will be the email address regex regulations and the em will be the email we recieved from user  
    pattern="^[a-zA-Z0-9]+[a-zA-Z0-9!#$%&'*+-/=?^_`{|}~]*@[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*\\.com$"
    '''the pattern: it starts off with at least one letter or number then it can be any letter, number, or any 
    of the speical charchters that are allowed none or more times followed by an @ sign then it is at least 
    one letter. It has the potential to add in an - but if you include that it must be followed by a letter or
    number. then it must end in .com (for now we chose one TLD)'''
    #took the allowed charchters in an email address from stack overflow 
    ending=re.search(pattern, ema)
    if ending!=None:
        return True #valid email we return
    if ending==None: #means the search was unsucsesful is value is None
        #print("Invalid email address")
        return False
        #go back to enter an email? to log in a user 
        #gmail.com, email.com, yahoo.com hotmail.com, aol.com  use top five popular ones

