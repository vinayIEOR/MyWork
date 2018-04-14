def Data(ResponseTime):
    PopulationDF=pd.read_csv('pop.txt',sep='  ',header=None,names=['loc','pop'])
    TimeMat=pd.read_csv('time.txt',sep=' ',header=None)
    PopulationDF.set_index('loc', inplace=True)
    del TimeMat[41]
    BoolData=TimeMat<= ResponseTime
    BoolDataN=BoolData*1
    Population=PopulationDF.values
    
    return (BoolDataN.values,Population.flatten(),TimeMat)


def EMSFunc(ResponseTime):
    
    TimeBinaryData , PopulationData, TimeData = Data(ResponseTime)
    #print(PopulationData[0:5])
    
    prob = pulp.LpProblem('AmbulanceLocation3', pulp.LpMinimize)
    
    CandidateLocation = range(40)
    DemandLocation= range(85)
    
    x = LpVariable.dicts('x',CandidateLocation ,upBound=1, lowBound=0,cat=pulp.LpInteger)
    y= LpVariable.dicts('y',DemandLocation,upBound=1, lowBound=0,cat=pulp.LpInteger)
    
    prob += lpSum(x[j]*TimeBinaryData[i,j]*TimeData[i,j] for i in range(85) for j in range(40))
    
    # constraint
    
    #prob +=
    
    