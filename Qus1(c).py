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

    
    prob = pulp.LpProblem('AmbulanceLocation2', pulp.LpMaximize)
    
    CandidateLocation = range(40)
    DemandLocation= range(85)
    
    x = LpVariable.dicts('x',CandidateLocation ,upBound=1, lowBound=0,cat=pulp.LpInteger)
    y= LpVariable.dicts('y',DemandLocation,upBound=1, lowBound=0,cat=pulp.LpInteger)
    
    # Objective Function
    prob += lpSum(PopulationData[i]*x[j]*TimeBinaryData[i,j] for j in range(40) for i in range(85))
    
    # Constraint 1
    for i in range(85):
            prob += lpSum(TimeBinaryData[i,j]*x[j] for j in range(40) ) >=y[i]
    
    # Constraint 2
    prob += lpSum(x[i] for i in range(40))<=3
    
    prob.solve()
    
    print ("Status:", LpStatus[prob.status])
    print ("Total Coverage of population from all Ambulance = ", value(prob.objective))
    
    for Loc in CandidateLocation:
        if x[Loc].varValue==1:
            print("Candidate Location = ", Loc+1)
    
    
    
EMSFunc(10)



