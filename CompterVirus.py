'''
this progemme is use to simulate the situation where virus
spread by mail in student class and see example LAB09 ex2
'''
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
Virus_infect=[]
random.seed(42)

def simvirus(n):
    """At start bindu's (1st "start") computer infected with virus"""
    
    infect_com=[1]
    N=range(1,n+1)  # total no. of maillist stored in bindu's computer including bindu
    
    def sample():
        choice=random.choice(N)
        if choice == infect_com[-1]:
            choice=sample()
        return choice
    Choice=sample()
    
    
    while (Choice not in infect_com):
        infect_com.append(Choice)
        Choice=sample()
        
                
    return(len(infect_com))
          
    
   
    
for i in range(0,1000):
    c=simvirus(20)
    Virus_infect.append(c)

print("Expected no. of computer infected with virus: "+str(np.mean(Virus_infect)))
sns.set()
plt.hist(Virus_infect, bins=50,color="red",histtype="bar")
plt.xlabel("no.of computer infected")
plt.ylabel("frequency")
plt.tick_params(axis=2)
plt.title("Histogram of No. of computer infected")
plt.show()



    

    
