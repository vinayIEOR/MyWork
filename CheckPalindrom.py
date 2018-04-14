""" Using recursive method find given string is a palindrom
or not"""
import numpy as np
def CheckPalindrom(string):
    if len(string)<=1:
        print("Given string is palindrom")
    else:
        if string[0]==string[-1]:
            string=string.strip((string[0]+string[-1]))        

            CheckPalindrom(string)
        else:
            print("string is not palindrom")
        
#CheckPalindrom("rotor")
count=1
def NoElimination(Array):
    global count
    """
    * Qus from brilliant.org  
    step1- remove number from all odd position
    step2- than remove number from all even position
    step3- if more than one no. remaining on list
            repeat step 1 and 2 nd respectively
    """
    def OddNoElimination(Array):
        global count
        
        A=np.delete(Array,[i for i in range(len(Array)) if i%2==0])
        count+=1
        #print("ODD",count)
        return A
    def EvenNo(Array):
        global count
        A=np.delete(Array,[i for i in range(len(Array)) if i%2!=0])
        count+=1
        #print("Even",count)
        return A
    
    while True:
        if len(Array)==1:
            break
        
        elif count%2 != 0:
            Array=OddNoElimination(Array)
        else:
            Array=EvenNo(Array)
    return Array



A=NoElimination(np.arange(1,12345))
print(A)

        
    
            
            
            
             