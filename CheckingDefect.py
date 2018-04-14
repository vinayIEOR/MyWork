'''
Lab10 ex2 checking defected piece for manufacturing plant
'''
import numpy as np
import matplotlib.pyplot as plt




def qCheck(N):
    product=range(1,N+1)
    productRadius=np.random.normal(loc=10.0, scale=.2, size=N)
    
    # product for Selection
    
    def selection(n,p):
        List=[]
        
        for i in range(0,n):
            instant=np.random.binomial(1,p)
            if instant==1:
                List.append(product[i])
        return List
    
    TestSelected=selection(N, 0.3)
    
    test1Pass_Ndef=[]
    test1Pass_Def=[]
    test1Fail_Def=[]
    test1Fail_Ndef=[]
    
    for i in TestSelected:
        # index i-1 selected because product start from 1..N and there is 1 more indexing in radius 
        if productRadius[i-1]>9.7 and productRadius[i-1]<10.3:
            a=np.random.binomial(1,.001)
            if a==0:
                test1Pass_Ndef.append(i)
            else:
                test1Pass_Def.append(i)
        else:
            a=np.random.binomial(1,.95)
            if a==1:
                test1Fail_Def.append(i)
            else:
                test1Fail_Ndef.append(i)
        
        test1pass= test1Pass_Ndef + test1Fail_Ndef 
        test1Fail= test1Fail_Def+test1Pass_Def
    
    test2pass_Ndef=[]
    test2pass_Def=[]
    test2Fail_Def=[]
    test2Fail_Ndef=[]
       
    for i in test1pass:
        b=np.random.binomial(1,.995)
        if b==1:
            b1=np.random.binomial(1,.005)
            
            if b1==1:
                test2pass_Def.append(i)
            
            else:
                test2pass_Ndef.append(i)
        
        else:
            b1=np.random.binomial(1,.99)
            
            if b1==1:
                test2Fail_Def.append(i)
            else:
                test2Fail_Ndef.append(i)
    
    test2pass= test2pass_Ndef + test2Fail_Ndef
    test2Fail= test2Fail_Def + test2pass_Def
        
    FractionDef = len(test1Fail+test2Fail)/N 
    
    W_radius_W_paint= len(test1Fail_Def+test1Fail_Ndef+test2Fail_Def+test2Fail_Ndef)/N
    
    RradiusRpaint_def= len(test1Pass_Def+test2pass_Def)/N
    
    WradusWpaint_Ndef = len(test1Fail_Ndef+test2Fail_Ndef)/N
    
    return (FractionDef,W_radius_W_paint,RradiusRpaint_def,WradusWpaint_Ndef)
    
            
        
def simulation_def(N,size=1):
    Mean_array=np.empty(4)
    list_all=np.array([qCheck(N) for i in range(size)])
    transpose_list=np.transpose(list_all)
    for i in range(4):
        Mean_array[i]=np.mean(transpose_list[i])
    
    
    print(Mean_array)
    plt.plot(list_all,alpha=.8)
    plt.show()
    





simulation_def(1000, size=1000)

"""
L_FrictionDef=[]  
L_W_radius_W_paint=[]
L_RradiusRpaint_def=[]
L_WradusWpaint_Ndef=[]
 print("the fraction of products that were thrown out as defective:  "+str(FractionDef))
print("the fraction of products that either had wrong paint or did not have radius between 9.6cm and 10.4cm  :"+str(W_radius_W_paint))

print(the fraction of products that had the right paint and radius between 9.6cm and 10.4cm, 
    but were still classified as defective  +str(RradiusRpaint_def))
 L_WradusWpaint_Ndef.append(WradusWpaint_Ndef)
    print(the fraction of products that had either wrong paint or wrong radius but were not thrown
              out   :+str(WradusWpaint_Ndef))

"""




"""
N=1000
the fraction of products that were thrown out as defective: 0.0402

the fraction of products that either had wrong paint or did not have radius between
9.6cm and 10.4cm.:-0.04178

the fraction of products that had the right paint and radius between 9.6cm and 10.4cm,
but were still classified as defective.-0.00161224489796

the fraction of products that had either wrong paint or wrong radius but were not thrown
out.-0.001929




"""
        
        
    