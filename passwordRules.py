import re
#implement password rules
#Password must contain 8 Charchters 1 Uppercase letter 1 Lower case letter 1 number 1 Special charchter

def pssWrd(pas):
    #print("Check password against rules")
    #variables for each to check
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
  
