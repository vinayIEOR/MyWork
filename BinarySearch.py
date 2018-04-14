"""implementation of Binary Search """

#import numpy as np
Prime=[2]
def GenratePrimeNo(number):
    for i in range(2,10000):
        for j in range(2,i):
            if i%j==0:
                break
            elif j+1==i:
                Prime.append(i)
        if len(Prime)==number:
                    break
    return Prime       
                
def BinarySearch(No):
    Array= GenratePrimeNo(100)
    print(Array)
   
    def Method(Max,Min):
        try:
            index=int((Max+Min)/2)
            if Array.index(No)==index:
                print(index)
            elif Array.index(No)<index:
                Max=index-1
                Method(Max, Min)
            elif Array.index(No)>index:
                Min=index+1
                Method(Max, Min)
        except:
            print("Given No. is Not prime")
    Method(len(Array)-1,0)
        
    
            
BinarySearch(217)        