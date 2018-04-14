'''
this programme draw n i.i.d normal and cauchy distribution 
and also take mean and median and find its asymptotic behaviour
when n->infinity 
'''
import numpy as np
from numpy import mean
import matplotlib.pyplot as plt
import seaborn as sns


def SampleCollection():
    """ x denote the Normal I.I.D r.v. and y denote 
    Cauchy I.I.D r.v"""
    x_mean=[]
    y_mean=[]
    x_median=[]
    y_median=[]
    
    for i in range(1,1001):
        x=np.random.standard_normal(i)
        x_mean.append(np.mean(x))
        y=np.random.standard_cauchy(i)
        y_mean.append(np.mean(y))
        x_median.append(np.median(x))
        y_median.append(np.median(y))
    
    N=range(1,1001)
    
    sns.set()
    
    fig=plt.figure(1, facecolor="yellow")
    plot1=fig.add_subplot(2,2,1,facecolor='white')
    plot2=fig.add_subplot(2,2,2,facecolor='white')
    plot3=fig.add_subplot(2,2,3,facecolor='white')    
    plot4=fig.add_subplot(2,2,4,facecolor='white') 
    
    
    plot1.plot(N,x_mean,"red")
    plot2.plot(N,y_mean,"black")
    plot3.plot(N,x_median,"red")
    plot4.plot(N,y_median,"black")
    
    plot1.set_title("X mean")
    plot1.set_xlabel("sample no.")
    plot1.set_ylabel("mean")
    
    plot2.set_title("y mean")
    plot2.set_xlabel("sample no.")
    plot2.set_ylabel("mean")
    
    plot3.set_title("X median")
    plot3.set_xlabel("sample no.")
    plot3.set_ylabel("median")
    
    
    plot4.set_title("Y Median ")
    plot4.set_xlabel("sample no.")
    plot4.set_ylabel("median")
    
    plt.show()
    
    
    
    
SampleCollection()   
  
    
    
    
    
    