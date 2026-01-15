import re
#regex regulations to ensure the user only enters a proper email address domain 

def email_ending(ema):
    #the patter will be the email address domain and the em will be the email were searching 
    #punct = "[^a-zA-Z0-9]"
    pattern="(a-zA-Z0-9!#$%&'*+-/=?^_`{|}~]+  @ email.com$|gmail.com$|yahoo.com$|aol.com$|hotmail.com$|icloud.com$)"
    #pattern=('@email.com|@gmail.com|yahoo.com|aol.com|hotmail.com|icloud.com$')
    ending=re.search(pattern, ema)
    #result = find_first('Harker$')
    if ending!=None:
        return #valid email we return
    if ending==None: #means the search was unsucsesful is value is None
        print("Invalid email address")
        #go back to enter an email? to log in a user 
        #gmail.com, email.com, yahoo.com hotmail.com, aol.com  use top five popular ones