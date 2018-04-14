'''
This programme use for decide how to stock when we have past data of sell
Milk.txt is past 500 day demand and we have to calculate the 
how much to stock thus milk man get maximum profit
'''
import numpy as np
import matplotlib.pyplot as plt

data=[]
Readfile=open("milk.txt", 'r')
Readline=Readfile.readline()
while Readline:
    data.append(int(Readline))
    Readline=Readfile.readline()


def Analysis(data):
    mean=np.mean(data)
    std=np.std(data)
    
    print("mean of given data: "+str(mean))
    print("Standard deviation of given data: "+str(std))
    
    
    time=range(1,501)
    plt.plot(time,data)
    plt.xlabel("Days")
    plt.ylabel("demand in days")
    plt.title("demand of Milk in 500 days")
    plt.show()
    
    plt.hist(data)
    plt.xlabel("Demand of milk in day")
    plt.ylabel("frequency of demand")
    plt.title("Histogram of Demand")
    plt.show()
    
    
def ExpectedProfit(data,stock):
    dailyStock=stock
    dailyProfit=[]
    for demand in data:
        Def= demand-dailyStock
        if Def>0:
            profit=dailyStock*6
        else:
            profit=(demand*6+Def*2)
        dailyProfit.append(profit)
    ExProf=np.mean(dailyProfit)
    return ExProf
    if stock is 1000:
        print("Expected profit for daily 1000L stock is: "+str(ExProf))
   
   

    
def optimalStock(data):
    #print("For different stock quantity analysis the optimal stock")
    
    stock=[]
    profitList=[]
    for i in range (500,2500,50):
        stock.append(i)
    for s in stock:
        profit=ExpectedProfit(data, s)
        profitList.append(profit)
        if s == 1000:
            print("Expected profit for daily 1000L stock is: "+str(profit))
            print("\n")
    
    maxProf=max(profitList)
    index=profitList.index(maxProf)
    optiStock=stock[index]
    print("optimal daily milk stock is: "+str(optiStock)+" with maximum profit "+str(maxProf))
    
    plt.plot(stock,profitList)
    plt.show()
        
    
        
       
            
        
Analysis(data)      
optimalStock(data)



"""mean is= 998.07
standard deviation= 155.372253314
5498.848"""


