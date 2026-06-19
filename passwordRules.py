import re
#implement password rules
#Password must contain 8 Charchters 1 Uppercase letter 1 Lower case letter 1 number 1 Special charchter

def pssWrd(pas):
    #print("Check password against rules")
    #or we can just make a general patten and check 
    #firs we have to check length 
    #while len(pas)>8:
        ##return False
        #Once its 8 or more charchters we can no check for pattern
        #check pattern seperately so we can clearly say what they are missing 
    if len(pas)>8:
        passCount=False
    else:
        passCount=True
    patternUpper="[A-Z]+" #needs to include at least one upper case
    patternLower="[a-z]+" #needs to include at least one lower case
    patternNum="[0-9]+" #needs to include at least one number
    patternSpec="[`~!@#$%^&*()_\-\+={\'}\]:;\[?/>.<,\"]+" #needs to include one speical charchterhow to include [] "'think need ""
    #or we can do variables 
    #variables for each to check

    #SEE UP RE SEARCHING
    patUp=re.search(patternUpper, pas)
    patLo=re.search(patternLower,pas)
    patNum=re.search(patternNum, pas)
    patSpe=re.search(patternSpec, pas)
    #we want to let them know all the check they didnt pass to make a stronger password 
    #so will set a flag called retCount so it wont return on first instance of missing , if the flag is greater than 0 returns false
    retCount=0
    if passCount==True and patUp!=None and patLo!=None and patNum!=None and patSpe!=None:
            #we get none if the pattern wasnt found, all pattenrs are found the password is good
            #nested inside the length check 
        return True
    if patUp==None:
        print("Password needs an uppercase charachter.")
        retCount+=1
    if patLo==None:
        print("Password needs a lowercase charchter.")
        retCount+=1
    if patNum==None:
        print("Password needs a number charchter.")
        retCount+=1
    if patSpe==None:
        print("Password needs a speical charchter. ")
        retCount+=1
    if retCount>0:
        return False
    else:
        return True
        
  