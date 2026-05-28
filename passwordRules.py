import re
#implement password rules
#Password must contain 8 Charchters 1 Uppercase letter 1 Lower case letter 1 number 1 Special charchter

def pssWrd(pas):
    #print("Check password against rules")
    #or we can just make a general patten and check 
    #firs we have to check length 
    if len(pas)>=8:
        #Once its 8 or more charchters we can no check for pattern
        #check pattern seperately so we can clearly say what they are missing 
        patternUpper=""
        patternLower=""
        patternNum=""
        patternSpec=""
    #or we can do variables 
    #variables for each to check

    if patternUpper!=None and patternLower!=None and patternNum!=None and patternSpec!=None:
        return True
    else:
        return False
    eightChar=False 
    upperChar=False
    lowerChar=False
    numChar=False
    specChar=False

    if eightChar!=True and upperChar!=True and lowerChar!=True and numChar!=True and specChar!=True:
        #need to check bec regarding re we recieve none
        return False
    else:
        #password hits all requierments
        return True
  
