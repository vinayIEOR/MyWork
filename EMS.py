import pandas as pd
import numpy as np
from pulp import *


def Data(ResponseTime):
    """ Import Data And form File Pop and Time
    and also convert time data to binary time data according
    to threshold value of Response time
    """
    
    PopulationDF=pd.read_csv('pop.txt',sep='  ',header=None,names=['loc','pop'],engine='python')
    TimeMat=pd.read_csv('time.txt',sep=' ',header=None)
    PopulationDF.set_index('loc', inplace=True)
    
    del TimeMat[40]
    
    BoolData=TimeMat<= ResponseTime
    BoolDataN=BoolData*1
    Population=PopulationDF.values
    
    
    return (BoolDataN.values,Population.flatten())

def EMSFunc(ResponseTime):
    
    TimeBinaryData , PopulationData = Data(ResponseTime)

    
    prob = pulp.LpProblem('AmbulanceLocation5', pulp.LpMaximize)
    
    CandidateLocation = range(40)
    DemandLocation= range(85)
    # Candidate location variable
    x = LpVariable.dicts('x',CandidateLocation ,upBound=1, lowBound=0,cat=pulp.LpInteger)
    # variable that ensure coverage should at least twice 
    u = LpVariable.dicts('u',DemandLocation,upBound=1, lowBound=0,cat=pulp.LpInteger)
    
    # Objective
    prob += lpSum(PopulationData[i]*u[i] for i in range(85))
    
    # Constraint
    
    #prob+= lpSum((TimeBinaryData[1,j]*x[j]-u[1]) for j in range(40))>=1
    for i in range(85):
        prob += lpSum((TimeBinaryData[i,j]*x[j])-u[i] for j in range(40) ) >=1
        
    #for i in range(85):
     #   prob += y[i]>=1
        
    prob += lpSum(x[j] for j in range(40))==3


    
    
    #prob += lpSum([[TimeBinaryData[i,j]*x[j]-u[i] for j in range(40)] for i in range(85)])>=1
     
    
    prob.solve()
    
    print ("Status:", LpStatus[prob.status])
    
    print ("objective value = ", value(prob.objective))
    
    for Loc in CandidateLocation:
        if x[Loc].varValue==1:
            print("Candidate Location = ", Loc+1)
    for i in DemandLocation:
        print(u[i].varValue)
    
    prob.writeLP("EMS111.lp")

  
EMSFunc(10)
    
    
    
    
      
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    
