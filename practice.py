import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
file=pd.read_csv("Klout.csv",header=None )
fileArray=file.values
fileArray=fileArray.flatten()
def Sample(Array,SampleSize,Trial):
    SampleData=np.empty(Trial)
    for i in range(Trial):
        Samplle=random.choices(Array,k=SampleSize)
        SampleData[i]=np.mean(Samplle)
        
    return SampleData

data=Sample(fileArray, 35, 10000)
print(np.mean(data),np.std(data))

plt.hist(data,bins=50)
plt.show()  

        
        
