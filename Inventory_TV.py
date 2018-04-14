#import pandas


'''
this is programme is deal with multistage inventory system 
we have 100 week demand and 4 supply stages with lead time and 
holding cost at certain stage. we try to find Avg. inventory holding cost 
'''
data=[]
Readfile=open("tv.txt", 'r')
Readline=Readfile.readline()
while Readline:
    data.append(int(Readline))
    Readline=Readfile.readline()
print(len(data))
    

def InventoryCost(data):
    orderQuantity=5000
    #at start we assume order is processed at every week at start of week
    for i in range(0,len(data)):
        x=orderQuantity-data[i]
        if x>0:
            ExcessQuantity=x
        else:
            BackOrder=x
        
        
        
        


    