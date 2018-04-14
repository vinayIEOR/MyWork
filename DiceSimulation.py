"""this program is take no. face and no. dice and add all the of different
and give the how many time each no. will appear """
import random 
import matplotlib.pyplot as plt
import seaborn as sns

def DiceSimulation(n,f,t):
    #f=no. of faces of dice
    #n =no. of dice using
    #t= no. of times experiment repeat
    diceop=[]
    random.seed(101)
    if n==1:
        for i in range (0,t):
            Ex=random.choices(range(1,f+1),k=n)
            diceop.append(Ex[0])
        
        for j in range(1,f+1):
            x=diceop.count(j)
            print(str(j)+" Appears "+str(x)+" Times")
        sns.set()
        plt.hist(diceop, color="blue",bins=50)
        plt.title("Histogram of No. of Time Individual Number Appear")
        plt.xlabel("Individual no. appear in dice")
        plt.ylabel("frequency of individual no.")
        plt.show()
    
    else:
        for i in range (0,t):
            Ex=random.choices(range(1,f+1),k=n)
            diceop.append(sum(Ex))
        for j in range(1,n*f+1):
            x=diceop.count(j)
            if j in diceop:
                print(str(j)+" Appears "+str(x)+" No. of Times")
        sns.set()
        plt.hist(diceop,range=(1,n*f), color="blue",bins=50)
        plt.title("Histogram of No. of Time Individual Number Appear: ")
        plt.xlabel("Individual no. appear in dice: ")
        plt.ylabel("frequency of individual no: ")
        plt.savefig("hist.png",format="png")
        plt.show()   
        

n=int(input("Enter the No. Dice For Simulation: "))
f=int(input("Enter the No. Faces in Dice 6/12: "))
t=int(input("Enter the No. of time Experiments you want: "))

DiceSimulation(n, f, t)
