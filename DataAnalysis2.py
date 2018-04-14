""" analysing large data file  using chunksize in pandas """
import pandas as pd
import matplotlib.pyplot as plt

def DataAnalysis(file,CountryCode):
    DFpop_data=pd.read_csv(file,chunksize=1000) #population data from file in 1000 line bunch
    new_DF=pd.DataFrame()
    
    for P_Data in DFpop_data:
        
        #Check out specific country by CountryCode EUU europe union
        DFPop_EUU=P_Data[P_Data["CountryCode"]==CountryCode]
        # Zip DataFrame columns of interest: pops
        pops_list= list( zip(DFPop_EUU['Total Population'],DFPop_EUU['Urban population (% of total)']))
        # Use list comprehension to create new DataFrame column 'Total Urban Population'
        #DFPop_EUU= DFPop_EUU.assign(UrbanPopulation =[int(tup[0]*tup[1]*.01) for tup in pops_list])
        DFPop_EUU["UrbanPopulation"]=[int(tup[0]*tup[1]*.01) for tup in pops_list]
        #make whole DataFrame for all iteration append in new_DF
        new_DF=new_DF.append(DFPop_EUU)
    return(new_DF['Year'],new_DF['UrbanPopulation'])

tupARB=DataAnalysis("world_ind_pop_data.csv","ARB")
tupEUU=DataAnalysis("world_ind_pop_data.csv","EUU")

fig=plt.figure(facecolor="yellow")
graph1=fig.add_subplot(2,1,1)
graph2=fig.add_subplot(2,1,2)

graph1.plot(tupARB[0],tupARB[1])
graph2.plot(tupEUU[0],tupEUU[1])

plt.show()

       