'''
this program show how central limit theorem work 
'''
import numpy as np
import matplotlib.pyplot as plt

Binom=[]
bernoulli=[]

def Binomial(n,p):
    for i in range(0,10000):
        B=np.random.binomial(n,p)
        Binom.append(B)
    return Binom


def Bernoulli(n,p):  
    for i in range(0,10000):
        Br=np.random.binomial(1,p,size=n) 
        bernoulli.append(sum(Br))
    return bernoulli 
    
n=int(input("enter the value of n"))
p=float(input("enter the value of p"))

Ber=Bernoulli(n, p)
Bnom=Binomial(n, p)

print(np.mean(Ber))
print(np.mean(Bnom))
print(np.std(Ber))
print(np.std(Bnom))

fig=plt.figure(facecolor="yellow")
hist1=fig.add_subplot(2,1,1)
hist2=fig.add_subplot(2,1,2)

hist1.hist(Ber)
hist2.hist(Bnom,color="red")

hist1.set_title("Bernoulli Distribution with n "+str(n)+" p "+str(p))
hist1.set_xlabel("outcome")
hist1.set_ylabel("frequency")

hist2.set_title("Binomial Distribution with n "+str(n)+" p "+str(p))
hist2.set_xlabel("outcome")
hist2.set_ylabel("frequency")

plt.show()



"""
n=1000,p=.4
400.2275
399.7732
15.4634777379
15.4627216802


n=100,p=.4
39.9975
40.0508
4.9028658711
4.89781781613

n=1000,p=.6
599.9961
600.0238
15.6063219495
15.3396881833

n=100,p=.6
59.9993
59.9178
4.84257158027
4.93449522849




"""


